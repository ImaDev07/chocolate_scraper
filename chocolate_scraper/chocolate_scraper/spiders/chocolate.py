from urllib.parse import urlparse, parse_qs
import scrapy

class ChocolateSpider(scrapy.Spider):
    name = 'chocolate'
    allowed_domains = ['chocolate.co.uk']
    start_urls = ['https://www.chocolate.co.uk/collections/all/products.json?page=1']

    def parse(self, response):
        data = response.json()
        products = data.get('products', [])

        for product in products:
            yield {
                'name': product.get('title'),
                'price': product.get('variants')[0].get('price') if product.get('variants') else None,
                'image_url': product.get('images')[0].get('src') if product.get('images') else None,
            }

        parsed_url = urlparse(response.url)
        query_params = parse_qs(parsed_url.query)
        current_page = int(query_params.get('page', ['1'])[0])

        if products:
            next_page = current_page + 1
            next_url = f'https://www.chocolate.co.uk/collections/all/products.json?page={next_page}'
            yield scrapy.Request(next_url, callback=self.parse)
