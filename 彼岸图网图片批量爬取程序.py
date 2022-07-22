#爬取动漫部分多页壁纸的下载

#分析翻页的网址
#https://pic.netbian.com/4kdongman/index.html
#https://pic.netbian.com/4kdongman/index_2.html
#https://pic.netbian.com/4kdongman/index_3.html
#https://pic.netbian.com/4kdongman/index_4.html
#可得翻页网址遵循规律（除第一页外）：https://pic.netbian.com/4kdongman/index_{i}.html
import os
import time
import requests
from lxml import etree
#彼岸图网首页网址
url_first="https://pic.netbian.com"
headers_={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}
#1.获取到实时标题栏,并且保存入字典dict_title,以便输入的标题查找到对应的标题
response=requests.get(url_first,headers=headers_)
str_data=response.content.decode(encoding="gbk")
html_obj=etree.HTML(str_data)
title_4k_all=html_obj.xpath("//div[@class='classify clearfix']/a[@href]/@title")
title_4k_all_url_b=html_obj.xpath("//div[@class='classify clearfix']/a/@href")
dict_title={}
print("以下是可以批量爬取壁纸的标题栏")
for i in range(3):
    print("     |     ")
for i in range(len(title_4k_all)):
    dict_title[title_4k_all[i]]=title_4k_all_url_b[i]
    print(title_4k_all[i])
for i in range(3):
    print("     |     ")
#批量创建标题栏文件夹
try:
    path=r"D:"
    path=path+"\\"+"彼岸图网"
    for i in dict_title:
        os.makedirs(path+"\\"+i)
except:
    pass

while True:
    #某个标题栏的输入
    title_4k=input("请在上述标题中选一个复制粘贴作为输入-------（建议选择：4K美女图片）：")
    #想要爬取的页数
    page=int(input(f"请输入想要爬取{title_4k}部分的壁纸的页数:"))
    if title_4k in dict_title:
        url1=url_first+dict_title[title_4k]
        # url_jpg_b=html_obj.xpath("//div/ul/li/a/img/@src")
        #爬取想要的页数
        for i in range(1,page+1):
            if i==1:
                url=url1+"index.html"
            else:
                url=url1+f"index_{i}.html"
            response = requests.get(url, headers=headers_)
            str_data = response.content.decode("gbk")
            html_obj = etree.HTML(str_data)
            url_jpg_b=html_obj.xpath("//div/ul/li/a/img/@src")
            # print(url_jpg_b)
            name=html_obj.xpath("//div/ul/li/a/b/text()")
            print(f"第{i}页下载中")
            for j in range(len(url_jpg_b)):
                url_jpg_b_pic=url_first+url_jpg_b[j]
                response=requests.get(url_jpg_b_pic,headers=headers_)
                bytes_data=response.content
                print("-----正在下载中-----")
                with open(f"D:\彼岸图网\{title_4k}\{name[j]}.jpg","wb") as f:
                    f.write(bytes_data)

        print(f"-----您已经成功爬取-----(可以在此电脑的D盘文件夹>彼岸图网>{title_4k}文件夹中打开哦！！！里面绝对有惊喜！！！)")
        print("这里建议亲亲们一定要打开文件夹看看，如果不喜欢可以在上述文件夹页面ctrl+A，右键删除，同时清空回收站，不会对电脑有任何影响哦！！！")
        time.sleep(3)
        print("")
        print("请问您是否还要继续爬取壁纸图片？")
        time.sleep(0.3)
        #判断是否继续
        core=input("是-------------------请输入数字1  （输入完毕后按回车）\n"
                   "否-------------------请输入数字2  （输入完毕后按回车）\n")
        time.sleep(0.3)
        # exit1    =input("否-------------------请输入数字2  （输入完毕后按回车）")
        if core=="1":
            continue
        elif core=="2":
            print("")
            print("您选择退出，界面即将在3秒后退出-----（也可以按右上角x键自行退出哦）")
            time.sleep(3)
            break
        else:
            print("")
            print("您选择是否继续爬取输入有误，我们即将在3秒后退出")
            time.sleep(3)
            break
    else:
        print("您想要爬取的标题栏输入错误，请重新输入")                #需要一个大循环，以重新输入


