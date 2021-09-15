"""
Program: Hacker News Website Scraper
Author: Subhashish Dhar
Date: 14/09/2021
"""

import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, features="lxml")

links = [link.get('href') for link in soup.find_all("a", class_="storylink")]
stories = [story.get_text() for story in soup.find_all("a", class_="storylink")]
points = [int(point.get_text().split()[0]) for point in soup.find_all("span", class_="score")]

index_of_max_score = points.index(max(points))

print(f"Most upvoted story: {stories[index_of_max_score+1]}")
print(f"Link: {links[index_of_max_score+1]}")
print(f"points: {points[index_of_max_score]}")
