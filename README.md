# 鹊桥桥

基于 [`鹊桥`](https://github.com/17TheWord/QueQiao) 与 `NoneBot2` 同步多个 `Minecraft Server` 消息的插件

## 支持的服务端列表

- Spigot
- Forge
- Fabric
- Folia
- NeoForge
- Velocity
- 原版端

配套 **插件/模组** 请前往 [`鹊桥`](https://github.com/17TheWord/QueQiao) 仓库查看详情

## 安装

> 没过审，将就用 pip 吧

```shell
pip install nonebot-plugin-queqiaoqiao
```

在 `pyproject.toml` 中添加插件依赖

```toml
[tool.nonebot]
# ...
plugins = ["nonebot_plugin_queqiaoqiao"]
# ...
```

## 配置

```dotenv
# 服务器名需与鹊桥端配置一致
sync_mc_groups = [["Server1", "Server2", "Server3"], ["Server4", "Server5"]]
```

## 特别感谢

- [NoneBot2](https://github.com/nonebot/nonebot2)：史上最无敌屌炸天牛逼Class Number One的机器人框架。

## 关于 Minecraft 适配器

- 本插件基于 [`nonebot-adapter-minecraft`](https://github.com/17TheWord/nonebot-adapter-minecraft)
  适配器实现 `Websocket`、`Rcon` 通信
- 若有自定义一些简单插件的想法，可以一试，例如：
  - 非插件端无权限系统场景下实现普通玩家使用`tp`命令
  - 实现简单的自助领取游戏物品
  - 连接直播间，实现弹幕聊天与游戏内聊天互通
  - ...

## 贡献与支持

觉得好用可以给这个项目点个 `Star` 或者去 [爱发电](https://afdian.com/a/17TheWord) 投喂我。

有意见或者建议也欢迎提交 [Issues](https://github.com/17TheWord/nonebot-plugin-queqiaoqiao/issues)
和 [Pull requests](https://github.com/17TheWord/nonebot-plugin-queqiaoqiao/pulls)。

## 许可证

本项目使用 [MIT](./LICENSE) 作为开源许可证。
