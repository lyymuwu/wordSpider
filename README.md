# wordSpider
crawl word from web Cambridge dictionary

This is my first project upload in github.
you provide a txt document and this crawler will find meaning and other info of the word in the txt, and write them into WordList.txt
you can start it by using "scrapy crawl wordSpider"
I probably won't change it in the future, it is just used for fun.

In the end, Hello GitHub !


这个程序能爬取Cambridge Dictionary网站上的单词信息（如果有其他人像实现类似的功能，感觉有道都会比这个网站好弄。。。） :coffee:

目前已知的问题：
如果单词以大写开头，最后爬取到的单词可能会发生形式变换
介于爬取的网站上有些单词没有专门的example一栏，可能造成无例句，单词不显示的情况
（以后多半也不会改进）
