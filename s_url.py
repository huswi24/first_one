import requests
from bs4 import BeautifulSoup
import re
from collections import OrderedDict
import pprint
import time

##################################################
#食べログより各ジャンルに応じた、指定した店舗情報を取得する#
##################################################


class Tabelog:

    def __init__(self,base_url):
        self.__regexcomp = re.compile(r'\n|\s')
        counter = 1
        while True:
            list_url = base_url + str(counter) + "/"
            if self.scrape_list(list_url) != True:
                break
            counter += 1

        return


    def scrape_list(self,list_url):
        r = requests.get(list_url)
        if r.status_code != requests.codes.ok:
            return False

        soup = BeautifulSoup(r.content,"lxml")
        soup_a_list = soup.find_all('a',class_ = "list-rst__rst-name-target")
        if len(soup_a_list) == 0:
            return False
        for soup_a in soup_a_list:
            item_url = soup_a.get("href")
            self.scrape_item(item_url)

        return True

    def scrape_item(self,item_url):
        r = requests.get(item_url)
        if r.status_code != requests.codes.ok:
            print(f"error:not found{item_url}")
            return
        soup = BeautifulSoup(r.content,'lxml')
        soup_table = soup.find("table",class_="rstinfo-table__table")
        self.scrape_info(soup_table)

        return

    def scrape_info(self,soup_table):
        restaurant_dic =  {}
        rs_name = []
        soup_tr_list = soup_table.find_all('tr')
        num = 1
        for soup_tr in soup_tr_list:
            if soup_tr.th.string in {"店名", "住所","ジャンル","予算","営業時間"}:
                item = self.__regexcomp.sub('',soup_tr.td.get_text())
                itemheader = '' if (soup_tr.thstring == '店名') else '\t'
                print(itemheader+str(num),item)
                rs_name.append(item)
            num += 1

        time.sleep(3)
        print('\t'+'--------------')
        return



italian = "https://tabelog.com/tokyo/rstLst/italian/"
franch = "https://tabelog.com/tokyo/rstLst/french/"
western = "https://tabelog.com/tokyo/rstLst/RC02/"#洋食・西洋料理のお店

print("1 : イタリアン\n2 : フレンチ\n3 : 西洋料理")

while True:
    target_genre = input('番号を入力してください : ')
    if target_genre == "1":
        target_genre = italian
        print('イタリアン料理を取得します')
        break
    elif target_genre == "2":
        target_genre = franch
        print('フレンチ料理を取得します')
        break
    elif target_genre == "3":
        target_genre = western
        print('西洋料理を取得します')
        break
    else :
        print("1〜3で入力してください。")

Tabelog(target_genre)
