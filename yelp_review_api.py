import requests
import api_keys
import google_vision

API_HOST = 'https://api.yelp.com'
BUSINESS_PATH = '/v3/businesses/'
REVIEWS_PATH = '/reviews'

# this function parses through a list of reviews to rune the joylikelihood
def add_joy_likelihood(list_reiews):
    result_list = []
    for review in list_reiews:
        #send the user image to the face detetion grab a list of joy_lilelihoods. Number returned is based on each face detected
        joy_list = google_vision.detect_faces_uri(review['user']['image_url'])
        # add a new variable of joy_list to the user Dictionary
        review['user']['likelihood'] = joy_list
        result_list.append(review)

    return result_list


# build the URL
def get_business_reviews(business_id):
    business_path = BUSINESS_PATH + business_id + REVIEWS_PATH
    return api_request(API_HOST, business_path)


def api_request(host, path):
    url = '{0}{1}'.format(host, path)
    headers = {
        'Authorization': 'Bearer %s' % api_keys.API_KEY,
    }
    # requests the json review info
    response = requests.request('GET', url, headers=headers)

    # saves the json reviews info
    reviews_data = response.json()

    # save the json as a list of Dictionaries
    list_reviews = reviews_data['reviews']

    return list_reviews

