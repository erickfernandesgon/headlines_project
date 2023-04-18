import scrapy


class KeywordsSpider(scrapy.Spider):
    name = 'keywords'
    start_urls = ['https://www.ethos.org.br/categoria/noticias/', 'https://www.pactoglobal.org.br/noticias', 'https://ibram.org.br/noticias/', 'https://www.gov.br/mma/pt-br/assuntos/noticias']

    def parse(self, response):
        if 'https://www.ethos.org.br/categoria/noticias/' in response.url:
            yield{'highlighted_news_ethos ': response.xpath('//div[@class="noticiasGeralDestaqueDivImg"]/a/@title').get(),
                'highlighted_link_ethos ':response.xpath('//div[@class="noticiasGeralDestaqueDivImg"]/a/@href').get()
            }
        for headlines in response.css('.noticiasGeralDivTit2'):
                yield{
                'text_content_instituto_ethos' : headlines.css('.noticiasGeralDivTit2 p ::text').extract(),
                'link_content_ethos' : headlines.css('.noticiasGeralDivTit2 ::attr(href)').extract()
             }
        for news_pacto_global in response.css('.link-clean'):
                yield{
                'pacto_global_news': news_pacto_global.css('.link-clean ::text').extract(),
                'pacto_global_news_link':news_pacto_global.css('.link-clean ::attr(href)').extract()
             }
        for ibram in response.css('a.title.mtr-site'):
                yield{
                'ibram_news': ibram.css('a.title.mtr-site ::text').extract(),
                'ibram_link_news': ibram.css('a.title.mtr-site ::attr(href)').extract()
            }
        for meio_ambiente in response.css('h2.tileHeadline'):
            yield{
                'ministerio_meio_ambiente_news':meio_ambiente.css('h2.tileHeadline ::text').extract(),
                'ministerio_meio_ambiente_link':meio_ambiente.css('h2.tileHeadline ::attr(href)').extract()
            }


