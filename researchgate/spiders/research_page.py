import scrapy
from scrapy.http import Request

class ResearchPageSpider(scrapy.Spider):
    name = 'research-page'
    allowed_domains = ['researchgate.net']
    start_urls = ['https://researchgate.net/topic/Computer-Science/publications']

    def parse(self, response):
        url_page = response.xpath('//div[@class="nova-v-publication-item__stack-item"]//div[@itemprop="headline"]/a/@href').extract()
        for page in url_page:
            absolute_url = response.urljoin(page)
            yield Request(absolute_url,callback=self.pages)
    
        # next_url = response.xpath('//a[@rel = "next"]/@href').extract_first()
        # absolute_url = response.urljoin(f"https://researchgate.net/{next_url}")
        # yield scrapy.Request(absolute_url)
    def pages(self,response):
        header = response.xpath('//div[@class="research-detail-header-section__ie11"]/h1/text()').extract_first()
        date = response.xpath('//div[@class="research-detail-header-section__metadata"]//ul/li/text()').extract_first()
        doi = response.xpath('//*[@rel="noopener"]/text()').extract_first()

        yield{
            'header':header,
            'date':date,
            'doi':doi
        }