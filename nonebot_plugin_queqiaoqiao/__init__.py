from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="鹊桥桥",
    description="基于鹊桥的同步多个Minecraft服务器消息的插件",
    homepage="https://github.com/17TheWord/nonebot-plugin-queqiaoqiao",
    usage="""
    在 dotenv 中配置以下配置项
    sync_mc_groups = [["Server1", "Server2", "Server3"], ["Server4", "Server5"]]
    """,
    config=Config,
    type="application",
    supported_adapters={"nonebot.adapters.minecraft"},
)

from . import on_mc_msg as on_mc_msg
