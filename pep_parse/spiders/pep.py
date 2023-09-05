import re
import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import START_URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    start_urls = START_URL

    def parse(self, response):
        pep_list = response.css(
            '#numerical-index table.pep-zero-table tbody tr a::attr(href)'
        )
        for pep in pep_list:
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        tag = response.css('#pep-content > h1::text').get()
        pattern = r"PEP\s(?P<number>\d+)\W+(?P<name>.+)"
        number, name = re.search(pattern, tag).groups()
        status = response.css('abbr::text').get()
        yield PepParseItem(
            dict(number=number, name=name, status=status,)
        )
