# -*- coding: utf-8 -*-
# python 3.5.2
# 测试系统，Win10
# Author:Van
# 实现SS5本机自动更新密码，争取24小时保持连接
# 实际做不到24小时，因为iss网站的密码的变更有一定时间的延迟
# 所以最好能有其他的SS源头网站
# V1.0
# 欢迎各种改进意见
# 请把对应的帐号密码修改成自己的
# 请把SS软件的路径改成自己的


import requests, json, time
from lxml import etree
import smtplib
from email.mime.text import MIMEText
from email.header import Header

TIME_GAP = 300
CONFIG_DIR = 'E:\\迅雷下载\\ShadowsocksR-win-3.7.4.1\\gui-config.json'

oldPwdList = []

def modify_json(pwd):
    with open(CONFIG_DIR,'r') as f:
        data = json.loads(f.read())
        for index, rawPwd in enumerate(pwd):
            data['configs'][index]['password'] = rawPwd.split(':')[-1]
    data = json.dumps(data)
    print(data)
    with open(CONFIG_DIR,'w') as f:
        f.write(data)

def check_update():
    url = 'http://www.ishadowsocks.org'
    html = requests.get(url).content.decode('utf-8', 'replace')
    pwd = etree.HTML(html).xpath('//*[@id="free"]/div/div[2]//h4[3]/text()')
    print('实时密码是：', pwd)

    if not pwd or oldPwdList == pwd:
        return pwd, False
    else:
        return pwd, True

def send_email(htm):
    # send email to notice new WestWorld is coming
    sender = 'fanqikai@163.com'
    receiver = '409085788@qq.com,fanqikai@163.com'
    subject = 'SS5密码有更新！'
    smtpserver = 'smtp.163.com'
    username = 'fanqikai@163.com'
    password = 'fanka111'
    msg = MIMEText(htm, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'UTF-8')
    msg['From'] = sender
    msg['To'] = ','.join(receiver)
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    pwd, update = check_update()
    while 1:
        if update:
            print('password changed, will update!')
            modify_json(pwd)
            oldPwdList = pwd
            print('新的临时密码是：', oldPwdList)
            try:
                send_email(str(pwd))
            except Exception as e:
                print("email failed:", e)
        pwd, update = check_update()
        time.sleep(TIME_GAP)
