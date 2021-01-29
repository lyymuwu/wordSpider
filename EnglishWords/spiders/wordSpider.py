import scrapy
from EnglishWords.items import EnglishwordsItem

firstword = ""
wordDatabase = open("helloworld.txt", 'r')
firstword = (wordDatabase.readline())[:-1]


def strCorrect(origalStr):
    begIndex = 1
    endIndex = -2
    for word in origalStr:
        if word != " " and word != "\n":
            begIndex = origalStr.index(word)
            break
    
    for word in reversed(origalStr):
        if word != " " and word != "\n":
            endIndex = origalStr[::-1].index(word)
            endIndex = -(endIndex+1)
            break
    return  origalStr[begIndex: (endIndex+1)] if endIndex!=(-1) else origalStr[begIndex:]


class WordspiderSpider(scrapy.Spider):
    name = 'wordSpider'
    allowed_domains = ['cambridge.org']
    start_urls = ['https://dictionary.cambridge.org/dictionary/english/' + firstword]
    print("HELLO: " + 'https://dictionary.cambridge.org/dictionary/english/' + firstword)

    def parse(self, response):
        item = EnglishwordsItem()
        item['word'] = strCorrect(str(response.xpath("//div[@class='h2 dhw dpos-h_hw  lpt-5 lpb-10']/text()").extract_first()))
        item['phoneticSymbols'] = response.xpath('//span[@class="ipa dipa lpr-2 lpl-1"]/text()').extract_first()
        item['meaning'] = response.xpath("//meta[@itemprop='headline']/@content").extract_first()  
        exampleList = response.xpath("//div[@class='degs had lbt lb-cm']/div/span").extract()

        correctList = []
        for example in exampleList:
            example = strCorrect(str(example)[18:-7])
            if "<em>" in example:
                index = example.find("<em>")
                example = example[:index] + example[index+4:]
                index = example.find("</em>")
                example = example[:index] + example[index+4:]
            correctList.append(example)
        item['example'] = correctList

        yield item

        word = wordDatabase.readline()
        new_links =  'https://dictionary.cambridge.org/dictionary/english/' + word
        if(len(word) > 0):
            yield scrapy.Request(new_links, callback=self.parse)

