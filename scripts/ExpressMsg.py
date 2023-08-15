import json, re
import requests
import PyOfficeRobot

def SearchExpressMsg(number):
    response = ""
    url = 'http://www.kuaidi100.com/query?type=ems&postid=%s' % number
    rs = requests.get(url)
    rs_dict = json.loads(rs.text)
    msg = rs_dict['message']
    if msg == 'ok':
        response += '您的快递%s物流信息如下：' % number
        response += '{ctrl}{ENTER}'
        data_list = rs_dict['data']
        for kuaidi_dict in data_list:
            time = kuaidi_dict['time']
            context = kuaidi_dict['context']
            response += '%s' % time
            response += '{ctrl}{ENTER}'
            response += '%s' % context
            response += '{ctrl}{ENTER}'
        PyOfficeRobot.chat.send_message("akinaustin", response)
        return response
    else:
        PyOfficeRobot.chat.send_message("akinaustin", msg)
        return msg


if __name__ == "__main__":
    str = "查询快递：JT3041580958255"
    pattern_em = r"查询快递：(\w+)"
    print(re.match(pattern_em, str))
    package_number = re.match(pattern_em, str).group(1)
    print(package_number)
    SearchExpressMsg(package_number)