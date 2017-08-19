# -*- coding: utf-8 -*-
from scrapy import Selector
from scrapy import Request
from scrapy.spiders import CrawlSpider
from recipes.items import Cookbook

class ScraperSpider(CrawlSpider):
    name = 'scraper'
    allowed_domains = ['tarladalal.com']
    #start_urls = ['https://www.tarladalal.com/recipes-for-indian-in-hindi-language-2']
    
    def start_requests(self):
        urli='https://www.tarladalal.com/recipes-for-indian-2?pageindex='
        urls=[]        
        for i in range(1,8):
            urls.append(urli+str(i))
        for url in urls:
            print url
            yield Request(url=url,callback=self.parse)


    def parse(self,response):
        res=Selector(response)
        for li in res.xpath('//span[@class="rcc_recipename"]'):
            url=li.xpath('.//a/@href').extract_first()
            if url is not None:
                yield response.follow(response.urljoin(li.xpath('.//a/@href').extract_first()),callback=self.parse_item)                
            
            
    def parse_item(self, response):
        cook=Cookbook()
        cook['name']=response.url.split('/')[-1]        
        sel=Selector(response)
        #for each field its xpath is selected and the result taken and stored.
        yo=sel.xpath('//*[@id="rcpnutrients"]')
        cook['nutrients']={}        
        for li in yo.xpath('.//tr'):
            cook['nutrients'][li.xpath('.//td/text()').extract_first()]=li.xpath('.//td[2]//text()').extract_first()
        cook['steps']={}
        i=1
        for li in sel.xpath('//*[@id="rcpprocsteps"]/li'):
            cook['steps'][i]=li.xpath('.//text()').extract_first()
            i=i+1
        cook['reviews']={}
        i=1
        for li,li1 in zip(sel.xpath('//span[@itemprop="reviewBody"]'),sel.xpath('//span[@itemprop="ratingValue"]')):
            if li.xpath('.//text()').extract_first() is not None and len(li.xpath('.//text()').extract_first())>1:
                cook['reviews'][i]={'text':li.xpath('.//text()').extract_first(),'rating':li1.xpath('.//text()').extract_first()}
            else:
                cook['reviews'][i]={'text':u'N/A','rating':li1.xpath('.//text()').extract_first()}
            i+=1
        i=1
        cook['ingredients']={}
        for li in sel.xpath('//span[@itemprop="ingredients"]'):
            first=li.xpath('.//a//text()').extract_first()
            second=li.xpath('./span/text()').extract_first()
            if first is not None and second is not None:
                cook['ingredients'][i]={first:second}
            elif first is not None:
                cook['ingredients'][i]={first:u'N/A'}
            else:
                i-=1
            i+=1
        yield cook
