BASE_URL = "https://www.researchgate.net/"

DOI_LINK = "https://www.doi.org/"

ITEM_URL = "//div[@class='nova-v-publication-item__stack-item']//div[@itemprop='headline']/a/@href"

# request token
RG_REQUEST_TOKEN = "//meta[@name='Rg-Request-Token']"

# paper info
TITLE = "//h1/text()"
DATE = '//meta[@property="citation_publication_date"]/@content'
DOI = "//div[contains(text(),'DOI:')]/a/text()"
CONFERENCE = "//li[contains(text(),'Conference:')]/text()"
CITATIONS_COUNT = "//button[contains(@class,'citations')]//h2/text()"
REFERENCES_COUNT = "//button[contains(@class,'references')]//h2/text()"
ABSTRACT = "//div[@itemprop='description']//text()"
DOWNLOAD_LINK = "//meta[@property='citation_pdf_url']/@content"
DOWNLOAD_LINK_ = "//a[contains(@data-testid,'research-header-cta-download-fulltext')]/@href"



# references section
REFERENCES = "//div[@class='js-target-reference']//div[@class='nova-v-citation-item']"
# references title
REFERENCES_TITLE = ".//div[contains(@class,'nova-v-publication-item__title')]/a/text()"
# referecnes hyper link (might be null)
REFERENCES_LINK = ".//div[contains(@class,'nova-v-publication-item__title')]//@href"
# references type (eg. Article, Conference Paper, Null)
REFERENCES_TYPE = ".//span[contains(@class,'nova-v-publication-item__type')]/text()"
# references authors
REFERENCES_AUTHOR = ".//ul[contains(@class,'nova-v-publication-item__person-list')]//text()"
# references date
REFERENCES_DATE = ".//div[@class='nova-v-publication-item__meta-right']//span/text()"
# references abstract
REFERENCES_ABSTRACT = ".//div[contains(@class,'nova-v-publication-item__description')]/span/text()"