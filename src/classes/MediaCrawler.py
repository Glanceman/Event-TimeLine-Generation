from numpy import ndarray
class MediaCrawler:
    def __init__(self,defaultKeyword:str) -> None:
        self.link:str=""
        self.keyword:str=defaultKeyword
        pass
    
    def setKeyword(self,word:str)->None:
        self.keyword=word

    def crawl(self)->ndarray:
        pass





    
