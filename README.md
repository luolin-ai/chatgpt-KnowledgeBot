了# 简介   
# # KnowledgeBot-WeChatGPT
基于微信机器人zhayujie/chatgpt-on-wechat结合fastGPT知识库的一个知识库微信、企业微信、飞书机器人
# ## 项目名称: "KnowledgeBot-WeChatGPT"

项目介绍:
KnowledgeBot-WeChatGPT 是一个基于知识库的微信机器人，它结合了私有化的知识和 GPT 预训练模型，为用户提供智能的对话和知识交流。
该项目利用私有化的知识库作为机器人的知识基础，其中包含了丰富的领域知识、常见问题和解决方案。结合 GPT 预训练模型，KnowledgeBot-WeChatGPT 可以根据a用户的提问和对话内容，通过对知识库和 GPT 模型的综合分析，给出准确、有用的回答和建议。
KnowledgeBot-WeChatGPT 在微信平台上实现了自动回复的功能，用户可以通过与机器人进行对话来获取专业的解答、提供实时信息和获取指导。它能够理解用户的问题，并根据知识库和 GPT 模型的结合，提供个性化、高质量的回复，满足用户的各种需求。
除了基于知识库的回答，KnowledgeBot-WeChatGPT 还充分利用了 GPT 模型的创造性和语言理解能力，能够进行富有趣味性的聊天、角色扮演和文字冒险等交互。它可以与用户进行有趣的对话，提供娱乐和互动体验。
KnowledgeBot-WeChatGPT 的目标是为用户提供高效、智能、有趣的交流体验，通过结合私有化的知识库和 GPT 预训练模型，为用户提供个性化、准确的回答和互动。它将成为用户在微信平台上获取知识和享受智能交流的首选伙伴。
让我们一起与 KnowledgeBot-WeChatGPT 探索知识的深度和语言的魅力，体验与智能机器人的精彩互动！

###欢迎wxKnowledgeBot群
![04be8dc33ffc40738aaff2926c6a1dd](https://github.com/luolin-ai/KnowledgeBot/assets/135555634/722e30ed-d1b6-4904-af45-c7680132c3d3)


最新版本支持的功能如下：

- [x] **多端部署：** 有多种部署方式可选择且功能完备，目前已支持个人微信，微信公众号和企业微信应用等部署方式
- [x] **基础对话：** 私聊及群聊的消息智能回复，支持多轮会话上下文记忆，支持 GPT-3，GPT-3.5，GPT-4模型
- [x] **语音识别：** 可识别语音消息，通过文字或语音回复，支持 azure, baidu, google, openai等多种语音模型
- [x] **图片生成：** 支持图片生成 和 图生图（如照片修复），可选择 Dell-E, stable diffusion, replicate模型
- [x] **丰富插件：** 支持个性化插件扩展，已实现多角色切换、文字冒险、敏感词过滤、聊天记录总结等插件
- [X] **Tool工具：** 与操作系统和互联网交互，支持最新信息搜索、数学计算、天气和资讯查询、网页总结，基于 [chatgpt-tool-hub](https://github.com/goldfishh/chatgpt-tool-hub) 实现


# 快速开始

# 基于自己私有化知识库的的微信机器人
点此登录洛林AI知识交互中心网站 {https://api.gojiberrys.cn/}
点击创建AI
[![img_3](https://github.com/luolin-ai/KnowledgeBot/assets/135555634/9ee74435-c05b-48f7-aa96-1f854787f100)]
如何创建知识库，
![img_4](https://github.com/luolin-ai/KnowledgeBot/assets/135555634/43f444ee-9659-4078-b8fe-f773e1794ac4)导入知识之手动方式
 文件导入 支持 .txt,.doc,.docx,.pdf,.md 文件。Gpt会自动对文本进行 QA 拆分，需要较长训练时间，拆分需要消耗 tokens，账号余额不足时，未拆分的数据会被删除。一个1个文本。 
![img_5](https://github.com/luolin-ai/KnowledgeBot/assets/135555634/020e733e-f802-47f3-954c-91c44aef84dc)

 表格导入 接受一个 csv 文件，表格头包含 question 和 answer。question 代表问题，answer 代表答案。 导入前会进行去重，如果问题和答案完全相同，则不会被导入，所以最终导入的内容可能会比文件的内容少。但是，对于带有换行的内容，目前无法去重。 
![img_6](https://github.com/luolin-ai/KnowledgeBot/assets/135555634/c486400c-6c00-4518-9842-c1cbd0ff6813)

 以上三种方法都可以，根据自己的需求来选择
完成以上操作基本之后点击保存，机器人就可以对上传的知识进行训练了，当训练完成后可以回自动显示到训练之后就在知识库中出现了
创建自己的私有化应用，，关联自己相关的知识库 
![img_7](https://github.com/luolin-ai/KnowledgeBot/assets/135555634/f08aaf28-7328-4a2a-a42f-41227b09bd37)

如何获取 api key 开发页，点击添加新的 Api Key 可获取 ，请在获取后保存，后续将无法再获取该 key，只能删除重新生成。 
![img_8](https://github.com/luolin-ai/KnowledgeBot/assets/135555634/6fc7323d-08fc-4109-884e-e54f7e8cbc63) 如何取 modelId / appId V3.8之后的接口改成了 appId 。两者是同一个东西，主要看接口实际字段。 我的应用编辑页内可获取 
![img_8](https://github.com/luolin-ai/KnowledgeBot/assets/135555634/83de8f35-9e15-4cb3-8cab-0cd7f8d2194f)

###
最新版本支持的功能如下：

- [x] **多端部署：** 有多种部署方式可选择且功能完备，目前已支持个人微信，微信公众号和企业微信应用等部署方式
- [x] **基础对话：** 私聊及群聊的消息智能回复，支持多轮会话上下文记忆，支持 GPT-3，GPT-3.5，GPT-4模型
- [x] **语音识别：** 可识别语音消息，通过文字或语音回复，支持 azure, baidu, google, openai等多种语音模型
- [x] **图片生成：** 支持图片生成 和 图生图（如照片修复），可选择 Dell-E, stable diffusion, replicate模型
- [x] **丰富插件：** 支持个性化插件扩展，已实现多角色切换、文字冒险、敏感词过滤、聊天记录总结等插件
- [X] **Tool工具：** 与操作系统和互联网交互，支持最新信息搜索、数学计算、天气和资讯查询、网页总结，基于 [chatgpt-tool-hub](https://github.com/goldfishh/chatgpt-tool-hub) 实现
### 2.运行环境

支持 Linux、MacOS、Windows 系统（可在Linux服务器上长期运行)，同时需安装 `Python`。
> 建议Python版本在 3.7.1~3.9.X 之间，推荐3.8版本，3.10及以上版本在 MacOS 可用，其他系统上不确定能否正常运行。

**(1) 克隆项目代码：**

```bash
cd KnowledgeBot/
```

**(2) 安装核心依赖 (必选)：**
> 能够使用`itchat`创建机器人，并具有文字交流功能所需的最小依赖集合。
```bash
pip3 install -r requirements.txt
```

**(3) 拓展依赖 (可选，建议安装)：**

```bash
pip3 install -r requirements-optional.txt
```
> 如果某项依赖安装失败请注释掉对应的行再继续。

其中`tiktoken`要求`python`版本在3.8以上，它用于精确计算会话使用的tokens数量，强烈建议安装。


使用`google`或`baidu`语音识别需安装`ffmpeg`，

默认的`openai`语音识别不需要安装`ffmpeg`。


使用`azure`语音功能需安装依赖，并参考[文档](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstarts/setup-platform?pivots=programming-language-python&tabs=linux%2Cubuntu%2Cdotnet%2Cjre%2Cmaven%2Cnodejs%2Cmac%2Cpypi)的环境要求。
:

```bash
pip3 install azure-cognitiveservices-speech
```

## 配置

配置文件的模板在根目录的`config-template.json`中，需复制该模板创建最终生效的 `config.json` 文件：

```bash
```

然后在`config.json`中填入配置，以下是对默认配置的说明，可根据需要进行自定义修改（请去掉注释）：

```bash
配置说明
{{
luolinai_api_key：

作用：洛林AI的API密钥，用于向洛林AI平台发送请求。
使用方法：将您在洛林AI平台获得的API密钥填写到该配置项中。
luolinai_model_id：

作用：指定要使用的洛林AI模型的ID。
使用方法：将您要使用的洛林AI模型的ID填写到该配置项中。
max_single_chat_replies：

作用：单聊模式下每个用户每轮对话的最大回复次数限制。
使用方法：根据您的需求，设置单聊模式下每个用户每轮对话的最大回复次数。
max_group_chat_replies：

作用：群聊模式下每个用户每轮对话的最大回复次数限制。
使用方法：根据您的需求，设置群聊模式下每个用户每轮对话的最大回复次数。
ad_message：

作用：广告消息，将插入到洛林AI的回复中，用于广告宣传。
使用方法：将您想要插入到洛林AI回复中的广告消息内容填写到该配置项中。
single_chat_prefix：

作用：单聊模式下触发对话的关键词列表。当用户发送消息中包含其中任一关键词时，将被视为单聊模式。
使用方法：根据您的需求，设置触发单聊模式的关键词列表。
single_chat_reply_prefix：

作用：单聊模式下洛林AI回复消息时的前缀，用于区分洛林AI的回复。
使用方法：根据您的需求，设置洛林AI回复消息时的前缀。
group_chat_prefix：

作用：群聊模式下触发对话的关键词列表。当用户在群聊中发送消息包含其中任一关键词时，将被视为群聊模式。
使用方法：根据您的需求，设置触发群聊模式的关键词列表。
group_name_white_list：

作用：允许进行群聊的群组名称白名单。只有在白名单中的群组中的消息才会触发群聊模式。
使用方法：根据您的需求，设置允许进行群聊的群组名称白名单。
group_chat_in_one_session：

作用：允许在同一个会话中进行群聊的群组名称列表。同一个群组的消息将在同一个会话中进行处理。
使用方法：根据您的需求，设置允许在同一个会话中进行群聊的群组名称列表。
image_create_prefix：

作用：触发洛林AI生成图片的关键词列表。当用户发送消息以列表中的关键词开头时，洛林AI将尝试生成图片。
使用方法：根据您的需求，设置触发生成图片的关键词列表。
speech_recognition：

作用：是否启用语音识别功能，允许用户通过语音进行对话。
使用方法：根据您的需求，设置是否启用语音识别功能。
group_speech_recognition：

作用：是否在群聊模式下启用语音识别功能，允许群聊中的语音消息进行识别。
使用方法：根据您的需求，设置是否在群聊模式下启用语音识别功能。
voice_reply_voice：

作用：是否启用语音回复功能，允许洛林AI以语音形式回复用户。
使用方法：根据您的需求，设置是否启用语音回复功能。
conversation_max_tokens：

作用：每次对话中的最大令牌数，用于限制对话内容的长度。
使用方法：根据您的需求，设置每次对话中的最大令牌数。
expires_in_seconds：

作用：会话过期时间，指定会话在多长时间后过期，需要重新创建会话。
使用方法：根据您的需求，设置会话的过期时间。
character_desc：

作用：洛林AI的角色描述，用于向用户介绍洛林AI的身份和功能。
使用方法：根据您的需求，设置洛林AI的角色描述。
subscribe_msg：

作用：关注公众号时发送的欢迎消息，向用户展示洛林AI的功能和指令。
使用方法：根据您的需求，设置关注公众号时发送的欢迎消息内容。
max_daily_replies：

作用：每个用户每天的最大回复次数限制。
使用方法：根据您的需求，设置每个用户每天的最大回复次数限制。
max_hourly_replies：

作用：每个用户每小时的最大回复次数限制。
使用方法：根据您的需求，设置每个用户每小时的最大回复次数限制。
max_message_length：

作用：消息的最大长度限制，超过该长度的消息将被视为无效。
使用方法：根据您的需求，设置消息的最大长度限制。
db_path：

作用：持久化存储数据库的路径，用于存储会话数据。
使用方法：根据您的需求，设置持久化存储数据库的路径。
bot_prefix：

作用：洛林AI回复消息时的前缀，用于区分洛林AI的回复。
使用方法：根据您的需求，设置洛林AI回复消息时的前缀。
error_message：

作用：发生错误时作为错误回复的默认错误消息。
使用方法：根据您的需求，设置发生错误时的默认错误消息。
}
```
}
##基于知识库的企业微信应用号配置
{
  "luolinai_api_key": "请输入您的知识库密钥",
  "luolinai_model_id": "请输入您的知识库模型ID",
  "image_create_prefix": [
    "画",
    "看",
    "找"
  ],
  "speech_recognition": false,
  "group_speech_recognition": false,
  "voice_reply_voice": false,
  "conversation_max_tokens": 1000,
  "expires_in_seconds": 3600,
  "channel_type": "wechatcom_app",
  "wechatcom_corp_id": "请输入您的企业ID",
  "wechatcomapp_secret": "请输入您的应用Secret",
  "wechatcomapp_agent_id": "请输入您的应用Agent ID",
  "wechatcomapp_token": "请输入您的应用Token",
  "wechatcomapp_aes_key": "请输入您的应用AES Key",
  "wechatcomapp_port": 9200


**配置说明：**

**1.个人聊天**

+ 个人聊天中，需要以 "bot"或"@bot" 为开头的内容触发机器人，对应配置项 `single_chat_prefix` (如果不需要以前缀触发可以填写  `"single_chat_prefix": [""]`)
+ 机器人回复的内容会以 "[bot] " 作为前缀， 以区分真人，对应的配置项为 `single_chat_reply_prefix` (如果不需要前缀可以填写 `"single_chat_reply_prefix": ""`)

**2.群组聊天**

+ 群组聊天中，群名称需配置在 `group_name_white_list ` 中才能开启群聊自动回复。如果想对所有群聊生效，可以直接填写 `"group_name_white_list": ["ALL_GROUP"]`
+ 默认只要被人 @ 就会触发机器人自动回复；另外群聊天中只要检测到以 "@bot" 开头的内容，同样会自动回复（方便自己触发），这对应配置项 `group_chat_prefix`
+ 可选配置: `group_name_keyword_white_list`配置项支持模糊匹配群名称，`group_chat_keyword`配置项则支持模糊匹配群消息内容，用法与上述两个配置项相同。（Contributed by [evolay](https://github.com/evolay))
+ `group_chat_in_one_session`：使群聊共享一个会话上下文，配置 `["ALL_GROUP"]` 则作用于所有群聊

**3.语音识别**

+ 添加 `"speech_recognition": true` 将开启语音识别，默认使用openai的whisper模型识别为文字，同时以文字回复，该参数仅支持私聊 (注意由于语音消息无法匹配前缀，一旦开启将对所有语音自动回复，支持语音触发画图)；
+ 添加 `"group_speech_recognition": true` 将开启群组语音识别，默认使用openai的whisper模型识别为文字，同时以文字回复，参数仅支持群聊 (会匹配group_chat_prefix和group_chat_keyword, 支持语音触发画图)；
+ 添加 `"voice_reply_voice": true` 将开启语音回复语音（同时作用于私聊和群聊），但是需要配置对应语音合成平台的key，由于itchat协议的限制，只能发送语音mp3文件，若使用wechaty则回复的是微信语音。

**4.其他配置**

+ `model`: 模型名称，目前支持 `gpt-3.5-turbo`, `text-davinci-003`, `gpt-4`, `gpt-4-32k`  (其中gpt-4 api暂未开放)
+ `temperature`,`frequency_penalty`,`presence_penalty`: Chat API接口参数，详情参考[OpenAI官方文档。](https://platform.openai.com/docs/api-reference/chat)
+ `proxy`：由于目前 `openai` 接口国内无法访问，需配置代理客户端的地址，详情参考  [#351](https://github.com/zhayujie/chatgpt-on-wechat/issues/351)
+ 对于图像生成，在满足个人或群组触发条件外，还需要额外的关键词前缀来触发，对应配置 `image_create_prefix `
+ 关于OpenAI对话及图片接口的参数配置（内容自由度、回复字数限制、图片大小等），可以参考 [对话接口](https://beta.openai.com/docs/api-reference/completions) 和 [图像接口](https://beta.openai.com/docs/api-reference/completions)  文档直接在 [代码](https://github.com/zhayujie/chatgpt-on-wechat/blob/master/bot/openai/open_ai_bot.py) `bot/openai/open_ai_bot.py` 中进行调整。
+ `conversation_max_tokens`：表示能够记忆的上下文最大字数（一问一答为一组对话，如果累积的对话字数超出限制，就会优先移除最早的一组对话）
+ `rate_limit_chatgpt`，`rate_limit_dalle`：每分钟最高问答速率、画图速率，超速后排队按序处理。
+ `clear_memory_commands`: 对话内指令，主动清空前文记忆，字符串数组可自定义指令别名。
+ `hot_reload`: 程序退出后，暂存微信扫码状态，默认关闭。
+ `character_desc` 配置中保存着你对机器人说的一段话，他会记住这段话并作为他的设定，你可以为他定制任何人格      (关于会话上下文的更多内容参考该 [issue](https://github.com/zhayujie/chatgpt-on-wechat/issues/43))
+ `subscribe_msg`：订阅消息，公众号和企业微信channel中请填写，当被订阅时会自动回复， 可使用特殊占位符。目前支持的占位符有{trigger_prefix}，在程序中它会自动替换成bot的触发词。


## 运行

### 1.本地运行

如果是开发机 **本地运行**，直接在项目根目录下执行：

```bash
python3 app.py
```
终端输出二维码后，使用微信进行扫码，当输出 "Start auto replying" 时表示自动回复程序已经成功运行了（注意：用于登录的微信需要在支付处已完成实名认证）。扫码登录后你的账号就成为机器人了，可以在微信手机端通过配置的关键词触发自动回复 (任意好友发送消息给你，或是自己发消息给好友)，参考[#142](https://github.com/zhayujie/chatgpt-on-wechat/issues/142)。


### 2.服务器部署

使用nohup命令在后台运行程序：

```bash
touch nohup.out                                   # 首次运行需要新建日志文件  
nohup python3 app.py & tail -f nohup.out          # 在后台运行程序并通过日志输出二维码
```
扫码登录后程序即可运行于服务器后台，此时可通过 `ctrl+c` 关闭日志，不会影响后台程序的运行。使用 `ps -ef | grep app.py | grep -v grep` 命令可查看运行于后台的进程，如果想要重新启动程序可以先 `kill` 掉对应的进程。日志关闭后如果想要再次打开只需输入 `tail -f nohup.out`。此外，`scripts` 目录下有一键运行、关闭程序的脚本供使用。

> **多账号支持：** 将项目复制多份，分别启动程序，用不同账号扫码登录即可实现同时运行。

> **特殊指令：** 用户向机器人发送 **#reset** 即可清空该用户的上下文记忆。



#扫码加我入交流群![weChat](https://github.com/luolin-ai/KnowledgeBot/assets/135555634/b3a9bc1c-7e96-463c-8e35-fa8353ba2131)

#关注公众号了解更多
![571d92f9b01ff97c6a1ee73b604f7bd7](https://github.com/luolin-ai/KnowledgeBot/assets/135555634/75951cf6-280f-40b6-b6de-526a44223858)


