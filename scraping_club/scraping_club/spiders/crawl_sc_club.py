import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrawlScClubSpider(CrawlSpider):
    name = 'crawl_sc_club'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/list_basic/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h4[@class='card-title']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//a[contains(text(), 'Next')]"), follow=True),
    )

    def parse_item(self, response):
        img_url = 'https://scrapingclub.com/static/img'
        item = {}
        item['title'] = response.xpath('//h3[@class="card-title"]/text()').get()
        item['price'] = response.xpath('//div[@class="card-body"]/h4/text()').get()
        item['description'] = response.xpath('//p[@class="card-text"]/text()').get()
        item['image'] = img_url + response.xpath('//img[@class="card-img-top img-fluid"]/@src').get()
        return item
