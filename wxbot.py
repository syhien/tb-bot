import werobot
from taobao_util import taobao

robot = werobot.WeRoBot(token="syh1en")


@robot.handler
def taobao_search(message):
    msg, _ = taobao(message.content)
    return msg


# 让服务器监听在 0.0.0.0:80
robot.config["HOST"] = "127.0.0.1"
robot.config["PORT"] = 8923
robot.run(server="gunicorn")
