from RESTapi import API, GET, POST
from .page import Page
from .post import Post


@API(base_url='https://graph.facebook.com/')
class FacebookAPI(object):

    def __init__(self, token):
        self.token = token

    def paginate(self, Type, **data):
        #TODO: do actual pagination
        elements = data['data']
        result = [Type(self, **elem) for elem in elements]
        return result

    @GET
    def getPage(self, pageId):
        return Page

    @GET
    def getPost(self, postId):
        return Post

    @POST
    def addPage(self):
        return "page"

    @POST
    def updatePage(self, pageId):
        return "page"


