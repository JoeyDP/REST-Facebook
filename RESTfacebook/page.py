from RESTapi import GET, POST

import facebook


class Page(facebook.FacebookAPI):

    suffix = "page"

    def __init__(self, fb):
        super().__init__(fb)

    @GET(suffix="posts")
    def getPosts(self):
        return Post


from post import Post
