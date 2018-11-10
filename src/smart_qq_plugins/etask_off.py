# coding: utf-8
from datetime import datetime
from random import randint

from smart_qq_bot.logger import logger
from smart_qq_bot.signals import on_bot_inited, on_group_message

from smart_qq_plugins.record_gen import genRecord

last_repeat_time = datetime.now()


@on_bot_inited("PluginManager")
def manager_init(bot):
    logger.info("etask_off is available now:)")


@on_group_message(name="etask_off", accept_self=False)
def etask_off(msg, bot):
    """
    :type bot: smart_qq_bot.bot.QQBot
    :type msg: smart_qq_bot.messages.GroupMsg
    """

    global last_repeat_time
    if msg.from_uin == 134296129:  # english chatting group 3598712579:
        if (datetime.now() - last_repeat_time).seconds < 5:  # 6 * 60 * 60:
            return
        last_repeat_time = datetime.now()
        repeat_content = msg.content
        # 1. repeat last message
        bot.send_group_msg(repeat_content, msg.from_uin, randint(1, 10000))
        # 2. snapshot generating
        # 3. record generating
        genRecord(msg.content)
        # 4. send to team leader at the given time
