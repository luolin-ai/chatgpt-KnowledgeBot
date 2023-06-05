import datetime
import requests
from common.log import logger
from bridge.context import Context
from bridge.reply import Reply, ReplyType
from bot.bot import Bot
from bot.chatgpt.chat_gpt_session import ChatGPTSession
from bot.session_manager import SessionManager
from config import conf

class luolinaiBot(Bot):
    AUTH_FAILED_CODE = 401

    def __init__(self):
        self.base_url = "https://api.gojiberrys.cn/api/openapi"
        self.sessions = SessionManager(ChatGPTSession, model=conf().get("model") or "gpt-3.5-turbo")
        self.reply_counts = {}
        self.last_update_date = datetime.date.today()
        self.max_daily_replies = conf().get("max_daily_replies", 10)
        self.max_single_chat_replies = conf().get("max_single_chat_replies")
        self.max_group_chat_replies = conf().get("max_group_chat_replies")
        self.ad_message = conf().get("ad_message")

    def reply(self, query, context: Context = None) -> Reply:
        # Get the WeChat nickname from the context
        wechat_nickname = context.get("wechat_nickname")

        # Check if we've moved to a new day since the last update
        if datetime.date.today() != self.last_update_date:
            # If so, reset the reply counts and update the date
            self.reply_counts = {}
            self.last_update_date = datetime.date.today()

        # Check if the user has already reached the maximum number of replies for the day
        if self.reply_counts.get(wechat_nickname, 0) >= self.max_daily_replies:
            # If so, return an error message
            return Reply(ReplyType.ERROR, "已达到最大回复次数")

        # Otherwise, increment the user's reply count
        self.reply_counts[wechat_nickname] = self.reply_counts.get(wechat_nickname, 0) + 1

        # Continue processing the reply as before...
        reply = self._chat(query, context)

        reply.content += "\n" + self.ad_message  # 在回复内容后添加广告
        return reply

    def _chat(self, query, context, retry_count=0):
        if retry_count >= 5:
            logger.warn("[luolinai] 失败超过最大重试次数")
            return Reply(ReplyType.ERROR, "请再问我一次吧")

        try:
            session_id = context.get("session_id")
            session = self.sessions.session_query(query, session_id)

            if session.messages and session.messages[0].get("role") == "system":
                session.messages.pop(0)

            luolinai_api_key = conf().get("luolinai_api_key")
            model_id = conf().get("luolinai_model_id")
            ad_message = self.ad_message

            prompts = []
            for msg in session.messages:
                if "role" in msg and "content" in msg:
                    prompt = {"obj": msg["role"], "value": msg["content"]}
                    prompts.append(prompt)
                else:
                    logger.warn(f"[luolinai] 无效的消息格式: {msg}")

            body = {
                "chatId": session_id,
                "modelId": model_id,
                "isStream": False,
                "prompts": prompts
            }
            headers = {"apikey": luolinai_api_key, "Content-Type": "application/json"}

            response = requests.post(url=f"{self.base_url}/chat/chat", json=body, headers=headers)

            logger.info(f"[luolinai] 响应状态码: {response.status_code}")
            logger.info(f"[luolinai] 响应内容: {response.content}")

            if response.status_code == 200:
                res = response.json()
                chat_reply = res.get("data")
                if isinstance(chat_reply, str):
                    chat_reply_with_ad = chat_reply + "\n\n" + ad_message
                else:
                    logger.error(f"[luolinai] 回复类型不正确: {type(chat_reply)}")
                    chat_reply_with_ad = str(chat_reply) + "\n\n" + ad_message
                return Reply(ReplyType.TEXT, chat_reply_with_ad)

            else:
                time.sleep(2)
                logger.warn(f"[luolinai] 进行重试，次数={retry_count + 1}")
                return self._chat(query, context, retry_count + 1)

        except Exception as e:
            logger.error(f"[luolinai] 异常: {str(e)}")
            if 'response' in locals():
                logger.error(f"[luolinai] API响应内容: {response.content.decode('utf-8')}")
            return Reply(ReplyType.ERROR, "发生错误，请再试一次。")
