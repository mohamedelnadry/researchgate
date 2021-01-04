import scrapy
from scrapy.http import Request

class ResearchSpider(scrapy.Spider):
    name = 'research'
    allowed_domains = ['researchgate.net']
    start_urls = ['https://researchgate.net/topic/Computer-Science/publications']

    def parse(self, response):
        allitem = response.xpath('//div[@class="nova-o-stack__item"]//div[@class="nova-v-publication-item nova-v-publication-item--size-m gtm-research-item"]')
        for item in allitem:
            header = item.xpath('.//div[@class="nova-v-publication-item__stack-item"]//div[@itemprop="headline"]/a/text()').extract_first()
            type_1 = item.xpath('.//span[@priority="secondary"]/text()').extract_first()  
            date = item.xpath('.//div[@class="nova-v-publication-item__meta-right"]/ul/li/span/text()').extract_first()
            download_url = item.xpath(  ).extract_first()
            absolute_download_url = f'https://www.researchgate.net/{download_url}'
            abstract = item.xpath('.//div[@class="nova-e-text nova-e-text--size-m nova-e-text--family-sans-serif nova-e-text--spacing-none nova-e-text--color-inherit nova-v-publication-item__description"]/text()').extract_first()
            yield{
                'header':header,
                'type_1':type_1,
                'date':date,
                'download_url':absolute_download_url,
                'abstract':abstract}

        next_url = response.xpath('//a[@rel = "next"]/@href').extract_first()
        absolute_url = response.urljoin(f"https://researchgate.net/{next_url}")
        yield scrapy.Request(absolute_url)








    # def parse_one_page(self,response):
    #     items_pages = response.xpath('//div[@class="nova-o-stack__item"]//div[@class="nova-v-publication-item nova-v-publication-item--size-m gtm-research-item"]')
    #     for i in items:
    #         page_url = item.xpath('.//div[@class="nova-v-publication-item__stack-item"]//div[@itemprop="headline"]/a/@herf').extract_first()
    #         absolute_url = response.urljoin(page_url)
            




        # response.xpath('.//a[contains(.,"Download full-text")]/@href').extract()

        # download_url = item.xpath('.//footer[@class="nova-v-publication-item__footer"]//a[contains(.,"Download full-text")]/@href').extract_first()
