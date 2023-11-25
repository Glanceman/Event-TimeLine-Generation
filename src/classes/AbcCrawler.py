import requests as r
from bs4 import BeautifulSoup
from datetime import datetime
from operator import itemgetter
from classes.MediaCrawler import MediaCrawler
import numpy as np

class AbcCrawler(MediaCrawler):

    def __init__(self, defaultKeyword: str) -> None:
        super().__init__(defaultKeyword)

    def crawl(self) -> np.ndarray:
        text=[]
        times=set()
        for i in range(43):
            # 定义文档的URL
            url= "https://abcnews.go.com/meta/api/search?limit=10&sort=&type=WireStory&section=&totalrecords=true&offset="+str(i*10+10)+"&after=2023-10-07&q=Israeli%20Palestinian"

            # 发送HTTP请求并获取文档内容
            response = r.get(url)
            json_content = response.json()

            # 提取item数组中的每个对象
            items = json_content['item']
            urls=[]
            # 遍历每个对象并提取link字段
            for item in items:
                link = item['link']
                urls.append(link)

            for url in urls:
                dic={}
                res = r.get(url)
                html = res.text
                bf = BeautifulSoup(html)


                time=bf.find(class_="xAPp Zdbe jTKb pCRh")
                time=time.text
                datetime_trans = datetime.strptime(time, "%B %d, %Y, %I:%M %p")
                formatted_date = datetime_trans.strftime("%Y-%m-%dT%H:%M:%S.000Z")

                if(formatted_date not in times):
                    dic["link"]=url
                    #get all the <p>tag and output the text of them
                    title=bf.find(class_='vMjA gjbz eHrJ mTgU')
                    if type(title) == type(None):
                        title=bf.find(class_="vMjA eeTZ eHrJ")
                    if type(title) == type(None):
                        continue
                    title=title.text
                    title=title.replace("Live updates |  "," ")
                    title=title.replace("Live updates | "," ")
                    dic["title"]=title
                    description=bf.find(class_='jxTE Poys lqtk HkWF HfYh kGyA' )
                    if type(description) == type(None):
                        description=bf.find(class_='ncwc Qmvg nyTI VbLm ystq kqbG akor ARhV ygKV yHyq tsIf WHLR lKuK CVfp xijV soGR XgdC aWMf')
                    if type(description) == type(None):
                        continue
                    author=bf.find(class_='TQPv HUca ucZk WxHI HhZO yaUf VOJB XSba Umfi ukdD')
                    author=author.text
                    dic["author"]=author.replace("By"," ")
                    dic["date"]=formatted_date
                    dic["content"]=description.text


                    text.append(dic)
                    times.add(formatted_date)
            sorted_list = sorted(text, key=itemgetter("date"))
            result = np.array([])
            for row in sorted_list:
                tmp=[]
                tmp.append(row["link"])
                tmp.append(row["title"])
                tmp.append(row["author"])
                tmp.append(row["date"])
                tmp.append(row["content"])
                if result.size==0 :
                    result=np.hstack((result,np.array(tmp)))
                else:
                    result = np.vstack((result,tmp))

        return result