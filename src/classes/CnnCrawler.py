from numpy import ndarray
import numpy as np
import requests;
from classes.MediaCrawler import MediaCrawler

class CnnCrawler(MediaCrawler):

    def __init__(self, defaultKeyword: str) -> None:
        super().__init__(defaultKeyword)

    def crawl(self) -> ndarray:
        filename = "data_cnn.csv"
        url=('https://search.prod.di.api.cnn.io/content?')
        header={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        result = np.array([])
        for i in range(1, 268):
            param={
                'q': 'israel gaza',
                'size' : '10',
                'from': f'{(i-1)*10}',
                'page': f'{i}',
                'sort': 'newest'
            }
            res=requests.get(url,params=param,headers=header)
            data = res.json()
            tmp=[]
            for j in range(0,10):
                row = data["result"][j]
                if 'VideoObject' in row['type']:
                    continue  
                author='cnn'
                tmp.append(np.array(row['path']))
                tmp.append(np.array(row['headline']))
                tmp.append(np.array(author))
                tmp.append(np.array(row['lastModifiedDate']))
                tmp.append(np.array(row['body']))
                if result.size==0 :
                    result=np.hstack((result,np.array(tmp)))
                else:
                    result = np.vstack((result,tmp))
        return result