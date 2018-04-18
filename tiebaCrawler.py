
import urllib.request
headers={"User-Agent":"Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11"}

def main():
    url="http://tieba.baidu.com/f"
    # headers={"User-Agent":"Mozilla.."}
    # kw=input("请输入要搜索的关键字：")
    kw="阿森纳"
    beginPage=int(input("请输入起始页："))
    endPage=int(input("请输入终止页："))
    url=url+"?"+urllib.parse.urlencode({"kw":kw})
    tiebaSpider(url,beginPage,endPage)

def loadPage(url,filename):
    print("正在下载"+filename)
    request=urllib.request.Request(url,headers=headers)
    response=urllib.request.urlopen(request).read().decode("utf-8",'ignore')
    return response

def writePage(html,filename):
    '''
    作用：将html内容写入到本地
    html:服务器相应文件内容
    '''
    print("正在保存"+filename)
    with open(filename,'w',encoding='utf-8') as f:
        f.write(html)

def tiebaSpider(url,beginPage,endPage):
    '''
    作用：贴吧爬虫调度器，负责组合处理每个页面的url
    '''
    for page in range(beginPage,endPage+1):
        pn=(page-1)*50
        fullurl=url+"&pn="+str(pn)
        filename="No."+str(page)+"Page.html"
        html=loadPage(fullurl,filename)
        print(html)
        writePage(html,filename)

if __name__ == "__main__":
    main()

