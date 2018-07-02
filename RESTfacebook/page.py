from RESTapi import Entity, GET, POST, StringProperty, ListProperty

from post import Post




@Entity
class Page(object):

    # parameters
    id = StringProperty()
    name = StringProperty()

    def __str__(self):
        return self.name

    @GET(suffix="posts", paginate=True)
    def getPosts(self):
        return Post


