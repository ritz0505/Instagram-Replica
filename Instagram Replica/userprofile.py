from google.appengine.ext import ndb
class UserProfile(ndb.Model):
    #email address of this User
    email_address = ndb.StringProperty()
    followerslist=ndb.StringProperty(repeated=True)
    followinglist=ndb.StringProperty(repeated=True)
