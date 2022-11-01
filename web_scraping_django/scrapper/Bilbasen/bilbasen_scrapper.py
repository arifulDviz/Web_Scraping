# from operator import contains
from gc import callbacks
from pydoc import pager
from urllib.parse import urljoin
import scrapy

import json

import logging

logging.basicConfig

logging.basicConfig(filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    page = 1

    def start_requests(self):
        url = 'https://www.bilbasen.dk/find-en-forhandler/search'

        yield {'['}

        yield scrapy.Request(url, callback=self.parse)
        yield {']'}

    def parse(self, response):
        Car_Dealers = response.css('div#DealerSearchResults div.cf')

        if len(Car_Dealers) == 0:
            return

        for car_dealer in Car_Dealers:
            # subcategory_result.append({
            #     'subcategory': subcategory
            # })

            Name = car_dealer.css('div.left p strong::text').get()
            # Phone =
            # Web_Link = car_dealer.css()
            Details = car_dealer.css('p::text')

            Address = Details[1].re(
                r'[^"\r\n"]+')[0].strip() + ' ' + Details[2].re(r'[^"\r\n"]+')[0].strip()

            Phone = Details[3].re(
                r'[^"\r\n"]+')[0].strip().split(":")[1].strip()

            Fax = Details[4].re(r'[^"\r\n"]+')[0].strip().split(":")[1].strip()
            Number_of_listings = int(Details[9].re(
                r'[^"\r\n"]+')[0].strip().split(':')[1].strip())
            Web_Link = car_dealer.css('p a::text').get()

            yield {

                'Name': Name,
                'Address': Address,
                'Phone': Phone,
                'Fax': Fax,
                'Number_of_listings': Number_of_listings,
                'Web_Link': Web_Link

            }

        # for subcategory in subcategories_slider:
        #     subcategory_result.append(
        #         {
        #             'subcategory': subcategory.re(r'[^“\n”]+')[0],
        #         }
        #     )
        pagination_arr = response.css('ul.pagination li a::text').getall()

        self.page = self.page+1

        yield scrapy.Request(url='https://www.bilbasen.dk/find-en-forhandler/search/side-' + str(self.page), callback=self.parse)

    def parse2(self, response):
        return

        # Product_Details_List.json is created by the spider arguments in scrapy
