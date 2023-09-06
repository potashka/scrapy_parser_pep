import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import BASE_DIR, DT_FORMAT, RESULTS

FILE_NAME = 'status_summary_{}.csv'


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        self.results[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        filename = FILE_NAME.format(datetime.now().strftime(DT_FORMAT))
        with open(
            f'{self.results_dir}/{filename}',
            'w', newline='', encoding='utf-8',  # только так русский сохраняет
        ) as f:
            csv.writer(
                f, dialect=csv.unix_dialect, quoting=csv.QUOTE_NONE
            ).writerows((
                ('Статус', 'Количество'),
                *self.results.items(),
                ('Всего', sum(self.results.values()))
            ))
