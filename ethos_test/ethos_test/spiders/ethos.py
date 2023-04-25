import scrapy


class KeywordsSpider(scrapy.Spider):
    name = 'keywords'
    start_urls = ['https://www.ethos.org.br/categoria/noticias/', 'https://www.pactoglobal.org.br/noticias', 'https://ibram.org.br/noticias/', 'https://www.gov.br/mma/pt-br/assuntos/noticias', 'https://www7.fiemg.com.br/Noticias']

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
                'ibram_news': [date.strip() for date in response.css('.pg-noticias .news-list .box .data-card .text-info .card-nav .d-flex .date ::text').extract()],
                'ibram_link_news': ibram.css('a.title.mtr-site ::attr(href)').extract()
            }
        for FIEG in response.css('.media.media--vertical'):
    # Extract the headline and link
    headline = FIEG.css('.media.media--vertical ::text').get().strip().replace('\n', '').replace('\r', '')
    link = FIEG.css('.media.media--vertical ::attr(href)').get()

    # Check if the headline contains "Desenvolvimento Industrial" and skip if it does
    if "Desenvolvimento Industrial" in headline:
        continue

    # Check if the headline contains a date and remove it
    if any(date in headline for date in ['01/','02/','03/','04/','05/','06/','07/','08/','09/','10/','11/','12/']):
        headline = headline.split(" ")[1:]

    # Yield the cleaned headline and link
    yield {
        'FIEMG_NEWS_HEADLINE': headline,
        'FIEMG_NEWS_HEADLINE_LINK': link
        }
        for meio_ambiente in response.css('h2.tileHeadline'):
            yield {
                'ministerio_meio_ambiente_news': meio_ambiente.css('h2.tileHeadline ::text').extract(),
                'ministerio_meio_ambiente_link': meio_ambiente.css('h2.tileHeadline ::attr(href)').extract()
            }


