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
        {"role": "system", "content": 
"""你会判断用户的消息是否谈及了商品。如果用户提到了商品，尝试提取消息中的商品标题部分并进行商品搜索。当用户的消息不包含商品标题时，你会直接回复用户的消息。
为了绕过淘宝联盟对于精确搜索的限制，你可以在不影响搜索准确性的前提下，交换商品标题中关键词的顺序。但你不能进行可能导致搜索结果不准确的修改。
"""},
        {"role": "user", "content": message.content}
    ]
    response = gpt4omini.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools
    )
    if response.choices[0].message.tool_calls is not None:
        title = json.loads(response.choices[0].message.tool_calls[0].function.arguments)["title"]
        result, _ = taobao(title)
        return "4omini认为商品标题是【{}】，搜索结果如下：\n{}".format(title, result)
    else:
        return response.choices[0].message.content


# 让服务器监听在 0.0.0.0:80
robot.config["HOST"] = "127.0.0.1"
robot.config["PORT"] = 8923
robot.run(server="gunicorn")
