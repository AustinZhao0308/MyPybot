import scripts.Jellyfin as jf
import scripts.DailyReport as dr
import scripts.System as sys

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
    elif msg == "关机":
        sys.ShutdownComputer()
    elif msg == "重启":
        sys.RestartComputer()


