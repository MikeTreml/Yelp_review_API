import google_vision
import yelp_review_api
import json



yelp_id_search ='swingin-door-exchange-milwaukee'

def main():
    list_reiews = yelp_review_api.get_business_reviews(yelp_id_search)


if __name__ == '__main__':
    main()
