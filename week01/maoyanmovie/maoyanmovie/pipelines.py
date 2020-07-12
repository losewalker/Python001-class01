# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import os
from itemadapter import ItemAdapter


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        title, link, time, category = item['title'], item['link'], item['time'], item["category"]

        store_file = os.path.dirname(__file__) + '/spiders/maoyan_movie.csv'
        with open(store_file, 'a+', encoding='utf_8_sig', newline='') as f:
            writer = csv.writer(f, dialect='excel')
            writer.writerow((title, category, time, link))

        return item
