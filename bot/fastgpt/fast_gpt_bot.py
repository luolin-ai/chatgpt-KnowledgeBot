import requests
import time
from common.log import logger
from bridge.context import Context
from bridge.reply import Reply, ReplyType
from bot.bot import Bot
from bot.chatgpt.chat_gpt_session import ChatGPTSession
from bot.session_manager import SessionManager
from config import conf


class FastGptBot(Bot):
    # authentication failed
    AUTH_FAILED_CODE = 401

    def __init__(self):
        self.base_url = "http://api.gojiberrys.cn/api/openapi"
        self.sessions = SessionManager(ChatGPTSession, model=conf().get("model") or "gpt-3.5-turbo")

    def reply(self, query, context: Context = None) -> Reply:
        return self._chat(query, context)

    def _chat(self, query, context, retry_count=0):
        if retry_count >= 2:
            # exit after maximum number of retries
            logger.warn("[FASTGPT] failed after maximum number of retry times")
            return Reply(ReplyType.ERROR, "请再问我一次吧")

        try:
            session_id = context.get("session_id")  # Use .get() to handle None case
            session = self.sessions.session_query(query, session_id)

            # remove system message
            if session.messages and session.messages[0].get("role") == "system":
                session.messages.pop(0)

            # load config
            fastgpt_api_key = conf().get("fastgpt_api_key")
            model_id = conf().get("fastgpt_model_id")
            logger.info(f"[FASTGPT] query={query}, model_id={model_id}")

            # convert session.messages to required format
            prompts = []
            for msg in session.messages:
                if "role" in msg and "content" in msg:
                    prompt = {"obj": msg["role"], "value": msg["content"]}
                    prompts.append(prompt)
                else:
                    logger.warn(f"[FASTGPT] Invalid message format: {msg}")

            body = {
                "chatId": session_id,
                "modelId": model_id,
                "isStream": False,
                "prompts": prompts
            }
            headers = {"apikey": fastgpt_api_key, "Content-Type": "application/json"}

            # do HTTP request
            logger.info(f"[FASTGPT] Request body: {body}")

            response = requests.post(url=f"{self.base_url}/chat/chat", json=body, headers=headers)
            
            #logger.info(f"THIS IS BASE URL BELLOW:")
            #logger.info(f"{self.base_url}/chat/chat")
	        #logger.info(response.json())
		  
            logger.info(f"[FASTGPT] Response status code: {response.status_code}")
            logger.info(f"[FASTGPT] Response content: {response.content}")

            if response.status_code == 200:
                res = response.json()
                #return Reply(ReplyType.CHAT, res.get("data"))
                return Reply(ReplyType.TEXT, res.get("data"))
                #return Reply(ReplyType.CHAT,response.content)
                logger.info(response.status_code)

            else:
                # retry
                time.sleep(2)
                logger.warn(f"[FASTGPT] do retry, times={retry_count + 1}")
                return self._chat(query, context, retry_count + 1)

        except Exception as e:
            logger.error(f"[FASTGPT] Exception: {str(e)}")
            logger.error(f"[FASTGPT] API response content: {response.content.decode('utf-8')}")
            return Reply(ReplyType.ERROR, "An error occurred, please try again.")
