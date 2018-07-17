
from RESTapi import Entity, GET, POST, StringProperty



@Entity()
class Post(object):
    id = StringProperty(required=True)
    message = StringProperty(required=False)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self)
