import re
import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import START_URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    start_urls = START_URL

    def parse(self, response):
        for pep in response.css(
            '#numerical-index table.pep-zero-table tbody tr a::attr(href)'
        ):
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = re.search(
            r'PEP\s(?P<number>\d+)\W+(?P<name>.+)',
            response.css('#pep-content > h1::text').get()
        ).groups()
        status = response.css('abbr::text').get()
        yield PepParseItem(
            number=number, name=name, status=status,
        )
