from calendar import month
from bs4 import BeautifulSoup
import requests
from database import engine, SessionLocal
import models
import datetime

db = SessionLocal()
models.Base.metadata.create_all(bind=engine)

def todayComic():
    url = "https://www.gocomics.com/garfield/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    count = 0
    comic = soup.find_all("img")[3]
    print(comic["src"])
    today = datetime.date.today().strftime("%d/%m/%Y")
    title = "Garfield on " + today
    date = today
    comic = models.Comic(title=title, url=comic["src"], date=date)
    db.add(comic)
    db.commit()


def addComics():
    # today's date
    today = datetime.date.today().strftime("%Y/%m/%d")
    # date start
    garfield_date = datetime.datetime(1978, 6, 19).strftime("%Y/%m/%d")
    # go to next day
    url = "http://pt.jikos.cz/garfield/"
    month = 7
    year = 1978
    today_year = datetime.date.today().year
    today_month = datetime.date.today().month
    while ((year <= 2022)):
        # remove day from garfield_date
        if (year == today_year and month == today_month):
            print("I AM HERE")
            break
        garfield_date_suffix = str(year) + "/" + str(month) + "/"
        month_url = url + garfield_date_suffix
        print(month_url)
        r = requests.get(month_url)
        soup = BeautifulSoup(r.text, "html.parser")
        # get all the days
        # find table
        table = soup.find_all("table")
        # find all tr
        trs = table[0].find_all("tr")
        for tr in trs:
            title = "Garfield on " + tr.find("td").text
            comic_url = tr.find("img")["src"]
            date = tr.find("td").text
            print(title, comic_url)
            # add to database
            comic = models.Comic(title=title, url=comic_url, date=date)
            db.add(comic)
            db.commit()
        # go to next day
        month = month + 1
        if month > 12:
            month = 1
            year = year + 1
            print(month)
            print(year)
addComics()