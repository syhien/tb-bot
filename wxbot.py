import werobot
from taobao_util import taobao
from openai import OpenAI
import json
import os

robot = werobot.WeRoBot(token="syh1en")
gpt4omini = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("OPENAI_API_KEY")
)
tools = [
    {
    "type": "function",
    "function": {
        "name": "taobao_search",
        "description": "提取所提供的消息中的商品标题部分进行商品搜索",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "商品标题"
                }
            }
        }
    }
}]

@robot.handler
def taobao_search(message):
    messages = [
        {"role": "system", "content": "你是一个商品搜索助手。当你接收到用户的消息时，你会提取消息中的商品标题部分进行商品搜索。当用户的消息不包含商品标题时，你会进行通用问答。"},
        {"role": "user", "content": message.content}
    ]
    response = gpt4omini.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools
    )
    if len(response.choices[0].message.tool_calls) > 0:
        title = json.loads(response.choices[0].message.tool_calls[0].function.arguments)["title"]
        msg, _ = taobao.search(title)
        return msg
    else:
        return response.choices[0].message.content


# 让服务器监听在 0.0.0.0:80
robot.config["HOST"] = "127.0.0.1"
robot.config["PORT"] = 8923
robot.run(server="gunicorn")
