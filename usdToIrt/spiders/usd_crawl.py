from asyncio.windows_events import NULL
import scrapy
from ..items import UsdtoirtItem
import re
import json
from datetime import datetime


class UsdCrawlSpider(scrapy.Spider):

    name = 'usd_crawl'

    start_urls = ['https://api.accessban.com/v1/market/indicator/summary-table-data/price_dollar_rl?']

    def parse(self, response):

        jsonresponse = json.loads(response.text)

        all_data = jsonresponse["data"]

        # creating items dictionary
        items = UsdtoirtItem() 
        items['openValue'] = []
        items['minValue'] = [] 
        items['maxValue'] = [] 
        items['closeValue'] = [] 
        items['changeAmount'] = []
        items['changePercent'] = []
        items['latinDate'] = [] 
        items['persionDate'] = [] 
    
        for data in all_data:  # extracting data

            keys = ['openValue', 'minValue', 'maxValue', 'closeValue', 'changeAmount', 'changePercent', 'latinDate', 'persionDate']

            if data[-1][:4] == '1401': # crawling last 1 year price data

                for i in range(len(keys)):

                    if keys[i] != 'latinDate' and keys[i] != 'persionDate':

                        try:

                            #Cleaning the string and convert it to float
                            items[keys[i]].append(float(re.sub("[^0-9.]", "", data[i])))

                        except ValueError:

                            items[keys[i]].append(NULL)

                            print('Not a float')

                    elif keys[i] == 'latinDate':

                        #convert string to Date datatype
                        items[keys[i]].append(datetime.strptime(data[i], '%Y/%m/%d').date())

                    else:

                        items[keys[i]].append(data[i])
            else:

                break

        yield items

