
from RESTapi import Entity, GET, POST, StringProperty



@Entity()
class Post(object):
    message = StringProperty(required=False)

    def __str__(self):
        return self.message

    def __repr__(self):
        return str(self)
