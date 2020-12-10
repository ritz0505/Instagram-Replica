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

class showImage(webapp2.RequestHandler):
    def get(self):
        x=[]
        y=[]
        followerscount=0
        followingcount=0
        user = users.get_current_user()
        user_id=user.email()
        ab=ndb.Key('UserProfile',user.email()).get()
        z=ab.followerslist
        k=ab.followinglist
        for i in z:
            followerscount=followerscount+1
        for i in k:
            followingcount=followingcount+1
        value=ndb.Key('UserPost',user_id).get()

        if value == None:
            self.response.write("No post yet!")
            length=0
            template_values={
            'user':user,
            'length':length,
            'followerscount':followerscount,
            'followingcount':followingcount
            }
            template = JINJA_ENVIRONMENT.get_template('homepage.html')
            self.response.write(template.render(template_values))
        else:
            x=value.post_image_url
            length=len(value.post_image_url)
            y=value.post_content
            z=value.created_date
            #x.sort(reverse=True)
            #y.sort(reverse=True)
            #z.sort(reverse=True)

            template_values={
            'value':value,
            'x':x,
            'y':y,
            'z':z,
            'length':length,
            'user':user,
            'followerscount':followerscount,
            'followingcount':followingcount
            }
            template = JINJA_ENVIRONMENT.get_template('homepage.html')
            self.response.write(template.render(template_values))

class checking(webapp2.RequestHandler):
    def get(self):
        x=[]
        y=[]
        followerscount=0
        followingcount=0
        user = users.get_current_user()
        user_id=user.email()
        result=self.request.get('data')
        #self.response.write(result)
        if user.email()==self.request.get('data'):
            self.redirect('/showImage')
        else:
            result=self.request.get('data')
            ab=ndb.Key('UserProfile',result).get()
            if ab == None:
                self.response.write("There is no such user.")
            else:
                z=ab.followerslist
                k=ab.followinglist
                for i in z:
                    followerscount=followerscount+1
                for i in k:
                    followingcount=followingcount+1

                val1=[]
                val=ndb.Key('UserProfile',self.request.get('data')).get()
                if val != None:
                    val1=val.followerslist
                    #self.response.write(val1)
                    id=user.email()
                    #self.response.write(id)
                    length=0

                #self.response.write(result)
                value=ndb.Key('UserPost',result).get()
                if value != None:
                    x=value.post_image_url
                    length=len(value.post_image_url)
                    y=value.post_content
                    z=value.created_date
                    #x.sort(reverse=True)
                    #y.sort(reverse=True)
                    #z.sort(reverse=True)

                    template_values={
                    'value':value,
                    'val1':val1,
                    'id':id,
                    'x':x,
                    'y':y,
                    'z':z,
                    'length':length,
                    'user1':self.request.get('data'),
                    'user':user,
                    'result':result,
                    'followerscount':followerscount,
                    'followingcount':followingcount
                    }
                    template = JINJA_ENVIRONMENT.get_template('otherhomepage.html')
                    self.response.write(template.render(template_values))
                else:
                    self.response.write("No Post Yet!")
                    length=0
                    template_values={
                    'user':user,
                    'length':length,
                    'result':result,
                    'followerscount':followerscount,
                    'followingcount':followingcount
                    }
                    template = JINJA_ENVIRONMENT.get_template('otherhomepage.html')
                    self.response.write(template.render(template_values))
