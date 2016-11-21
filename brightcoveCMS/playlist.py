class Playlist(object):

    def __init__(self, client):
        self.client = client


    def get(self, id=""):
        if id != "":
            id = id + "/"
        return self.client.call_api("https://cms.api.brightcove.com/v1/accounts/" + self.client.account_id + "/playlists/" + id, "GET")


    def search(self, search):
        return self.client.call_api("https://cms.api.brightcove.com/v1/accounts/" + self.client.account_id + "/playlists/?q=" + search, "GET")

    def videos(self, id):
        playlist = self.client.call_api("https://cms.api.brightcove.com/v1/accounts/" + self.client.account_id + "/playlists/" + id, "GET")
        video_list = []
        for video in playlist["video_ids"]:
            video_list.append(self.client.call_api("https://cms.api.brightcove.com/v1/accounts/" + self.client.account_id + "/videos/" + str(video), "GET"))
        return video_list

