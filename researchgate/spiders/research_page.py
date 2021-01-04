import scrapy
from scrapy.http import Request
import time
from . import path

def transform_number(s):
    if s == None:
        s = 0
    else:
        s = s[s.find("(")+1:s.find(")")]
        return int(s.replace(",",""))


class ResearchPageSpider(scrapy.Spider):
    name = 'research-page'
    allowed_domains = ['researchgate.net']
    start_urls = ['https://researchgate.net/topic/Computer-Science/publications']

    def parse(self, response):
        url_page = response.xpath(path.ITEM_URL).extract()
        for page in url_page:
            absolute_url = response.urljoin(page)
            yield Request(absolute_url,callback=self.pages)
        # next_url = response.xpath('//a[@rel = "next"]/@href').extract_first()
        # absolute_url = response.urljoin(f"https://researchgate.net/{next_url}")
        # yield scrapy.Request(absolute_url)
    def pages(self,response):
        title = response.xpath(path.TITLE).extract_first()
        date = response.xpath(path.DATE).extract_first()
        doi = response.xpath(path.DOI).extract_first()
        if doi == None:
            pass
        else:
            doi_url = path.DOI_LINK + doi
        # doi_url = path.DOI_LINK + doi
        download_url = response.xpath(path.DOWNLOAD_LINK).extract_first()
        conferance = response.xpath(path.CONFERENCE).extract_first()
        citations_count = transform_number(response.xpath(path.CITATIONS_COUNT).extract_first())
        reference_count =transform_number(response.xpath(path.REFERENCES_COUNT).extract_first())
        abstract = response.xpath(path.ABSTRACT).extract_first()
        reference_page = response.xpath(path.REFERENCES)
        refer = []
        for ref in reference_page:
            reference_title = ref.xpath(path.REFERENCES_TITLE).extract_first()
            reference_link = ref.xpath(path.REFERENCES_LINK).extract_first()
            absolute_reference_link = path.BASE_URL + reference_link
            reference_type = ref.xpath(path.REFERENCES_TYPE).extract_first()
            reference_date =ref.xpath(path.REFERENCES_DATE).extract_first()
            reference_abstract = ref.xpath(path.REFERENCES_ABSTRACT).extract_first()
            item = {
                'reference_title':reference_title,
                'reference_link':absolute_reference_link,
                'reference_type':reference_type,
                'reference_date':reference_date,
                'reference_abstract':reference_abstract,
            }
            refer.append(item)
        yield{
            'title':title,
            'date':date,
            'doi':doi,
            'conferance':conferance,
            'citations_count':citations_count,
            'reference_count':reference_count,
            'abstract':abstract,
            'doi_url':doi_url,
            'download_url':download_url,
            'reference':refer,
            
        }









    # def reference(self,response):
    #     reference_page = response.xpath(path.REFERENCES)
    #     for ref in reference_page:
    #         reference_title = ref.xpath(path.REFERENCES_TITLE).extract_first()
    #         reference_link = ref.xpath(path.REFERENCES_LINK).extract_first()
    #         reference_type = ref.xpath(path.REFERENCES_TYPE).extract_first()
    #         reference_date =ref.xpath(path.REFERENCES_DATE).extract_first()
    #         reference_abstract = ref.xpath(path.REFERENCES_ABSTRACT).extract_first()
    #         yield {
    #             'reference_title':reference_title,
    #             'reference_link':reference_link,
    #             'reference_type':reference_type,
    #             'reference_date':reference_date,
    #             'reference_abstract':reference_abstract
    #             }










        # reference_page = response.xpath(path.REFERENCES)
        # for ref in reference_page:
        #     reference_title = ref.xpath(path.REFERENCES_TITLE).extract_first()
        #     reference_link = ref.xpath(path.REFERENCES_LINK).extract_first()
        #     reference_type = ref.xpath(path.REFERENCES_TYPE).extract_first()
        #     reference_date =ref.xpath(path.REFERENCES_DATE).extract_first()
        #     reference_abstract = ref.xpath(path.REFERENCES_ABSTRACT).extract_first()
        #     yield {
        #         'reference_title':reference_title,
        #         'reference_link':reference_link,
        #         'reference_type':reference_type,
        #         'reference_date':reference_date,
        #         'reference_abstract':reference_abstract
        #         }

        