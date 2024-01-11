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
import html
import bs4 

def remove_tags(message):
    parsed = bs4.BeautifulSoup(message, "html.parser").text
    print(parsed)
    return bs4.BeautifulSoup(message, "html.parser").text

def run():
    reference_id='2AfmfGFbe0A0WsTYm0SDTx'
    conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "2173464f0bmsh087f6a414d24270p11a1f5jsn1ae2008c92ce",
        'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
    }
    if Artist.objects.filter(api_id=reference_id).exists():
        print('Developer msg: data already exists in database')
    else:
        conn.request("GET", "/artists/?ids={reference_id}".format(
                    reference_id=reference_id), headers=headers)
        res = conn.getresponse()
        data = json.loads(res.read().decode('utf-8'))['artists'][0]

        reference = Artist(api_id=data['id'], name=data['name'], followers=data['followers']['total'], popularity=data['popularity'], image=data['images'][0]['url'] )
        reference.save()
        print(reference)
        conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")
        headers = {
            'X-RapidAPI-Key': "2173464f0bmsh087f6a414d24270p11a1f5jsn1ae2008c92ce",
            'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
        }
        conn.request("GET", "/artist_related/?id={reference_id}".format(reference_id=reference_id), headers=headers)
        res = conn.getresponse()
        data = json.loads(res.read().decode('utf-8'))
        print(data)
        
        bulk_list = []
        for artist in data['artists']:
            if Artist.objects.filter(api_id=artist['id']).exists():
                print("id already exists")
            else :   
                bulk_list.append(Artist(api_id=artist['id'], name=artist['name'], popularity=artist['popularity'], followers=artist['followers']['total'], image=artist['images'][0]['url'] ))
                
        print(bulk_list)
        bulk = Artist.objects.bulk_create(bulk_list)

        ## loop through artist records and get artist descriptions
        data = Artist.objects.all()
        print(type(data))
        conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")
        headers = {
            'X-RapidAPI-Key': "82ce6fe0f2msh1b1cfd285dbcc80p1b3260jsn6c515c923b86",
            'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
        }
        
        for i in data:
            id = str(i)
            print(i)
            conn.request("GET", "/artist_overview/?id={id}".format(
                    id=id), headers=headers)
            res = conn.getresponse()
            datas = json.loads(res.read().decode('utf-8'))
            print(datas)
            update = Artist.objects.get(api_id=id)
            text = html.unescape(datas['data']['artist']['profile']['biography']['text'])
            update.overview = remove_tags(text)
            update.save()
            print(text)
