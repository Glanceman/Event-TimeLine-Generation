from classes.CrawlerFactory import CrawlerFactory
import numpy as np
import pandas as pd

KEYWORDS = ["israel"]
UPDATE_DATA = True

def mining():
    
    if(UPDATE_DATA):
        #retrieve information from social media
        #add different crawlers
        crawlers=[]
        crawlers.append(CrawlerFactory.createSouthMorningCrawler(KEYWORDS[0]))
        crawlers.append(CrawlerFactory.createCnnCraler("israel gaza"))
        crawlers.append(CrawlerFactory.createAbcCrawler(KEYWORDS[0]))
        # data mining with each keyword
        finalResult = np.array([])
        for keyword in KEYWORDS:
            for crawler in crawlers: # loop each crawler
                crawler.setKeyword(keyword)
                crawlerResult = crawler.crawl()
                if finalResult.size==0 :
                    finalResult=crawlerResult
                else:
                    finalResult = np.vstack((finalResult,crawlerResult))

        #convert to dataframe and save to csv
        df = pd.DataFrame(finalResult)
        df.to_csv('data.csv', index=False, header=['link','title','author','date','content'],encoding='utf-8',sep='|')

    df = pd.read_csv('data.csv',sep='|')

    # Display the DataFrame
    #print(df)


    # todo integrate data from different sources
    


    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__mining__':
    print(f"package name : { __package__}" )
    mining()
