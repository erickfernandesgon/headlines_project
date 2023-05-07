import scrapy
class KeywordsSpider(scrapy.Spider):
    name = 'keywords'
    allowed_domains = 'globalfert.com.br'
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    start_urls = ['https://www.ethos.org.br/categoria/noticias/', 'https://www.pactoglobal.org.br/noticias', 'https://ibram.org.br/noticias/', 'https://www.gov.br/mma/pt-br/assuntos/noticias', 'https://www7.fiemg.com.br/Noticias', 'https://www.amcham.com.br/noticias','https://www.aberje.com.br/category/noticias/', 'https://abag.com.br/noticias-abag/', 'https://www.cnabrasil.org.br/cna/noticias', 'https://www.socioambiental.org/historias', 'http://www.aprosoja.com.br/comunicacao/noticias-e-releases/','https://www.saopaulo.sp.gov.br/ultimas-noticias/', 'https://www.desenvolvimentoeconomico.sp.gov.br/category/noticias/', 'https://www.al.sp.gov.br/noticias', 'https://globalfert.com.br/category/noticias/']

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
            yield {
                'FIEMG_NEWS_HEADLINE': str(FIEG.css('.media.media--vertical ::text').extract()),
                'FIEMG_NEWS_HEADLINE_LINK':str(FIEG.css('.media.media--vertical ::attr(href)').extract())
             }
        for meio_ambiente in response.css('h2.tileHeadline'):
            yield {
                'ministerio_meio_ambiente_news': meio_ambiente.css('h2.tileHeadline ::text').extract(),
                'ministerio_meio_ambiente_link': meio_ambiente.css('h2.tileHeadline ::attr(href)').extract()
            }
        for each_headline in response.css('.cover-collection-tile.tile-content'):
            yield {
                'headline_news': str(each_headline.css('.cover-collection-tile.tile-content ::text').extract())
            }
        for news_associations in response.css('.coluna9'):
            yield {
                'headline_aberge': str(
                    news_associations.css('.coluna9 ::text').extract()),
                'links_aberge': str(news_associations.css('.coluna9 ::attr(href)').extract())
            }
        for abag_association in response.css('.dg-blog-grid'):
            yield {
                'headline_abag': str(abag_association.css('.dg-blog-grid ::text').extract()),
                'links_abag': str(abag_association.css('.dg-blog-grid ::attr(href)').extract())
            }
        for cna_highlights in response.css('.grid-destaque-lista'):
            yield {
                'headline_cna': str(cna_highlights.css('.grid-destaque-lista ::text').extract()),
                'links_abag': str(cna_highlights.css('.grid-destaque-lista ::attr(href)').extract())
            }
        for socio_ambiental in response.css('.grid-3-columns'):
            yield {
                'headline_socioambiental': str(socio_ambiental.css('.grid-3-columns ::text').extract()),
                'links_socioambientals': str(socio_ambiental.css('.grid-3-columns ::attr(href)').extract())
            }
        for aprosja_series in response.css('.listagem'):
            yield {
                'headline_aprosja': str(aprosja_series.css('.listagem ::text').extract()),
                'links_aprosja': str(aprosja_series.css('.listagem ::attr(href)').extract())
            }
        for governo_sp_website in response.css('.style-post-list'):
            yield {
                'headline_governo_sampa': str(governo_sp_website.css('.style-post-list ::text').extract()),
                'links_governo_sampa': str(governo_sp_website.css('.style-post-list ::attr(href)').extract())
            }
        for desenvolvimento_sp_website in response.css('.lista'):
            yield {
                'headline_desenvolvimento_sampa': str(desenvolvimento_sp_website.css('.lista ::text').extract()),
                'links_desenvolvimento_sampa': str(desenvolvimento_sp_website.css('.lista ::attr(href)').extract())
            }
        for alesp in response.css('.rw'):
            yield {
                'headline_alesp': str(alesp.css('.rw ::text').extract()),
                'links_alesp': str(alesp.css('.rw ::attr(href)').extract())
            }
        for globalfert in response.css('.mg-box-container.clearfix'):
            yield {
                'headline_globalfert': str(globalfert.css('.mag-box-container.clearfix ::text').extract()),
                'links_globalfert': str(globalfert.css('.mag-box-container.clearfix ::attr(href)').extract())
            }
