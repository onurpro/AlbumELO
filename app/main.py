###


###

import random

from .api_client import getAlbums

def generateAlbum(albumListLength):
    return random.randint(0, albumListLength-1)

albumList = getAlbums("onur_pro")

albumListLength = len(albumList)

print(albumList[generateAlbum(albumListLength)].name)