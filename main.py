
import bacli
from RESTfacebook import FacebookAPI


bacli.setDescription("Test for FacebookAPI")

TOKEN = "token"


@bacli.command
def run():
    fb = FacebookAPI(TOKEN)
    page = fb.getPage(5)
    posts = page.getPosts()
    print(posts)

