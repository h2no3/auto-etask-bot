# coding: utf-8
from datetime import datetime
from random import randint

from smart_qq_bot.messages import GroupMsg, PrivateMsg
from smart_qq_bot.signals import on_all_message, on_bot_inited, on_group_message
from smart_qq_bot.logger import logger

last_repeat_time = datetime.now()

@on_bot_inited("PluginManager")
def manager_init(bot):
    logger.info("etask-off is available now:)")


@on_group_message(name="etask-off", accept_self=False)
def etask_off(msg, bot):
    """
    :type bot: smart_qq_bot.bot.QQBot
    :type msg: smart_qq_bot.messages.GroupMsg
    """

    global last_repeat_time

    if msg.from_uin == 134296129:  # english chatting group 3598712579:
        if (datetime.now() - last_repeat_time).seconds < 5:#6 * 60 * 60:
            return
        last_repeat_time = datetime.now()
        repeat_content = msg.content
        bot.send_group_msg(repeat_content, msg.from_uin, randint(1, 10000))
