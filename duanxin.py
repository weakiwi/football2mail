#encoding=utf-8

__author__ = 'ds'#作者自然不是我啦

#文件名称冲突
from email.mime.text import MIMEText
import smtplib

def main(content,mail_add):
    msg = MIMEText(_text=content, _charset='utf-8')
    #输入Email地址和口令:
    from_addr = '你的邮箱'
    password = '你的密码'
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.qq.com'
    # 输入收件人地址:
    to_addr = mail_add

    #SMTP协议默认端口是25
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    #server.starttls()
    #server.connect(host=smtp_server, port=25)
    #server.esmtp_features["auth"]="AUTH_LOGIN"
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

#if __name__ == '__main__':
 #   main('hahaha')
