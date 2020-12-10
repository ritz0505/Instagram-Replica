import os
import webapp2
import jinja2
from myuser import MyUser
from post import UserPost
from userprofile import UserProfile
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from blobcollection import BlobCollection
from uploadhandler import UploadHandler

from google.appengine.ext.blobstore import BlobKey
from google.appengine.api.images import get_serving_url
from google.appengine.api import images
from google.appengine.ext.webapp import blobstore_handlers

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class search(webapp2.RequestHandler):
    def get(self):
        user=users.get_current_user()
        result=""
        result=UserProfile.query().fetch()
        #self.response.write(ab)
        template_values={
        'result':result,
        'user':user.email()
        }
        template = JINJA_ENVIRONMENT.get_template('search_user_page.html')
        self.response.write(template.render(template_values))
