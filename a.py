# -*- coding:utf-8 -*-

import urllib,re

#获取不同的网址
def get_url(page):
    return 'http://www.budejie.com/video/'+str(page)

# 获取源代码
def get_html(url):
    return urllib.urlopen(url).read()

#下载
def download(mp4_url,path):
    # print path
    path = "".join(path.split())

    urllib.urlretrieve(mp4_url,'%s.mp4'%(path.decode('utf-8').encode('gbk')))
    print 'ok!!'

# 匹配视频地址
def get_mpl_url(request):
    reg = r'data-mp4="(.*?)"'
    return re.findall(reg,request)

# 匹配视频的名称
def get_name (request):    
    reg = re.compile(r'<div class="j-r-list-c-desc">(.*?)</div>',re.S)
    return re.findall(reg,request)

#调用
html = get_html(get_url(1))
mp4_url = get_mpl_url(html)
mp4_name = get_name(html)


try:
    for x,y in zip(mp4_url,mp4_name):
        if '|' in y:
            continue
        download(x,y)
except IOError,e:
    print e