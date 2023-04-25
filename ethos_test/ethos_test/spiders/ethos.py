import scrapy


class KeywordsSpider(scrapy.Spider):
    name = 'keywords'
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    start_urls = ['https://www.ethos.org.br/categoria/noticias/', 'https://www.pactoglobal.org.br/noticias', 'https://ibram.org.br/noticias/', 'https://www.gov.br/mma/pt-br/assuntos/noticias', 'https://www7.fiemg.com.br/Noticias', 'https://www.amcham.com.br/noticias','https://www.aberje.com.br/category/noticias/', 'https://abag.com.br/noticias-abag/']

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
            headline = str(FIEG.css('.media.media--vertical ::text').extract()).strip().replace(r'\n', '').replace(r'\r', '').replace(' \\t','').replace('                        ',"")
            link = FIEG.css('.media.media--vertical ::attr(href)').get()
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
        for each_headline in response.css('.cover-collection-tile.tile-content'):
            yield {
                'headline_news':str(each_headline.css('.cover-collection-tile.tile-content ::text').extract()).strip().replace('\n', "").replace('\\n', "").replace('               ', "")

            }
        for news_associations in response.css('.coluna9'):
            yield {
                'headline_aberge': str(
                    news_associations.css('.coluna9 ::text').extract()).strip().replace(r'\n\t\t\t\t\t', "").replace(r'\t\t\t\t',"").replace(r'Página', ""),
                'links_aberge': str(news_associations.css('.coluna9 ::attr(href)').extract())
            }
        for abag_association in response.css('.dg-blog-grid'):
            yield {
                'headline_abag': str(abag_association.css('.dg-blog-grid ::text').extract()),
                'links_abag': str(abag_association.css('.dg-blog-grid ::attr(href)').extract())
            }

