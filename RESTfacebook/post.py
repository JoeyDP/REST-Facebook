
from RESTapi import GET, POST

import facebook


class Post(facebook.FacebookAPI):
    def __init__(self, fb):
        super().__init__(fb)
        self.text = ""

    def __str__(self):
        return self.text

