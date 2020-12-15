from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

import google_vision

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install())

def website(searchName):
    url = "https://www.yelp.com/biz/{0}".format(searchName)
    driver.get(url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    reviews = soup.findAll('li', attrs={'class': 'lemon--li__373c0__1r9wz margin-b5__373c0__2ErL8 border-color--default__373c0__3-ifU'})
    list_reviews = []
    for review in reviews:
        dict = {}
        dict["name"] = review.find('a', attrs={'class': 'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE'}).get_text(strip=True)
        image = review.find('img', attrs={'class': 'lemon--img__373c0__3GQUb photo-box-img__373c0__35y5v'})['src']
        dict["image_url"] = image
        dict['joy_likelihood'] = google_vision.detect_faces_uri(image)
        list_reviews.append(dict)

    return list_reviews



