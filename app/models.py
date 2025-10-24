
class LibraryItem:

    def __init__(self, name, url, mbid):
        self.name = name
        self.url = url
        self.mbid = mbid

class Album(LibraryItem):

    def __init__(self, name, url, mbid, artistName, imageURL):
        super().__init__(name, url, mbid)

        self.artistName = artistName
        self.imageURL = imageURL

        self.eloScore = 1500