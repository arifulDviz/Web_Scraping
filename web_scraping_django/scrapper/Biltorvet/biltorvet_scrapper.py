# from operator import contains
from gc import callbacks
from pydoc import pager
from urllib.parse import urljoin
import requests
import scrapy

import json

import logging

logging.basicConfig

logging.basicConfig(filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = 'https://www.biltorvet.dk/forhandler'

        headers = {'Accept': 'text/html,application/xhtml+xml,*/*',

                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
                   }

        yield scrapy.Request(url, headers=headers, callback=self.parse2)

    def parse2(self, response):

        Values = response.css('companysearch').re(
            r'\"value\":\d+')

        num_of_values = len(Values)

        print(" Values ", Values)

        for i in range(10, num_of_values):
            # for i in range(10, 20):
            url = "https://www.biltorvet.dk/Api/Company/Search"
            print(int(Values[i].split(':')[1].strip()))

            payload = json.dumps({

                "MakeIdList": [

                    int(Values[i].split(':')[1].strip())
                    # 928
                ],

                "SearchString": ""

            })

            headers = {

                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',

                'Accept': 'application/json, text/plain, */*',

                'Content-Type': 'application/json',

                'sec-ch-ua-mobile': '?0',

                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',

                'sec-ch-ua-platform': '"Windows"',

                'Sec-Fetch-Site': 'same-origin',

                'Sec-Fetch-Mode': 'cors',

                'Sec-Fetch-Dest': 'empty',

                'host': 'www.biltorvet.dk',

                'Cookie': 'biltorvet.dk-AnonUserGuid=df04ad68-e59a-46b8-b72e-c8415ae0f878; biltorvet.dk-AspNetCore.Session=CfDJ8EOxtH2Ksp9MgxoRX4iIhXZPRR2UC6P4r78DsLZ7qgh9bhwVZaKcHIioo308JniDPAHYxh4aAbvl4wsPDwLfApuuzMJ8XHSzqWP0jxF%2FISxf3vrNWR8ufIbg2aGs27OIVhIeDJZVinb3uHduq7urxeRnkk%2Br0iWIT%2BJbRCf9J47I; biltorvet.dk-DeviceGuid=d259adc8-c67a-46e1-9f31-10410223307e'

            }

            yield scrapy.Request(url, method='POST', headers=headers,
                                 body=(payload), callback=self.parse3)
            # break

    def parse3(self, response):
        print(json.loads(response.body))

        data = json.loads(response.body)
        company_list = data['companyList']
        # print(company_list)
        headers = {
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'host': 'www.biltorvet.dk'
        }

        if len(company_list) > 0:
            for company in company_list:
                company['url'] = response.urljoin(company['url'])
                yield scrapy.Request(url=company['url'], headers=headers, cb_kwargs={'company': company}, callback=self.parse4)

    # pass

    # print(company_list)

    # return
    # return super().parse(response, **kwargs)
    def parse4(self, response, company):

        # print(response.body)

        contact_information = response.css('subheadercompany')

        # print(" contact_information ", contact_information.get())
        # company = {}
        if contact_information is not None:
            # contact_information = contact_information[':contact-information']
            if len(response.css('subheadercompany').re(r'\"tel:\d+')) > 0:
                phone_number = (response.css('subheadercompany').re(
                    r'\"tel:\d+')[0].split(':')[1].strip())
                company['phone'] = phone_number
            else:
                company['phone'] = ''

            # contact_details = json.loads(contact_information)

            # print(contact_details)

            if response.css('a.js-contact-homepage-link') is not None:
                company['website'] = response.css(
                    'a.js-contact-homepage-link b::text').get()
            else:
                company['website'] = ''

            # company['phone'] = phone_number
        else:
            company['phone'] = ''
            company['website'] = ''

        # print(company)

        # yield {
        #     json.dumps(company)
        # }

        yield{
            'id': company['id'],
            'name': company['name'],
            'address': company['address'],
            'zipAndCity': company['zipAndCity'],
            'website': company['website'],
            'phone': company['phone'],
            'adCount': company['adCount'],
            # 'id': company['id'],
        }
