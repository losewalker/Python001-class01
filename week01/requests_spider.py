import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


maoyan_url = "https://maoyan.com/films?showType=3"
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
header = {'user-agent':user_agent}

response = requests.get(maoyan_url, headers=header)

bs_info = bs(response.text, 'html.parser')

data = []
for tags in bs_info.find_all("div", attrs={"class":"movie-item-hover"}):
    file_info = []
    for atag in tags.find_all('a'):
        film_name = atag.find_all('div', attrs={"class":"movie-hover-title"})[0].contents[1].text
        film_type = atag.find_all('div', attrs={"class":"movie-hover-title"})[1].contents[2].strip()
        on_time = atag.find_all('div', attrs={"class":"movie-hover-title"})[3].contents[2].strip()
        link = "https://maoyan.com"+atag.get('href')
        file_info = [film_name, film_type, on_time, link]
    data.append(file_info)

movies = pd.DataFrame(data = data[:10])
movies.to_csv('./movies.csv', encoding='utf_8_sig', index=False, header=False)
