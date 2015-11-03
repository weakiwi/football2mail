#coding=utf-8
from bs4 import BeautifulSoup
import codecs
import urllib
import urllib2
import time
#import duanxin

def get_zhanbao(mytime):
#    date = '20151101'
    date = mytime
    goal_url = 'http://goal.sports.163.com/schedule/' + date + '.html'#构成网址
    response = urllib2.urlopen(goal_url)
    page = response.read()
    soup = BeautifulSoup(page)#构造bs
    tag = soup.find_all(class_='bg2 bg7')#查找对应标签
    zhanbao = []
    mail_content = ''
    for i in tag:
        if i.get_text().encode('utf-8')[7:13] == '战报':#判断关键字段为‘统计’还是‘战报’
            zhanbao.append('http://goal.sports.163.com'+i.find('a').get('href'))#存储所有‘战报’的超链接
#    print zhanbao
    for i in zhanbao:
        response = urllib2.urlopen(i)
        page = response.read()
        soup = BeautifulSoup(page)
        tag = soup.find_all('b')
        if tag == '':
            break
        for i in tag:
            mail_content += i.get_text().encode('utf-8')+'|'#构造邮件内容
            print i
#    print mail_content
    return mail_content
def get_bifeng(mytime):
#    date = '20151101'
    date = mytime
    goal_url = 'http://goal.sports.163.com/schedule/' + date + '.html'#构成网址
    response = urllib2.urlopen(goal_url)
    page = response.read()
    soup = BeautifulSoup(page)#构造bs
    tag_zhudui = soup.find_all('span', 'c1')
    tag_kedui = soup.find_all('span', 'c2')
    tag_bifeng = soup.find_all('span', 'c3')
    temp_bifeng = []
    bifeng = ' '
    print tag_bifeng
    for (i, j) in zip(tag_zhudui, tag_bifeng):
        temp_bifeng.append(i.get_text().encode('utf-8') + ' ' + j.get_text().encode('utf-8') + ' ')
    for (i, j) in zip(tag_kedui, temp_bifeng):
        bifeng += (j + ' ' + i.get_text().encode('utf-8')+'\n')
    return bifeng
if __name__ == '__main__':
    mytime = time.strftime("%Y%m%d", time.localtime())
    mail_content = get_zhanbao(mytime)
    if mail_content != '' and mail_content:#若当天无战报则不发送
        duanxin.main(mail_content,'你的邮箱')
        duanxin.main(mail_content,'你的邮箱')
    else:
        mail_content = get_bifeng(mytime)#无战报则发送比分
        duanxin.main(mail_content,'你的邮箱')
        duanxin.main(mail_content,'你的邮箱')        
