from bs4 import BeautifulSoup
from datetime import datetime
import requests as re

today = datetime.today().strftime("%Y%m%d")

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=' + today

html = re.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

imax = soup.select_one('span.imax')

if imax:
    imax = imax.find_parent('div', class_='col-times')
    imax_movie = imax.select_one("div.info-movie > a > strong").text.strip()
else:
    imax_movie = None