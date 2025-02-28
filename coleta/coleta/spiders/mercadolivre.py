import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]

    def parse(self, response):
        products = response.css('div.poly-card__content')

        for product in products:

            yield {                
                'brand': product.css('span.poly-component__brand::text').get(),
                'name': product.css('h3.poly-component__title-wrapper a::text').get(),
                'reviews_rating_number': product.css('span.poly-reviews__rating ::text').get(),
                'reviews_amount': product.css('span.poly-reviews__total ::text').get(),
                'price': product.css('h3.poly-component__title-wrapper a::text').get()
            }

