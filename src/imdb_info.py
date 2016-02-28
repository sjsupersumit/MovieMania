import requests
from bs4 import BeautifulSoup
import urllib2
import logging
import sys
import re

IMDB_BASE_URL = "http://www.imdb.com/"

def main():
    logging.basicConfig(filename="/Users/sumit.jha/Documents/personal/SubtitleDownloader/imdb.log", level=logging.INFO)
    logging.info("Starting with the arguments...." + str(sys.argv))

    if len(sys.argv) == 1:
        print "No file Name is given. Exiting....!!!"
        sys.exit(1)

    for cnt,name in enumerate(sys.argv):
        if cnt != 0:
            print extract_info(name)


def extract_info(name):
    if name.strip():
        name = re.sub("\s+", "+", name)
        find_url = IMDB_BASE_URL + "find?ref_=nv_sr_fn&s=all&q=" + name
        page = urllib2.urlopen(find_url)
        soup = BeautifulSoup(page.read(), "lxml")
        first_link = soup.find("table", {"class": "findList"}).tr.find("td", {"class": "result_text"}).a.get('href')
        info_page_url = IMDB_BASE_URL + first_link
        info_page = urllib2.urlopen(info_page_url)
        soup = BeautifulSoup(info_page.read(), "lxml")
        movie_info = soup.find("div", {"class":"title_wrapper"}).h1
        movie_name = movie_info.contents[0]
        movie_year = movie_info.find("span").find("a").contents[0]
        movie_rating = soup.find("div", {"class": "ratingValue"}).span.contents[0]
        movie_summary = soup.find("div", {"class": "summary_text"}).contents[0].strip()
        movie_story_line = soup.find("div", {"class": "article", "id":"titleStoryLine"}).find("p").contents[0]
        movie_review = soup.find("div", {"class": "user-comments"}).find("p", {"itemprop":"reviewBody"}).contents[0]

        final_output = "\n---------------------------\n" + movie_name + (movie_year) + " \n ----Ratings----\n" + movie_rating + "\n" \
                        "\n----SUMMARY---\n" + movie_summary + "\n\n-------STORY_LINE------------\n" + movie_story_line + "\n\n -------------USER REVIEW-----\n\n" + movie_review
        logging.info("\n\n" + final_output + "\n\n")
        print final_output.encode("utf-8")

if __name__ == '__main__':
    main()
