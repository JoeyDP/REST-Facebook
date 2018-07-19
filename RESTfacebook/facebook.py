from RESTapi import API, GET, POST, RequestPage, Paginator
from .page import Page
from .post import Post


@API(base_url='https://graph.facebook.com/')
class FacebookAPI(object):

    def __init__(self, token):
        self.token = token

    class Page(RequestPage):
        @property
        def data(self):
            return self.response.json()

        @property
        def items(self):
            return self.data.get('data', list())

        @property
        def itemCount(self):
            return None     # Facebook doesn't send total

        def getNextUrl(self):
            """ Return next url or raise StopIteration if end """
            paging = self.data.get("paging")
            if not paging:
                raise StopIteration()

            nextUrl = paging.get("next")
            if not nextUrl:
                raise StopIteration()
            return nextUrl

    def paginate(self, Type, response):
        firstPage = FacebookAPI.Page(response)
        for page in Paginator(firstPage):
            for item in page.items:
                yield Type(self, **item)


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


