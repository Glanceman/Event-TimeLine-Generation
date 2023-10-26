from classes.MediaCrawler import MediaCrawler
import requests as r
from bs4 import BeautifulSoup as bs

class RedditCrawler(MediaCrawler):
    
    def __init__(self, keyword: str) -> None:
        super().__init__(keyword)
        self.link="https://www.reddit.com/search/?q="

    def crawl(self) -> None:
        super().crawl()
        resp = r.get(self.link+self.keyword)
        soup = bs(resp.text, "html.parser")
        links = soup.find_all('a',attrs={"data-testid": "post-title"})
        print(len(links))
        for link in links:
            print(link['href'])

