# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

outputFile = open("WordList.txt", "w", encoding='UTF-8')

class EnglishwordsPipeline:
    def process_item(self, item, spider):
        line = item['word'] + "/" + item['phoneticSymbols'] + "/" + "\nMEANING:\n\t " + item['meaning'] + "\nExample:"
        for example in item['example']:
            line += ("\n\t" + example)
        line.encode("utf-8")
        
        outputFile.writelines(line+"\n\n")
        return item
