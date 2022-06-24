## A small tool to generate timeline for podcasts

### Dependencies and Env
- Tested on `python=3.8`
- You need to install `ffmpeg` for this to work
### Sample Usage
Simply replace the `PATH` and `glob` for your need and run the script directly

Example
```
╰─❯ python3 get_duration.py

***********生成时间轴***********
powered by ffprobe & python :)
********************************

0:00:00  --  敦刻尔克 第01集 解读电影《敦刻尔克》
0:11:41  --  敦刻尔克 第02集 山雨欲来 德军战前准备
0:23:06  --  敦刻尔克 第03集 风雨飘摇 英法不战先屈
0:41:12  --  敦刻尔克 第04集 烽烟骤起 纳粹摧枯拉朽
0:53:14  --  敦刻尔克 第05集 绝处逢生 进攻神秘停止
1:08:45  --  敦刻尔克 第06集 逃出生天 联军艰难撤退
1:23:14  --  敦刻尔克 第07集 鹰击长空 英德空军争霸
```