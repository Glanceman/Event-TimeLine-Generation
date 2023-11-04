import time
from classes.MediaCrawler import MediaCrawler
import requests as r
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import numpy as np


class SouthMorningCrawler(MediaCrawler):

    def __init__(self, defaultKeyword: str) -> None:
        super().__init__(defaultKeyword)
        self.link = "https://www.scmp.com/search/"
        self.scrollCount = 10

    def crawl(self) -> np.ndarray:
        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        # options.add_argument('--headless')
        #options.add_experimental_option("detach", True)
        driver= webdriver.Edge(options=options)
        driver.get(self.link+self.keyword)
        time.sleep(1.5) # wait for the page is loaded
        
        print("scroll")
        SCROLL_PAUSE_TIME = 1
        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        currentScrollCount = 0
        while currentScrollCount<self.scrollCount:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            currentScrollCount+=1

        soup = bs(driver.page_source)
        divTags=soup.find_all("div", attrs={"data-qa":'ContentItemSearch-Container'})
        articleLinks:list =[]
        
        for divTag in divTags:
            aTag = divTag.find("a" ,href=True)
            articleLinks.append('https://www.scmp.com'+aTag['href'])
        print(articleLinks[:3])


        r.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
        s = r.session()
        s.keep_alive = False # 关闭多余连接
        result = np.array([])
        for link in articleLinks:
            tmp=[]
            try:
                resp= s.get(link)
                soup = bs(resp.text,"html.parser")
                #date, title, author, content
                title = soup.find("h2",attrs={"data-qa":"ContentHeadline-Container"}).text
                author = soup.find("div",attrs={"data-qa":"AuthorNames-AuthorNamesContainer"}).find('a').text
                date = soup.find("time",attrs={"data-qa":"ArticleDate-time"})['datetime']
                content =soup.find("section",attrs={"data-qa":"ContentBody-ContentBodyContainer"}).text

                tmp.append(link)
                tmp.append(title)
                tmp.append(author)
                tmp.append(date)
                tmp.append(content)
                if result.size==0 :
                    result=np.hstack((result,np.array(tmp)))
                else:
                    result = np.vstack((result,tmp))
            except:
                print(f"Fail to get {link}")
        
        print(result.shape)
        return result
        # extract info
        