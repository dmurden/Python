from plexapi.server import PlexServer
from plexapi.photo import Photoalbum
from plexapi.photo import Photo
baseurl = 'http://192.168.1.20:32400'
token = '4VBoe83uqDaxqwj66oaq'
plex = PlexServer(baseurl, token)
#photo = Photo.fetchItem(96031, Photo)
photoalbum = plex.fetchItem(96029,Photoalbum)
print(photoalbum.title)
photo = plex.fetchItem(100303, Photo)
print(photo.year)
test = {'year.value': '2012', 'year.locked':'1'}
photo.edit(**test)

#photosection = plex.library.section('Photos')
#for section in photosection.all():
#    print(section)

#movies = plex.library.section('Movies')
#test = {'title.value': 'hello', 'movie.title.locked': 1}
#for movie in movies.search(title='harry'):
    #print(movie.title)
    #movie.edit(**test)
    #movie.reload()
    #print(movie.title)
    #break
