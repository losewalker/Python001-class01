第一周学习笔记
一、爬虫的基本流程
1.向目标网址发起请求，接受网页返回的资源
2.解析返回的资源，提取出需要的数据和信息
3.将提取到的信息进行持久化，即存储；或者进一步使用该数据



二、编写爬虫
1.requests + beautifulsoup/lxml
1) requests向目标网页发起请求，使用的方法为get(url,headers),url即为目标网址，headers是请求头信息，可以帮助我们的程序更好的模拟浏览器
2) 对网页进行分析，使用BeautifulSoup进行网页解析，常用方法为find_all(node),find(node),get(node), node即为要提取的网页结点信息
3) 将要存储的数据以ython自带的数据结构进行保存，存储时，可以有多种方式，将上述数据写入文件中，可以使用python标准的文件读写功能，也可以使用第三方库,如pandas写入cav。excel等文件中


2.爬虫框架scrapy
1) 在spider文件中设置好首次请求的地址，在start_requests中发起请求，使用的方法为scrapy.Request(url,callback）,url为请求的地址，callback为网页数据的解析方法
2) 编写数据解析方法，即parse(self, reaponse)方法, 解析时可以使用bs4或者lxml，推荐使用scrapy自带的选择器Selector
3) 在items文件中设置保存数据的组织方式，在pipeline中编写数据存储的逻辑，注意，要咋子setting.py将pipeline相关的设置项打开


三、关于Scrapy爬虫
1.组成及功能：
a 引擎：指挥其他组件协同工作，相当于requests爬虫中人工控制流程的功能， 无显示文件，需要修改
b 调度器： 处理引擎发来的请求，无需修改
c 下载器：下载网页，相当于reuqests的功能，无需修改
d 爬虫：网页的解析逻辑，相当于bs4和lxml，需要自行编写
e 项目、管道：数据持久化，项目相当于存储字段，管道相当于存储方式和存储逻辑，需要自行编写
f 下载中间件：一般不需要修改
g 爬虫中间件：一般不需要修改
2.常用命令（命令行运行）
1.scrapy startproject projectname ：新建一个爬虫项目
2.scrapy genspider name domain：新建一个爬虫，name即为爬虫名称，domain为该爬虫对应的域名
3.scrapy crawl spidername：运行爬虫