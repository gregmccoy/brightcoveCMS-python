import requests
import json
from brightcoveCMS.video import Video
from brightcoveCMS.playlist import Playlist

class BrightcoveClient(object):

    def __init__(self, client_id, token, account_id):

        self.token = token
        self.client_id = client_id
        self.account_id = account_id
        self.headers = { "Authorization": "Bearer " + self.token }
        self.video = Video(self)
        self.playlist = Playlist(self)
        self.contenttype = "application/x-www-form-urlencoded"

    def get_oauth(self):
        headers = { "Content-Type": self.contenttype }
        response =requests.post("https://oauth.brightcove.com/v3/access_token",
                headers=headers,
                auth=(self.client_id , self.token),
                data="grant_type=client_credentials")

        return json.loads(response.text)["access_token"]


    def call_api(self, endpoint, method, data=None, files=None):
        self.headers = { "Authorization": "Bearer " + self.get_oauth() }
        if method == "POST":
            response = requests.post(endpoint, headers=self.headers, data=data, files=files)
        elif method == "PUT":
            response = requests.put(endpoint, headers=self.headers, data=data, files=files)
        elif method == "GET":
            response = requests.get(endpoint, headers=self.headers, data=data)
        elif method == "DELETE":
            response = requests.delete(endpoint, headers=self.headers, data=data)
        else:
            raise Exception("Method not supported")

        if response.status_code != 200 and response.status_code != 201:
            raise requests.ConnectionError("Expected status code 200, but got {}".format(response.status_code))
        return_data = ""
        return response.json()
