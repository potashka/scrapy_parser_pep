# scrapy_parser_pep

# Парсинг документов PEP

Асинхронный парсер собирающий данные о Python Enhancement Proposals (PEP) с сайта https://www.python.org/. С каждой страницы PEP парсер собирает номер, название, статус и сохраняет два файла в формате .csv в директории results/:

Файл со списком PEP

Файл со сводкой по статусам

# Технологии проекта

Python — высокоуровневый язык программирования.
Scrapy — фреймворк для парсинга веб сайтов.


## Клонировать реппозиторий:

git clone https://github.com/potashka/scrapy_parser_pep.git

## Создать и активировать виртуальное окружение(Windows):

python -m venv env

source venv/Scripts/activate

## Установить зависимости из файла requirements.txt:

pip install -r requirements.txt

## Запуск парсера

scrapy crawl pep

## Автор: Алексей Потанин

Контакты: 

[github](https://github.com/potashka)

[email](avpotanin@gmail.com)