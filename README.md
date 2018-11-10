# daily redundant etask-off bot
英语老师太太太烦了。。。。
自动化每日英语任务已开坑,stay tuned

# features
+ 扫码登录qq √
+ 自动英语造句 √
+ 自动生成造句截图
+ 自动生成录音文件 √

# dev
基于smartqq，添加插件实现上述功能，插件源码参见:`src/smart_qq_plugins/`
+ `etask_off.py` 功能实现
+ `record_gen.py` 录音生成，使用百度语音API
+ `conf.json` [todo] 添加配置信息，可以将这些生成文件发送给组长，如果进一步还可以直接给学习委员
+ `bubble.html` [todo]造句截图

# ref
>一些决策根源于对强迫人按某种特定方式行事的做法极度厌恶。历史上一些最坏的灾难就起因于理想主义者们试图强迫人们“做某些对他们最好的事情”。这种理想主义不仅导致了对无辜者的伤害，也迷惑和腐化了施展权利的理想主义者自身。对于与之相左的意见提议，理想主义者往往有忽略它们的倾向。

# license
see [LICENSE](/LICENSE) for all the details