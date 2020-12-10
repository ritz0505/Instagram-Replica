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
from showImage import showImage,checking
from uploadImage import Home,PhotoUploadHandler
from search_user import search
from followUnfollow import followUnfollow,unfolllowClass
from TimelineClass import TimeLineClass

from google.appengine.ext.blobstore import BlobKey
from google.appengine.api.images import get_serving_url
from google.appengine.api import images
from google.appengine.ext.webapp import blobstore_handlers

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type']='text/html'
        # URL that will contain a login or logout link
        # and also a string to represent this
        url=''
        url_string=''
        name=''
        welcome='Welcome back'
        # pull the current user from the request
        url=users.create_login_url(self.request.uri)
        url_string='login'
        user = users.get_current_user()
        var1=[]
        var2=[]
        var3=[]
        if user:
            url_string = 'logout'
            user_Details_Key = ndb.Key('MyUser', user.email())
            user_Details = user_Details_Key.get()
            if user_Details != None:
                user_Details.email_address = user.email()
                user_Details.put()
            else:
                user_Details = MyUser(id=user.email())
                user_Details.email_address = user.email()
                user_Details.put()

            ab=ndb.Key('UserProfile',user.email()).get()
            if ab != None:
                ab.email_address=user.email()
                ab.put()
            else:
                ab = UserProfile(id=user.email())
                ab.email_address = user.email()
                ab.put()

            upload_url = blobstore.create_upload_url('/PhotoUploadHandler')
            template_values={
            'upload_url':upload_url
            }
            template = JINJA_ENVIRONMENT.get_template('postupload.html')
            self.response.write(template.render(template_values))

        else:

            url=users.create_login_url(self.request.uri)
            url_string='login'

        template_values={
        'url' :url,
        'url_string' : url_string,
        'user' : user,
        'welcome':welcome,
        }
        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))

class showList(webapp2.RequestHandler):
    def get(self):
        value=[]
        a=ndb.Key('UserProfile',self.request.get('result')).get()
        #self.response.write(a)
        if a != None:
            value=a.followerslist
            if value == None:
                self.response.write("No Followers till now!!")
        else:
            self.response.write("No Followers till now..!!")
        template_values={
        'value':value
        }
        template = JINJA_ENVIRONMENT.get_template('displayList.html')
        self.response.write(template.render(template_values))

class showFollowingList(webapp2.RequestHandler):
    def get(self):
        value=[]
        a=ndb.Key('UserProfile',self.request.get('result')).get()
        #self.response.write(a)
        if a != None:
            value=a.followinglist
            if value == None:
                self.response.write("No Followers till now!!")
        else:
            self.response.write("You are not Following..!!")
        template_values={
        'value':value
        }
        template = JINJA_ENVIRONMENT.get_template('displayFollowingList.html')
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([('/', MainPage),('/Home',Home),('/PhotoUploadHandler', PhotoUploadHandler),('/showImage',showImage),
('/search',search),('/checking',checking),('/followUnfollow',followUnfollow),('/showList',showList),('/showFollowingList',showFollowingList),
('/TimeLineClass',TimeLineClass),('/unfolllowClass',unfolllowClass)], debug=True)
