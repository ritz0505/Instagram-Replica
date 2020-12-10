from google.appengine.ext import blobstore
from google.appengine.ext import ndb
from google.appengine.ext.webapp import blobstore_handlers

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        upload = self.get_uploads()[0]
        blobinfo = blobstore.BlobInfo(upload.key())
        filename = blobinfo.filename
        collection_key = ndb.Key('BlobCollection', 1)
        collection = collection_key.get()
        collection.filenames.append(filename)
        collection.blobs.append(upload.key())
        collection.put()
        self.redirect('/')
