# -*- coding: utf-8 -*-
import scrapy
from jasonSpider.JasonspiderItem import JasonspiderItem


class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    # allowed_domains = ['cnblogs.com']
    # start_urls = ['https://cnblogs.com/#p2']

    def start_requests(self):
        url = 'https://cnblogs.com'
        page = getattr(self, 'page', 1)
        url += '/#p' + page
        print(url)
        yield scrapy.Request(url, self.parse)

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
