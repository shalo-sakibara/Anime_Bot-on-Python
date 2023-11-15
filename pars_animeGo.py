from bs4 import BeautifulSoup
import requests
import datetime

data = datetime.date.today()
date_day = data.day


def new_anime_from_AnimeGo():
    site = 'https://animego.org/'
    r = requests.get(site)
    html = BeautifulSoup(r.content, "html.parser")
    new_anime = html.find(
        "div", id=f"slide-toggle-1")

    arr = []
    for el in new_anime:
        name_anime = el.find("span").text
        ref = el.get('onclick')
        ref = site[:-1] + ref[ref.index("=")+2:-1]
        ozvych = el.text[el.text.index("(")+1: el.text.index(")")]
        seria = el.text.replace(name_anime, "")
        seria = seria.replace(ozvych, '')
        string = f'{name_anime} "{seria[0:-2]}" {ozvych}  {ref}'
        arr.append(string)
    return arr
