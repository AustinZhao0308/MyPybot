import scripts.Jellyfin as jf
import scripts.DailyReport as dr

def FuncLaucher(msg):
    if msg == "启动jellyfin":
        jf.startServer()
    elif msg == "关闭jellyfin":
        jf.killServer()
    elif msg == "发送早报":
        dr.getDailyReport()
    elif msg == "日期":
        dr.DateMsg()
    elif msg == "天气":
        dr.WeatherMsg()

