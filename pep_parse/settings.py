from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

# constants
ALLOWED_DOMAINS = [
    'peps.python.org',
]
START_URL = [f'https://{parameters}/' for parameters in ALLOWED_DOMAINS]
DT_FORMAT = "%Y-%m-%d_%H-%M-%S"
RESULTS = 'results'

FEED_EXPORT_ENCODING = "utf-8"

FEEDS = {
    f'{RESULTS}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    },
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
