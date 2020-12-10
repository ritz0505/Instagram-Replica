from google.appengine.ext import ndb
from post import UserPost
class MyUser(ndb.Model):
    #email address of this User
    email_address = ndb.StringProperty()
    user_id=ndb.StringProperty()
    
    #post=ndb.StructuredProperty(UserPost,repeated=True)
