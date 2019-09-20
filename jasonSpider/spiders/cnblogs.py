# -*- coding: utf-8 -*-
import scrapy
from jasonSpider.JasonspiderItem import JasonspiderItem


class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    # start_urls = ['https://cnblogs.com/#p2']

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Referer': 'https://www.cnblogs.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Method': 'GET',
        "Connection": "keep-alive",
        'Authority': 'www.cnblogs.com',
        'Cookie': '_ga=GA1.2.2102059732.1531759815; Qs_lvt_289801=1552891808%2C1554165719; Qs_pv_289801=1431315049922028800%2C125109502466263840; Hm_lvt_d8d668bc92ee885787caab7ba4aa77ec=1555816373; Hm_lvt_e7832a384d37994887357af186b47e63=1557969978; UM_distinctid=16b272104d02b3-08ddc8e881500d-37647e03-13c680-16b272104d1482; CNZZDATA1272990511=587500636-1560043096-https%253A%252F%252Fwww.baidu.com%252F%7C1560043096; CNZZDATA1254929547=2079358424-1559728158-https%253A%252F%252Fwww.baidu.com%252F%7C1563764734; Hm_lvt_444ece9ccd5b847838a56c93a0975a8b=1563765147; CNZZDATA1254128672=116913883-1567943776-https%253A%252F%252Fcn.bing.com%252F%7C1567943776; Hm_lvt_fa5cea7cd463480c76a420af9fa8973e=1567949567; _gid=GA1.2.450494227.1568875369',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36",
    }

    def start_requests(self):
        url = 'https://cnblogs.com'
        page = getattr(self, 'page', 1)
        url += '/#p' + page
        print(url)
        yield scrapy.Request(url, self.parse, 'GET', self.headers)

    def parse(self, response):
        items = []

        for each in response.xpath('//div[@id="post_list"]'):
            item = JasonspiderItem()
            item['title'] = each.xpath('//div[@class="post_item_body"]/h3/a/text()').extract()
            item['author'] = each.xpath('//div[@class="post_item_foot"]/a/text()').extract()
            item['recommended_count'] = each.xpath('//span[@class="diggnum"]/text()').extract()
            item['release_time'] = each.xpath('//div[@class="post_item_foot"]/text()').extract()
            item['comment_count'] = each.xpath('//span[@class="article_comment"]/a/text()').extract()
            item['view_count'] = each.xpath('//span[@class="article_view"]/a/text()').extract()

            items.append(item)

        return items
