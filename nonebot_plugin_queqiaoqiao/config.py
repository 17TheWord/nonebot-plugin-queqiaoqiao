from nonebot import get_plugin_config, logger
from nonebot.compat import PYDANTIC_V2
from pydantic import BaseModel, Field, field_validator, validator


class Config(BaseModel):
    sync_mc_server_group: list[list[str]] = Field(
        default_factory=list, description="MC服务器同步群组"
    )
    sync_mc_server_dict: dict[str, list[str]] = Field(
        default_factory=dict, description="MC服务器同步群组字典"
    )
    sync_server_set: set[str] = Field(
        default_factory=set, description="MC服务器同步群组集合"
    )

    # 当 sync_mc_server_group 传入值时，更新dict
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

        cls.sync_mc_server_dict = {}
        for server_group in v:
            logger.info(f"正在处理服务器群组：{server_group}")
            server_set = set(server_group)  # 转换为集合提高效率
            for current_server in server_group:
                sync_targets = list(server_set - {current_server})
                cls.sync_mc_server_dict[current_server] = sync_targets
                logger.debug(
                    f"服务器 '{current_server}' 已配置同步，同步目标：{sync_targets}"
                )
            logger.debug(f"服务器群组 {server_group} 同步配置完成")
        logger.debug("服务器群组同步完毕。")

        cls.sync_server_set = {server for group in v for server in group}

        return v


plugin_config = get_plugin_config(Config)
