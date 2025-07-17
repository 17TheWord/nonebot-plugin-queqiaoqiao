from nonebot import get_bot, logger, on_message
from nonebot.adapters.minecraft import Bot, MessageEvent, MessageSegment
from nonebot.adapters.minecraft.model import TextColor

from .config import plugin_config


def sync_mc_server_group(event: MessageEvent):
    return event.server_name in plugin_config.sync_server_set


sync_mc_server = on_message(priority=5, rule=sync_mc_server_group)


@sync_mc_server.handle()
async def handle_server_message(event: MessageEvent):
    if not (
        sync_server_list := plugin_config.sync_mc_server_dict.get(event.server_name)
    ):
        logger.debug("同步群组为空")
        return
    # 先转换消息
    message = MessageSegment.text(f"[{event.server_name}] ", TextColor.LIGHT_PURPLE)
    message += MessageSegment.text(event.player.nickname + " ", TextColor.GREEN)
    for msg in event.get_message():
        message += MessageSegment.text(msg.data["text"])

    # 通过 get_bot 获取映射表内的其他Bot
    for server_name in sync_server_list:
        try:
            bot: Bot = get_bot(server_name)  # type: ignore
        except KeyError:
            logger.debug(f"未找到映射表内的Bot: {server_name}，将忽略同步")
            continue
        await bot.send_msg(message=message)
