from bs4 import BeautifulSoup 
import requests
import datetime

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
    print(title, comic["src"], date)
    return [title, comic["src"], date]