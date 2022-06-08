import scrapy


"""
Classe que contém métodos para raspagem
de dados na página de aos fatos.

## CREATE A PROJECT:
    scrapy startproject nome


## RUN:
    scrapy crawl nomeDadoNaClasse
##
"""


class QuotesSpider(scrapy.Spider):
    name = "first"  # nome para identificação na execução

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):  # trata os dados
        print(f"[*]status code: {response.status}")  # status code
        print(f"[*]ip address: {response.ip_address}")  # ip do site

