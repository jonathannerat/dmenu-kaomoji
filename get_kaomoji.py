#!/usr/bin/env python

from bs4 import BeautifulSoup
from bs4.element import PageElement
import requests
import sys
import os


URL = "http://kaomoji.ru/en"


def main():
    kaocsv = sys.argv[1] if len(sys.argv) > 2 else None
    if not kaocsv:
        folder = os.getenv("XDG_CACHE_HOME")
        if folder is None:
            home = os.getenv("HOME")
            folder = home + "/.cache" if home is not None else ""
        kaocsv = folder + "/kaomojis.tsv"

    s = requests.Session()
    s.headers['user-agent'] = ''

    page = s.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    kaomojis = dict()

    for kaomoji_table in soup.find_all("table", class_="table_kaomoji"):
        name = kaomoji_table.find_parent("div").find_previous_sibling("h3").text

        if name == "Special":
            kaomojis[name] = get_kaomojis_special(kaomoji_table)
        else:
            kaomojis[name] = get_kaomojis(kaomoji_table)

    with open(kaocsv, "w") as fp:
        fp.write("id\tcategory\tkaomoji\tdescription\n")
        id = 0
        for category in kaomojis:
            for el in kaomojis[category]:
                kao = el[0]
                desc = el[1] if el[1] is not None else ""
                fp.write(f"{id}\t{category}\t{kao}\t{desc}\n")
                id += 1


def get_kaomojis(table: PageElement):
    ret = []

    for td in table.find_all("td"):
        kaomoji = td.text
        if kaomoji:
            ret.append((kaomoji, None))

    return ret


def get_kaomojis_special(table: PageElement):
    kaomojis = []
    kaomoji = None

    for i, td in enumerate(table.find_all("td")):
        if i % 2 == 0:
            kaomoji = td.text
        else:
            kaomojis.append((kaomoji, td.text))

    return kaomojis

if __name__ == "__main__":
    main()
