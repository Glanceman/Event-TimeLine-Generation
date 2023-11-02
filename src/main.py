from classes.CrawlerFactory import CrawlerFactory


KEYWORD = "war"


def main():
    #todo retrieve information from social media
    crawler = CrawlerFactory.createSouthMorningCrawler(KEYWORD)
    crawler.crawl()

    # todo integrate data from different sources
    
    # todo process the data (remove overlapped)

    # todo present the data

    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f"package name : { __package__}" )
    main()
