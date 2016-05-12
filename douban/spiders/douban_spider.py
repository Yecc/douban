# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from douban.items import DoubanItem
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

#解决编码错误
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class DoubanSpider(Spider):
	name = "douban"
	download_delay = 1
	allowed_domains = ["movie.douban.com"]
	start_urls = [
		"https://movie.douban.com/top250?start=0&filter=",
		"https://movie.douban.com/top250?start=25&filter=",
		"https://movie.douban.com/top250?start=50&filter=",
		"https://movie.douban.com/top250?start=75&filter=",
		"https://movie.douban.com/top250?start=100&filter=",
		"https://movie.douban.com/top250?start=125&filter=",
		"https://movie.douban.com/top250?start=150&filter=",
		"https://movie.douban.com/top250?start=175&filter=",
		"https://movie.douban.com/top250?start=200&filter=",
		"https://movie.douban.com/top250?start=225&filter="
	]
	
	def parse(self,response):
		sel = Selector(response)
		sites = sel.xpath('//div[@class="item"]/div[@class="info"]')
		items = []
		for site in sites:
			item = DoubanItem()
			item['title'] = site.xpath('div[@class="hd"]/a/span[@class="title"]/text()').extract()
			item['rating_num'] = site.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
			item['link'] = site.xpath('div[@class="hd"]/a/@href').extract()
			items.append(item)
			#decode("unicode_escape")
		open('douban.txt','a').write(str(items).decode("unicode_escape"))
		open('douban.txt','a').close()
		
		

