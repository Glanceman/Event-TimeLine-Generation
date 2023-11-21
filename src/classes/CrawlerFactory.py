from classes.SouthMorningCrawler import SouthMorningCrawler
from classes.CnnCrawler import CnnCrawler
class CrawlerFactory:

    @staticmethod
    def createSouthMorningCrawler(keyword:str) ->SouthMorningCrawler:
        crawler = SouthMorningCrawler(keyword)
        return crawler
    @staticmethod
    def createCnnCraler(keword:str) ->CnnCrawler:
        crawler=CnnCrawler(keword)
        return crawler