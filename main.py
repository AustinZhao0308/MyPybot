from PyOfficeRobot.core.WeChatType import *
import PyOfficeRobot, datetime
import scripts.Jellyfin as jf
import scripts.DailyReport as dr
from scripts.FuncLaucher import FuncLaucher
from functools import partial
from data.keywords import keywords

wx = WeChat()

wx.GetSessionList()
msg = 'Activate bot!'
who = 'akinaustin'
wx.ChatWith(who=who)
wx.SendMsg(msg, who)

def getmsg():
    friend_name, receive_msg = wx.GetAllMessage[-1][0], wx.GetAllMessage[-1][1]
    while receive_msg == temp_msg:
        pass
    return receive_msg


temp_msg = ''
while True:
    try:
        friend_name, receive_msg = wx.GetAllMessage[-1][0], wx.GetAllMessage[-1][1]  # 获取朋友的名字、发送的信息
        if (friend_name == who) & (receive_msg != temp_msg) & (receive_msg in keywords.keys()):
            temp_msg = receive_msg
            wx.SendMsg(keywords[receive_msg], who)  # 向`who`发送消息
        elif (friend_name == who) & (receive_msg != temp_msg) & (receive_msg not in keywords.keys()):
            temp_msg = receive_msg
            FuncLaucher(receive_msg)

        #每日早报
        current_time = datetime.now().time()
        eight_am = time(8, 0, 0)
        if current_time == eight_am:
            dr.getDailyReport()

        #每日晚报

    except:
        pass


