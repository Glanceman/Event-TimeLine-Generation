from classes.SouthMorningCrawler import SouthMorningCrawler

class CrawlerFactory:

    @staticmethod
    def createSouthMorningCrawler(keyword:str) ->SouthMorningCrawler:
        crawler = SouthMorningCrawler(keyword)
        return crawler