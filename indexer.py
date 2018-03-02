from octosearch.indexer import File
from instapaper import Instapaper
from io import StringIO


class Indexer(object):

    def index(self, conf):
        i = Instapaper(conf['instapaper_key'], conf['instapaper_secret'])
        i.login(conf['username'], conf['password'])

        for bookmark in i.bookmarks():
            yield InstapaperBookmark(bookmark)


class InstapaperBookmark(File):

    _bookmark = None

    def __init__(self, bookmark, encoding='utf-8'):
        self._bookmark = bookmark
        super(InstapaperBookmark, self).__init__(self._metadata(bookmark), encoding)

    def open_binary(self):
        return self.open_text()

    def open_text(self):
        return StringIO(self._bookmark.text)

    def _metadata(bookmark):
        return {
            'url': bookmark.url,
            'extension': 'html',
            'mimetype': 'text/html',
            'size': 0
        }
