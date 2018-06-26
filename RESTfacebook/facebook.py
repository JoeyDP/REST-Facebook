
from RESTapi import API, GET, POST


class FacebookAPI(API):
    base_url = "https://api.facebook.com/"

    def __init__(self, token):
        self.token = token

    @GET
    def getPage(self, pageId):
        return Page

    @POST
    def addPage(self):
        return "page"

    @POST
    def updatePage(self, pageId):
        return "page"


from page import Page
