import requests
import itchat
import random


def get_request(_info):
    #发送给服务器数据
    apiUrl = 'http://www.tuling123.com/openapi/api'

    data = {
        #图灵api调用
        'key': 'e0090cedd0344149a3a3a30ca78fddab',
        'info': _info,
        'userid': 'wechat-robot',


    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return


@itchat.msg_register(itchat.content.TEXT)
def tyling_robat(msg):
    defalultReply = 'I recrvied:' + msg['Text']
    robots = ['kebe', 'jay','lyf']
    reply = get_request(msg['Text'] + random.choice(robots))
    return reply or defalultReply

# 网页登录扫码
itchat.auto_login(enableCmdQR=2)
itchat.run()
