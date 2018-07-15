from RESTapi import Entity, GET, StringProperty

from .post import Post
from .photo import Photo



@Entity
class Page(object):

    # parameters
    id = StringProperty()
    name = StringProperty(required=False)

    def __str__(self):
        return self.name

    @GET(suffix="posts", paginate=True)
    def getPosts(self):
        return Post

    @GET(suffix="photos", paginate=True)
    def getPhotos(self, type=None, fields=None):
        """ type can be: uploaded """
        return Photo


