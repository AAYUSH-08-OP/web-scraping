from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
time.sleep(10)

def scraper():
    header = ["name", "distance", "mass", "radius"]
    star_data = []
    for i in range(0, 100):
        soup = BeautifulSoup("html.parser")
        for ul_tag in soup.find_all("ul", attrs = {"class", "Proper name"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tags in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tags.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tags.contents[0])
                    except:
                        temp_list.append("")
            star_data.append(temp_list)
        ##browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scraper.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(header)
        csvwriter.writerow(star_data)
scraper()