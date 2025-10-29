import werobot
from taobao_util import taobao

robot = werobot.WeRoBot(token="syh1en")


@robot.handler
def handle_message(message, session):
    """
    处理用户消息，直接进行淘宝商品搜索
    移除了Gemini/LLM依赖，采用简化逻辑
    """
    user_input = message.content.strip()

    # 检查输入是否为空
    if not user_input:
        return "请输入商品关键词，例如：Nike运动鞋、iPhone 15"

    try:
        # 调用新的taobao函数，返回3个值
        results, msg, links = taobao(user_input)

        # 检查是否找到商品
        if isinstance(results, list) and len(results) > 0:
            # 成功找到商品，返回格式化消息
            return msg
        else:
            # 没有找到商品或发生错误
            return results if isinstance(results, str) else "未找到相关商品，请尝试其他关键词"

    except Exception as e:
        # 捕获异常并返回友好错误消息
        print(f"搜索错误: {e}")
        return "抱歉，搜索过程中发生错误，请稍后重试"


# 配置服务器
robot.config["HOST"] = "127.0.0.1"
robot.config["PORT"] = 8923

if __name__ == "__main__":
    print("=" * 60)
    print("微信机器人启动中...")
    print("=" * 60)
    print(f"监听地址: {robot.config['HOST']}:{robot.config['PORT']}")
    print("=" * 60)
    robot.run()
