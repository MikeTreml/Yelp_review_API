import requests
import api_keys


API_HOST = 'https://api.yelp.com'
BUSINESS_PATH = '/v3/businesses/'
REVIEWS_PATH = '/reviews'

# build the URL
def get_business_reviews(business_id):
    business_path = BUSINESS_PATH + business_id + REVIEWS_PATH
    return api_request(API_HOST, business_path)


def api_request(host, path):
    url = '{0}{1}'.format(host, path)
    headers = {
        'Authorization': 'Bearer %s' % api_keys.API_KEY,
    }
    response = requests.request('GET', url, headers=headers)
    # grab the json review info
    reviews_data = response.json()
    # save the json as a list of Dictionaries
    list_reviews = reviews_data['reviews']
    return list_reviews

