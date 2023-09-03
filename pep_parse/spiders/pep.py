import scrapy

from pep_parse.items import PepParseItem
# from pep_parse.settings import START_URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    start_urls = ['https://peps.python.org/']  # START_URL

    def parse(self, response):
        pep_list = response.css(
            '#numerical-index table.pep-zero-table tbody tr'
        )
        for pep in pep_list:
            yield response.follow(
                pep.css('a::attr(href)').get(), callback=self.parse_pep
            )

    def parse_pep(self, response):
        data = {
            'number': response.css('#pep-content > h1::text').get().split()[1],
            'name': ' '.join(
                response.css('#pep-content > h1::text').get().split()[3:]
            ),
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(data)
