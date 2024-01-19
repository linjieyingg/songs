# %% [markdown]
# run once to fill database with artists
# %%
import os
os.chdir("..")
import django
# In case that we need it later
# from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'mimuse.settings')
# This is for async, in case we will see it later (maybe)
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
import json
import http.client
from artists.models import Artist
from songs.models import Song, Album
import html
import bs4 

def remove_tags(message):
    parsed = bs4.BeautifulSoup(message, "html.parser").text
    print(parsed)
    return bs4.BeautifulSoup(message, "html.parser").text

def run():
   
    api_key = '153c501680msh3dfee41a79a9befp16cbecjsn34ee5a30aea5'
    api_key2 = 'decc1ccd1emshec26a27a5b4d655p1dd505jsn708530cee011'
    seed_track = '2IMPPA9UZpqTnnVIy9lDHU'
    
    conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
    }
    
    #  get track recommendations
    conn.request("GET", "/recommendations/?limit=5&seed_tracks={seed_track}".format(seed_track=seed_track), headers=headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))
    song_list = list()
    print(data)
    for song in data['tracks']:
        if Song.objects.filter(api_id=song['id']).exists():
            continue
        else:
            if(song['album']['release_date_precision']=="day"):
                song_list.append(Song(api_id=song['id'], title = song['name'], preview_url= song['preview_url'], release_date= song['album']['release_date'], popularity=song['popularity'], recommended=True))
            else:
                song_list.append(Song(api_id=song['id'], title = song['name'], preview_url= song['preview_url'], popularity=song['popularity'], recommended=True))
    Song.objects.bulk_create(song_list)
    
    # get artists of recommended tracks 
    for song in data['tracks']:
        id = str(song['artists'][0]['id'])
        song_id = song['id']
        if Artist.objects.filter(api_id=id).exists():
            print('Developer msg: data already exists in database')
            continue
        else:
            conn.request("GET", "/artists/?ids={id}".format(
                            id=id), headers=headers)
            res = conn.getresponse()
            datas = json.loads(res.read().decode('utf-8'))['artists'][0]
            artist = Artist(api_id=id, name = datas['name'], popularity=datas['popularity'], image=datas['images'][0]['url'], followers=datas['followers']['total'])
            artist.save()
            song_id = song['id']
            this_song = Song.objects.get(api_id=song_id)
            artist.songs.add(this_song)
            artist.save()

    ## loop through artist records and get artist descriptions
    data = Artist.objects.all()
    print(type(data))    
    for i in data:
        id = str(i)
        try:
            conn.request("GET", "/artist_overview/?id={id}".format(
                        id=id), headers=headers)
            res = conn.getresponse()
            datas = json.loads(res.read().decode('utf-8'))
            update = Artist.objects.get(api_id=id)
            text = html.unescape(datas['data']['artist']['profile']['biography']['text'])
            update.overview = remove_tags(text)
            update.save()
        except:
            continue
        
    # get artist singles
    for artist in Artist.objects.all():
        api_id = artist.api_id
        conn.request("GET", "/artist_singles/?id={api_id}&limit=5".format(api_id=api_id), headers=headers)
        res = conn.getresponse()
        singles = json.loads(res.read().decode('utf-8'))['data']['artist']['discography']['singles']['items']
        for single in singles: 
            if single['releases']['items'][0]['type'] == 'SINGLE':
                id = single['releases']['items'][0]['id']
                if Song.objects.filter(api_id=id).exists():
                    continue
                else:
                    print(id)
                    try:
                        conn.request("GET", "/albums/?ids={id}".format(id=id), headers=headers)
                        res = conn.getresponse()
                        song_info = json.loads(res.read().decode("utf-8"))['albums'][0]['tracks']['items'][0]
                        song_record = Song.objects.update_or_create(api_id=song_info['id'],title=song_info['name'], popularity=song_info['popularity'], preview_url=song_info['preview_url'] )
                        song_record.save()
                        song_artist = Artist.objects.get(api_id=api_id)
                        song_artist.songs.add(song_record)
                        song_artist.save()
                    except:
                        continue
    
    # get artist albums
    data = Artist.objects.all()
    for i in data:
        artist_id = str(i)
        print(i)
        conn.request("GET", "/artist_albums/?id={artist_id}&limit=5".format(artist_id=artist_id), headers=headers)
        res = conn.getresponse()
        datas = json.loads(res.read().decode('utf-8'))
        print(datas)
        for album in datas['data']['artist']['discography']['albums']['items']:
            this = Album(api_id = album['releases']['items'][0]['id'])
            this.save()
            artist = Artist.objects.get(api_id=artist_id)
            artist.albums.add(this)
            artist.save()
            
    #get album info      
    for artist in Artist.objects.all():
        albums = Artist.albums.through.objects.filter(artist_id=artist.id)
        for album in albums:
            album_id = Album.objects.get(id=album.album_id).api_id
            artist_id = Artist.objects.get(id=album.artist_id).api_id
            try: 
                conn.request("GET", "/albums/?ids={album_id}".format(album_id=album_id), headers=headers)
                res = conn.getresponse()
                album_info = json.loads(res.read().decode('utf-8'))['albums'][0]
                this_album = Album.objects.filter(api_id=album_id)
                if(album_info['release_date_precision']=="day"):
                    this_album.update(title=album_info['name'], release_date=album_info['release_date'], cover_image=album_info['images'][0]['url'])
                else:
                    this_album.update(title=album_info['name'], cover_image=album_info['images'][0]['url'])
                this_artist = Artist.objects.get(api_id=artist_id)
                this_artist.albums.add(this_album.first())    
                this_artist.save()
            except:
                api_key = api_key2
                headers = {
                    'X-RapidAPI-Key': api_key,
                    'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
                }
                continue
    
    # get tracks in albums
    for album in Album.objects.all():
        album_id = album.api_id
        try:
            conn.request("GET", "/album_tracks/?id={album_id}&limit=5".format(album_id=album_id), headers=headers)
            res = conn.getresponse()
            album_tracks = json.loads(res.read().decode('utf-8'))['data']['album']['tracks']['items']
            for track in album_tracks:
                uri = track['track']['uri']
                id = uri.replace('spotify:track:', '')
                try: 
                    conn.request("GET", "/tracks/?ids={id}".format(id=id), headers=headers)
                    res = conn.getresponse()
                    track_info = json.loads(res.read().decode('utf-8'))['tracks'][0]
                    if Song.objects.filter(api_id=id).exists():
                        continue
                    else:
                        Song.objects.update_or_create(api_id=id, album_id=album, title=track_info['name'], popularity=track_info['popularity'], preview_url = track_info['preview_url'], release_date=album.release_date)
                        song= Song.objects.get(api_id=id)
                        artist = Artist.objects.get(api_id=track_info['artists'][0]['id'])
                        artist.songs.add(song)
                        artist.save()
                except:
                    print("TOO MANY SONGS API CANNOT HANDLE")
                    api_key = api_key2
                    headers = {
                        'X-RapidAPI-Key': api_key,
                        'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
                    }
                    continue
        except:
            print("API LIMIT")
            api_key = api_key2
            headers = {
                'X-RapidAPI-Key': api_key,
                'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
            }
            continue
    print('done filling database')
# %%
