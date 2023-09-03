from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

# constants
ALLOWED_DOMAINS = [
    'peps.python.org',
]
START_URL = [f'https://{domain}/' for domain in ALLOWED_DOMAINS]
DT_FORMAT = "%Y-%m-%d_%H-%M-%S"
RESULTS = 'results'

FEED_EXPORT_ENCODING = "utf-8"

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    },
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
