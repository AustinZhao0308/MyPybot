from PyOfficeRobot.core.WeChatType import *
import PyOfficeRobot
import time

keywords = {
    "你好": "你好！我是Akinlan Studio Bot。",
    "我要报名": "你好，这是报名链接：www.python-office.com"
}

wx = WeChat()
wx.GetSessionList()
msg = 'test'
who = 'akinaustin'
wx.ChatWith(who=who)
# for i in range(10):
wx.SendMsg(msg, who)
while True:
    PyOfficeRobot.chat.chat_by_keywords(who, keywords=keywords)
    time.sleep(1)

