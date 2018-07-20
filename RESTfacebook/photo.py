from RESTapi import Entity, GET, StringProperty, ListProperty, IntProperty


class ImageProperty(object):
    source = StringProperty()
    height = IntProperty()
    width = IntProperty()


@Entity
class Photo(object):

    # parameters
    id = StringProperty()
    images = ListProperty(ImageProperty, required=False)

    def __str__(self):
        return self.id
