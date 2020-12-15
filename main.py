import google_vision
import yelp_review_api
import json



yelp_id_search ='swingin-door-exchange-milwaukee'

def main():
    list_reiews = yelp_review_api.get_business_reviews(yelp_id_search)
    list_reiews_joy = google_vision.add_joy_likelihood(list_reiews)
    final_json = json.dumps(list_reiews_joy)
    print(final_json)
    with open("final_json.json", "w") as file:
        json.dump(final_json, file)


if __name__ == '__main__':
    main()
