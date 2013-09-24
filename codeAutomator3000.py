#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import re
import os
import sys

pseudocode = sys.argv[1]

google_question_url = "https://www.google.fr/search?q=how+to+"+pseudocode+"&as_sitesearch=www.stackoverflow.com"
google_question_url = re.sub(' ', '%20', google_question_url)

google_soup = BeautifulSoup(requests.get(google_question_url).text)
a = google_soup.findAll('a')[25]

so_question_url = a['href']
so_question_url = re.sub('\/url\?q\=', '', so_question_url)
so_soup = BeautifulSoup(requests.get(so_question_url).text)

code =  so_soup.find('div', {"class": "accepted-answer"}).findAll('code')
code = str(code)
code = re.sub('<code>', '', code)
code_clean = re.sub('<\/code>', '', code)
code_clean = code_clean[1:-1]

print code_clean
