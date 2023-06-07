import scrapy

class KeywordsSpider(scrapy.Spider):
    name = 'keywords'
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    start_urls = ['https://www.ethos.org.br/categoria/noticias/', 'https://www.pactoglobal.org.br/noticias', 'https://ibram.org.br/noticias/', 'https://www.gov.br/mma/pt-br/assuntos/noticias', 'https://www7.fiemg.com.br/Noticias', 'https://www.amcham.com.br/noticias','https://www.aberje.com.br/category/noticias/', 'https://abag.com.br/noticias-abag/', 'https://www.cnabrasil.org.br/cna/noticias', 'https://www.socioambiental.org', 'http://www.aprosoja.com.br/comunicacao/noticias-e-releases/','https://www.saopaulo.sp.gov.br/ultimas-noticias/', 'https://www.desenvolvimentoeconomico.sp.gov.br/category/noticias/', 'https://www.al.sp.gov.br/noticias']

    def parse(self, response):
        if 'https://ibram.org.br/noticias/' in response.url:
            for ibram in response.css('.title.mtr-site'):
                yield{
                'IBRAM_HEADLINES': ibram.css('.title.mtr-site ::text').extract(),
                'IBRAM_LINKS': ibram.css('.title.mtr-site ::attr(href)').extract(),
                'IBRAM_DATA_HEADLINE': response.css('.date ::text').extract()
            }
        for fiemg in response.css('.media.media--vertical'):
            yield {
                'FIEMG_NEWS_HEADLINE': str(fiemg.css('.media.media--vertical ::text').extract()),
                'FIEMG_NEWS_HEADLINE_LINK':str(fiemg.css('.media.media--vertical ::attr(href)').extract()),
             }
        for meio_ambiente in response.css('h2.tileHeadline'):
            yield {
                'ministerio_meio_ambiente_news': meio_ambiente.css('h2.tileHeadline ::text').extract(),
                'ministerio_meio_ambiente_link': meio_ambiente.css('h2.tileHeadline ::attr(href)').extract(),
                'ministerio_meio_ambiente_data': response.css('.summary-view-icon ::text').extract()
            }
        for amcham in response.css('.collection-item'):
            yield {
                'AMCHAM_HEADLINES': str(amcham.css('.collection-item ::text').extract()),
                'AMCHAM_LINKS':str(amcham.css('.collection-item ::attr(href)').extract()),
                'AMCHAM_DATAS': str(response.css('.dtpub ::text').extract())
            }
        for cna_highlights in response.css('.card__titulo.deep-sea-100'):
            yield {
                'headline_cna_mainly': cna_highlights.css('.card__titulo.deep-sea-100 ::text').extract()
            }
        for cna_highlights_texts_2 in response.css('.card__titulo.bourbon-important'):
            yield {
                'headline_cna_secondpart': cna_highlights_texts_2.css('.card__titulo.bourbon-important ::text').extract()
            }
        for cna_links_mainly in response.css('.card-mais-noticias'):
            yield {
                'links_cna': cna_links_mainly.css('.card-mais-noticias ::attr(href)').extract()
            }
        for cna_links_part2 in response.css('.card-noticia-grande.pequeno.post'):
            yield {
                'links_cma_part2': cna_links_part2.css('.card-noticia-grande.pequeno.post ::attr(href)').extract()
            }
        for cna_data in response.css('.card__data'):
             yield {
                'CNA_DATA': str(cna_data.css('.card__data ::text').extract())
            }
        for socio_ambiental_headlines in  response.css('.card-title'):
            yield {
                'headline_socioambiental': str(socio_ambiental_headlines.css('.card-title ::text').extract())
            }
        for socio_ambiental_links in response.css('.change-border-color.card-home-news'):
            yield {
                'link_socioambiental': str(socio_ambiental_links.css('.change-border-color.card-home-news ::attr(href)').extract())
            }
        for socio_ambiental_dates in response.css('.card-date'):
            yield {
                'date_socioambiental': str(socio_ambiental_dates.css('.card-date ::text').extract())
            }
        for aprosja_series in response.css('.listagem'):
            yield {
                'headline_aprosja': str(aprosja_series.css('.listagem ::text').extract()),
                'links_aprosja': str(aprosja_series.css('.listagem ::attr(href)').extract())
            }
        for dates in response.css('.centro'):
            yield {
                'aprosja_dates':dates.css('.centro ::text').extract()
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
        for data_sampa in response.css('.date'):
            yield {
                'headline_data_sampa':data_sampa.css('.date ::text').extract()
            }
        for alesp in response.css('.rw'):
            yield {
                'headline_alesp': str(alesp.css('.rw ::text').extract()),
                'links_alesp': str(alesp.css('.rw ::attr(href)').extract())
            }
        for data_publicacao_alesp in response.css('.data-publicacao'):
            yield{
                'data_publicacao_alesp':str(data_publicacao_alesp.css('.data-publicacao ::text').extract())
            }