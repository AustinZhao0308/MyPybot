import scripts.Jellyfin as jf

def FuncLaucher(msg):
    if msg == "启动jellyfin":
        jf.startServer()
    elif msg == "关闭jellyfin":
        jf.killServer()
