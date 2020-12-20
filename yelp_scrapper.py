from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

import google_vision

def get_soup(url):
    # paramerters for the headless broswer
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')

    # downloads the newest webdriver to a give access tot the chrome browser.
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    # parses the beautiful soup data with xml.
    soup = BeautifulSoup(driver.page_source, 'lxml')

    return soup

def website(searchName):
    soup = get_soup("https://www.yelp.com/biz/{0}".format(searchName))

    # saves the list of reviews
    reviews = soup.findAll('li', attrs={'class': 'lemon--li__373c0__1r9wz margin-b5__373c0__2ErL8 border-color--default__373c0__3-ifU'})

    # the business name
    business_name = soup.find('h1', attrs={'class': 'lemon--h1__373c0__2ZHSL heading--h1__373c0__dvYgw undefined heading--inline__373c0__10ozy'}).get_text(strip=True)
    list_reviews = []

    # loop through the list of reviews on at a time
    for review in reviews:
        dict = {}
        dict["name"] = review.find('a', attrs={'class': 'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE'}).get_text(strip=True)
        image = review.find('img', attrs={'class': 'lemon--img__373c0__3GQUb photo-box-img__373c0__35y5v'})['src']
        dict["review_content"] = review.find('span', attrs={'class': 'lemon--span__373c0__3997G raw__373c0__3rcx7'}).get_text(strip=True)
        dict["star_rating"] = review.find('div', attrs={'class': 'i-stars__373c0__1T6rz'})['aria-label']
        dict["location"] = review.find('span', attrs={'class': 'lemon--span__373c0__3997G text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa-'}).get_text(strip=True)
        dict["place_name"] = business_name
        dict["image_url"] = image
        dict['likelihood'] = google_vision.detect_faces_uri(image)
        list_reviews.append(dict)

    return list_reviews



