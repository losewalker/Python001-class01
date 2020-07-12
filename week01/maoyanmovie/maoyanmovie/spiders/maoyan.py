import scrapy
# from bs4 import BeautifulSoup as bs
from scrapy.selector import Selector
from maoyanmovie.items import MaoyanmovieItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ["https://maoyan.com/films?showType=3"]

    def start_requests(self):
        url = "https://maoyan.com/films?showType=3"
        yield scrapy.Request(url=url, callback=self.parse)


    # def parse(self, response):
    #     bs_info = bs(response.text, 'html.parser')

    #     data = []
    #     for tags in bs_info.find_all("div", attrs={"class":"movie-item-hover"}):
    #         file_info = []
    #         for atag in tags.find_all('a'):
    #             item = MaoyanmovieItem()
    #             film_name = atag.find_all('div', attrs={"class":"movie-hover-title"})[0].contents[1].text
    #             film_type = atag.find_all('div', attrs={"class":"movie-hover-title"})[1].contents[2].strip()
    #             on_time = atag.find_all('div', attrs={"class":"movie-hover-title"})[3].contents[2].strip()
    #             link = "https://maoyan.com"+atag.get('href')
    #             file_info = [film_name, film_type, on_time, link]
                
    #         data.append(file_info)
    
    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-item-hover"]')

        for movie in movies[:10]:
            title = movie.xpath('./a/div/div[1]/span[1]/text()').extract_first()
            link = movie.xpath('./a[@data-act="movie-click"]/@href').extract_first()
            category = movie.xpath('./a/div/div[2]/text()').extract()[1].strip('\n').strip()
            time = movie.xpath('./a/div/div[4]/text()').extract()[1].strip('\n').strip()

            item = MaoyanmovieItem()
            item['title'] = title
            item['link'] = 'https://maoyan.com' + link
            item['time'] = time
            item['category'] = category

            yield item