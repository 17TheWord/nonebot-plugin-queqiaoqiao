from nonebot import get_plugin_config, logger
from nonebot.compat import PYDANTIC_V2
from pydantic import BaseModel, Field, field_validator, validator

from .common import sync_mc_server_dict, sync_server_set


def _get_sync_mc_server_dict(sync_mc_server_group):
    result = {}
    for server_group in sync_mc_server_group:
        logger.info(f"正在处理服务器群组：{server_group}")
        server_set = set(server_group)
        for current_server in server_group:
            sync_targets = list(server_set - {current_server})
            result[current_server] = sync_targets
            logger.debug(
                f"服务器 '{current_server}' 已配置同步，同步目标：{sync_targets}"
            )
        logger.debug(f"服务器群组 {server_group} 同步配置完成")
    logger.debug("服务器群组同步完毕。")
    return result


def _get_sync_server_set(sync_mc_server_group):
    return {server for group in sync_mc_server_group for server in group}


class Config(BaseModel):
    sync_mc_server_group: list[list[str]] = Field(
        default_factory=list, description="MC服务器同步群组"
    )

    @(
            field_validator("sync_mc_server_group", mode="before")
            if PYDANTIC_V2
            else validator("sync_mc_server_group", pre=True, always=True)
    )
    @classmethod
    def update_sync_mc_server_dict(cls, v):
        if not isinstance(v, list) or not all(isinstance(i, list) for i in v):
            logger.warning("sync_mc_server_group 配置格式错误，请检查。")
            return []

        sync_mc_server_dict.clear()
        sync_mc_server_dict.update(_get_sync_mc_server_dict(v))

        sync_server_set.clear()
        sync_server_set.update(_get_sync_server_set(v))

        return v


plugin_config = get_plugin_config(Config)
