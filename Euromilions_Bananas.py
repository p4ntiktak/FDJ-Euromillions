# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:12:50 2021

@author: kYcu
"""

from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import csv



from random import*
from time import*


zpi_url_euromillions ="https://media.fdj.fr/static/csv/euromillions/euromillions_202002.zip"


with urlopen(zpi_url_euromillions) as f:
    with BytesIO(f.read()) as b, ZipFile(b) as myzipfile:
         myzipfile.extract('euromillions_202002.csv')
#        foofile_lotto = myzipfile.open('loto_201911.csv')
#        print(foofile_lotto.read())


lol= open('euromillions_202002.csv', "r")
csv_lol_reader = csv.reader(lol,delimiter=";")

next(csv_lol_reader)
number_of_rows = 0
list_from_lol = []
list_stars = []
last_date = []

for row in csv_lol_reader:
    number_of_rows = number_of_rows + 1
    # print(row[4],row[5],row[6],row[7],row[8],row[9])
    list_from_lol.append(row[5])
    list_from_lol.append(row[6])
    list_from_lol.append(row[7])
    list_from_lol.append(row[8])
    list_from_lol.append(row[9])
    list_stars.append(row[10])
    list_stars.append(row[11])
    last_date.append(row[2])
    if number_of_rows > 5:
        break

print(last_date[0])
print(list_from_lol)
print(list_stars)

main_list = list(map(int,list_from_lol))
main_stars_list = list(map(int,list_stars))


lucky = sample(main_list,k=5)
luckyStars = sample(main_stars_list,k=2)



lucky.sort()
luckyStars.sort()

print("Random prediction for next Euromillions game")
print(lucky)
print(luckyStars)