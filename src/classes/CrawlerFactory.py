from classes.SouthMorningCrawler import SouthMorningCrawler
from classes.CnnCrawler import CnnCrawler
from classes.AbcCrawler import AbcCrawler
class CrawlerFactory:

    @staticmethod
    def createSouthMorningCrawler(keyword:str) ->SouthMorningCrawler:
        crawler = SouthMorningCrawler(keyword)
        return crawler
    @staticmethod
    def createCnnCraler(keword:str) ->CnnCrawler:
        crawler=CnnCrawler(keword)
        return crawler
    @staticmethod
    def createAbcCrawler(keyword:str) ->AbcCrawler:
        crawler = AbcCrawler(keyword)
        return crawler