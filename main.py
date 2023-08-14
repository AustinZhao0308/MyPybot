from PyOfficeRobot.core.WeChatType import *
from data.keywords import keywords
import PyOfficeRobot

wx = WeChat()
#wx.GetSessionList()
msg = 'Activate bot!'
who = 'akinaustin'
wx.ChatWith(who=who)
# for i in range(10):
wx.SendMsg(msg, who)
PyOfficeRobot.chat.chat_by_keywords(who, keywords=keywords)

