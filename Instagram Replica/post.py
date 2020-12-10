from google.appengine.ext import ndb
class UserPost(ndb.Model):
    #login_address=ndb.StringProperty()
    creator_address=ndb.StringProperty()
    post_content = ndb.StringProperty(repeated=True)
    #post_content_lower = ndb.StringProperty()
    post_image = ndb.BlobKeyProperty(repeated=True)
    post_image_url = ndb.StringProperty(repeated=True)
    created_date = ndb.StringProperty(repeated=True)
    updated_date = ndb.StringProperty()
