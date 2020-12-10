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
from followUnfollow import followUnfollow

from google.appengine.ext.blobstore import BlobKey
from google.appengine.api.images import get_serving_url
from google.appengine.api import images
from google.appengine.ext.webapp import blobstore_handlers

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class TimeLineClass(webapp2.RequestHandler):
    def get(self):
        user=users.get_current_user()
        image = []
        post = []
        date = []
        x.append(user.email())
        value=ndb.Key('UserProfile',user.email()).get()
        userCount = 0
        while userCount < len(value.followinglist):
            x.append(value.followinglist[userCount])
            userCount = userCount + 1
        self.response.write(x)
        #value1=ndb.Key('UserPost',user.email()).get()
        #self.response.write(value1)
        #if value1 != None:
            #var1=value1.post_image_url
            #var1_caption=value1.post_content
            #var1_creation=value1.created_date
            #var1.sort(reverse=False)
            #var1_caption.sort(reverse=False)
            #var1_creation.sort(reverse=False)
            #image=var1
            #post=var1_caption
            #for i in range(0,len(value1.created_date)):
                #date.append(value1.created_date[i])
                #self.response.write("<br>")
                #self.response.write(date)
                #self.response.write("<br>")
        for i in x:
            self.response.write("<br>")
            self.response.write(i)
            #if i != None:
                #value2 = ndb.Key('UserPost', i).get()
                #if value2 != None:
                    #for i in range(0,len(value2.created_date)):
                        #date.append(value2.created_date[i])
        date.sort(reverse=True)
        #self.response.write(date)
        y=len(date)
        #self.response.write("<br>")
        for i in range(0,y): # Loop for number of post.
            #self.response.write("<br>")
            #self.response.write(date[i])
            found = 0
            for j in range(0,len(x)): # Loop for number of users.
                if found == 0:
                    data = ndb.Key('UserPost',x[j]).get()
                    #self.response.write("<br>")
                    #self.response.write(data.created_date)
                    for k in range(0,len(data.created_date)): # Loop for count of post each user have.
                        if data.created_date[k] == date[i]:
                            image.append(data.post_image_url[k])
                            post.append(data.post_content[k])
                            #self.response.write("<br>")
                            #self.response.write(image)
                            #self.response.write("<br>")
                            #self.response.write(post)
                            found = 1
                            break
                else:
                    break
        result1=image
        result2=y
        result3=post
        result4=date
        template_values={
        'result2':result2,
        'result1':result1,
        'result3':result3,
        'result4':result4
        }
        template = JINJA_ENVIRONMENT.get_template('TimeLine.html')
        self.response.write(template.render(template_values))
