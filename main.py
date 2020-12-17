import google_vision
import yelp_review_api
import json

import yelp_scrapper



def json_file_create(data, file_name):
    with open(file_name, "w") as file:
        file.write(data)

def yelp_api_run(yelp_id_search):
    list_reiews = yelp_review_api.get_business_reviews(yelp_id_search)
    list_reiews_joy = google_vision.add_joy_likelihood(list_reiews)
    final_json = json.dumps(list_reiews_joy, indent=4)
    print(final_json)
    json_file_create(final_json, "json\API_json.json")


def yelp_scrapper_run(yelp_id_search):
    scrapped_json = json.dumps(yelp_scrapper.website(yelp_id_search), indent=4)
    print(scrapped_json)
    json_file_create(scrapped_json, "json\scrapped_json.json")


def main():
    yelp_id_search = 'swingin-door-exchange-milwaukee'
    yelp_api_run(yelp_id_search)
    yelp_scrapper_run(yelp_id_search)


if __name__ == '__main__':
    main()
