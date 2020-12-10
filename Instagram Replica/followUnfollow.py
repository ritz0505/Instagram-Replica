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

class followUnfollow(webapp2.RequestHandler):
    def get(self):
        user=users.get_current_user()
        result=self.request.get('result')
        self.response.write(result)
        button=self.request.get('follow')
        self.response.write(button)
        ab=ndb.Key('UserProfile',user.email()).get()
        ab.followinglist.append(result)
        ab.put()
        ab1=ndb.Key('UserProfile',result).get()
        ab1.followerslist.append(user.email())
        ab1.put()
        self.redirect('/')


class unfolllowClass(webapp2.RequestHandler):
    def get(self):
        user=users.get_current_user()
        result=self.request.get('result')
        self.response.write(result)
        button=self.request.get('follow')
        self.response.write(button)
        ab=ndb.Key('UserProfile',user.email()).get()
        ab.followinglist.remove(result)
        ab.put()
        ab1=ndb.Key('UserProfile',result).get()
        ab1.followerslist.remove(user.email())
        ab1.put()
        self.redirect('/')
