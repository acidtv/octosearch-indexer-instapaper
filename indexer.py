from octosearch.indexer import File
from instapaper import Instapaper
import io


class Indexer(object):

    def index(self, conf):
        i = Instapaper(conf['instapaper_key'], conf['instapaper_secret'])
        i.login(conf['username'], conf['password'])

        for bookmark in i.bookmarks(limit=99999):
            yield InstapaperBookmark(bookmark)


class InstapaperBookmark(File):

    _bookmark = None

    def __init__(self, bookmark):
        super().__init__()
        self._bookmark = bookmark
        self._set_properties(bookmark)

    def open(self):
        return io.BytesIO(self._bookmark.text.encode('utf-8'))

    def _set_properties(self, bookmark):
        self.title = bookmark.title
        self.url = bookmark.url
        self.mimetype = 'text/html'
        self.size = 0
        self.modified = bookmark.time
