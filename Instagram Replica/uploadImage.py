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
from datetime import datetime

from google.appengine.ext.blobstore import BlobKey
from google.appengine.api.images import get_serving_url
from google.appengine.api import images
from google.appengine.ext.webapp import blobstore_handlers

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class Home(webapp2.RequestHandler):
    def get(self):
        upload_url = blobstore.create_upload_url('/PhotoUploadHandler')
        ab=UserPost().fetch()
        template_values={
        'ab':ab,
        'upload_url':upload_url
        }
        template = JINJA_ENVIRONMENT.get_template('postupload.html')
        self.response.write(template.render(template_values))

class PhotoUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        user = users.get_current_user()
        createddate=datetime.now()
        date=createddate.strftime("%Y-%m-%d %H:%M:%S")
        upload = self.get_uploads()[0]
        post_content = self.request.get('post_content')
        post_model = ndb.Key('UserPost',user.email()).get()
        if post_model == None:
            post_model = UserPost(id=user.email())
        post_model.post_content.append(post_content)
        post_model.created_date.append(date)
        img_url = ''
        blobinfo = blobstore.BlobInfo(upload.key())
        filename = blobinfo.filename
        post_model.post_image.append(upload.key())
        post_model.creator_address=user.email()
        img_url = get_serving_url(upload.key())
        post_model.post_image_url.append(get_serving_url(upload.key()))
        #post_model.append(upload.key())
        post_model.put()
        self.redirect('/')
