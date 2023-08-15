import scripts.Jellyfin as jf
import scripts.DailyReport as dr
import scripts.System as sys
import scripts.ExpressMsg as em
import re, PyOfficeRobot

pattern_em = r"查询快递：(\w+)"

def FuncLaucher(msg):
    if msg == "启动jellyfin":
        print("调用：启动jellyfin")
        jf.startServer()
    elif msg == "关闭jellyfin":
        print("调用：关闭jellyfin")
        jf.killServer()
    elif msg == "发送早报":
        print("调用：发送早报")
        dr.getDailyReport()
    elif msg == "日期":
        print("调用：发送日期")
        dr.getDate()
    elif msg == "天气":
        print("调用：发送天气")
        dr.getWeather()
    elif msg == "关机":
        print("调用：关机")
        sys.ShutdownComputer()
    elif msg == "重启":
        print("调用：重启")
        sys.RestartComputer()
    elif re.match(pattern_em,msg):
        PyOfficeRobot.chat.send_message("akinaustin", "开发中，目前信息不准确")
        print("调用：快递查询")
        package_number = re.match(pattern_em,msg).group(1)
        print(package_number)
        em.SearchExpressMsg(package_number)



