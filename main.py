from PyOfficeRobot.core.WeChatType import *
import PyOfficeRobot
import scripts.Jellyfin as jf
from functools import partial
from data.keywords import keywords

wx = WeChat()

wx.GetSessionList()
msg = 'Activate bot!'
who = 'akinaustin'
wx.ChatWith(who=who)
wx.SendMsg(msg, who)

temp_msg = ''
while True:
    try:
        friend_name, receive_msg = wx.GetAllMessage[-1][0], wx.GetAllMessage[-1][1]  # 获取朋友的名字、发送的信息
        #静态回复
        if (friend_name == who) & (receive_msg != temp_msg) & (receive_msg in keywords.keys()):
            temp_msg = receive_msg
            wx.SendMsg(keywords[receive_msg], who)  # 向`who`发送消息
        #函数调用
        if (friend_name == who) & (receive_msg == "启动jellyfin"):
            jf.startServer()
        elif (friend_name == who) & (receive_msg == "关闭jellyfin"):
            jf.killServer()
    except:
        pass


