
import bacli
from RESTfacebook import FacebookAPI


bacli.setDescription("Test for FacebookAPI")

TOKEN = ""


@bacli.command
def run():
    fb = FacebookAPI(TOKEN)
    page = fb.getPage(942723909080518)
    print("page", page)
    posts = page.getPosts()
    print("posts", posts)

