import csv
from collections import defaultdict
from datetime import datetime
from scrapy.exceptions import DropItem

from pep_parse.settings import BASE_DIR, DT_FORMAT, RESULTS

FILE_NAME = 'status_summary_{time}.csv'
TIME_NOW = datetime.now().strftime(DT_FORMAT)


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        status = item.get('status')
        self.results[status] += 1
        if status is None:
            raise DropItem('Статус не найден')
        return item

    def close_spider(self, spider):
        with open(
            f'{self.results_dir}/{FILE_NAME.format(time=TIME_NOW)}',
            'w', newline='', encoding='utf-8'  # только так русский сохраняет
        ) as f:
            csv.writer(
                f, dialect=csv.unix_dialect
            ).writerows(
                [
                    ('Статус', 'Количество'),
                    *self.results.items(),
                    ('Всего', sum(self.results.values()))
                ]
            )
