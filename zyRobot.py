
#-*- coding:utf-8 -*-

from qqbot import QQBotSlot as qqbotslot, RunBot


@qqbotslot
def onQQMessage(bot, contact, member, content):
    if content == '-hello':
        bot.SendTo(contact, '')
    if content == '陈':
        pass
    # elif content == '-stop':
    #     bot.SendTo(contact, 'QQ机器人已关闭')
    #     bot.Stop()



if '__main__' == __name__:
    RunBot()
