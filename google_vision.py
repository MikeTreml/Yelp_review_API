import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/michaeltreml/Documents/g_vision.json"

def add_joy_likelihood(list_reiews):
    result_list = []
    for review in list_reiews:
        #send the user image to the face detetion grab a list of joy_lilelihoods. Number returned is based on each face detected
        joy_list = detect_faces_uri(review['user']['image_url'])
        # add a new variable of joy_list to the user Dictionary
        review['user']['likelihood'] = joy_list
        result_list.append(review)

    return result_list


def detect_faces_uri(uri):
    """Detects faces in the file located in Google Cloud Storage or the web."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri
    response = client.face_detection(image=image)
    faces = response.face_annotations
    #safe = response.safe_search_annotation
    list_joy_likelihood = []

    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    #add joylikelihood to a list to be returned.
    for face in faces:
        dict = {}
        dict["Joy"] = likelihood_name[face.joy_likelihood]
        dict["Sorrow"] = likelihood_name[face.sorrow_likelihood]
        dict["Anger"] = likelihood_name[face.anger_likelihood]
        dict["Surprise"] = likelihood_name[face.surprise_likelihood]
        dict["Under Exposed"] = likelihood_name[face.under_exposed_likelihood]
        dict["Headwear"] = likelihood_name[face.headwear_likelihood]
        dict["Blurred"] = likelihood_name[face.blurred_likelihood]
        list_joy_likelihood.append(dict)
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return list_joy_likelihood