# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    # allowed_domains = ['https://www.douban.com/doulist/1264675/']
    # start_urls = ['https://www.douban.com/doulist/1264675//']
    start_urls = ['http://i.meituan.com/s/a?cid=-1&bid=-1&sid=defaults&p=2&ciid=50&bizType=area&csp=&nocount=true&stid_b=_b2&w=%E7%A6%8F%E9%9B%B7%E5%BE%B7']
    # start_urls = ['http://hz.meituan.com/s/%20%E7%A6%8F%E9%9B%B7%E5%BE%B7']
    def parse(self, response):
        # print response.body
        result = ''
        selector = scrapy.Selector(response)
        print selector
        books = selector.xpath('//dd[@class="poi-list-item"]')
        for each in books:
            title = each.xpath('.//span[@class="poiname"]/text()').extract_first()
            # rate = each.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()').extract()[0]
            # author = re.search('<div>(.*?)<br', each.extract(), re.S).group(1)
            result +="\n"+ title
        #自动抓取下一页,将新获取的request返回给引擎，实现继续循环。也就实现了“自动下一网页的爬取”。
        for i in range(2,21):
            url = 'http://i.meituan.com/s/a?cid=-1&bid=-1&sid=defaults&p='+str(i)+'&ciid=50&bizType=area&csp=&nocount=true&stid_b=_b2&w=%E7%A6%8F%E9%9B%B7%E5%BE%B7'
            # print(url)
            yield Request(url, callback=self.parse)
            
        #抓取的内容以追加的方式写入txt
        f =open('POIname2.txt',"w")
        f.write(result)
        f.close()


