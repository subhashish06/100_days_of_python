"""
Program: Movies Scraper
Author: Subhashish Dhar
Date: 15/09/2021
"""

import requests
from bs4 import BeautifulSoup

response = requests.get("https://stacker.com/stories/1587/100-best-movies-all-time")
soup = BeautifulSoup(response.text, features="lxml")

movies = soup.find_all(class_="ct-slideshow__slide__text-container__caption")
movie_list = [movie.get_text().strip('\n') for movie in movies]
movie_list = movie_list[1:]
movie_list.reverse()

with open("movies.txt", mode='w',encoding="utf-8") as file_handler:
    for movie in movie_list:
        file_handler.write(movie)
        file_handler.write("\n")
