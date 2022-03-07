from bs4 import BeautifulSoup
import requests as re

if __name__ == '__main__':
    url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20220302'
    html = re.get(url)

    # print(html)  # response 200: ok
    # print(html.text) # html code들이 출력

    # bs4에서 가장 많이 사용하는 함수, find, select
    soup = BeautifulSoup(html.text, 'html.parser')
    # # body > div > div.sect - showtimes > ul > li: nth - child(1) > div > div.info - movie > a > strong
    movie_title_list = soup.select('div.info-movie')

    # for title in movie_title_list:
    #     print(title.select_one('a > strong').text.strip())  # text로 strong 태그는 제거 + strip으로 양 쪽 공백 제거

    imax_movie = soup.select_one('span.imax')

    if imax_movie:
        title = soup.select_one('div.info-movie > a > strong').text.strip()
        print(title + ' IMAX 영화가 상영중입니다.')
    else:
        print('현재 IMAX 영화를 상영하지 않습니다.')