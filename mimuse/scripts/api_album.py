# %%
import os
os.chdir("..")

# %%
import django
# from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mimuse.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

# %%
import json
import http.client

from songs.models import Album

# %%
conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "2173464f0bmsh087f6a414d24270p11a1f5jsn1ae2008c92ce",
    'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
}

conn.request("GET", "/albums/?ids=3IBcauSj5M2A6lTeffJzdv", headers=headers)

res = conn.getresponse()
data = json.loads(res.read().decode('utf-8'))

# %%
print(data)

# %%
bulk_list = []
for album in data['albums']:
    if Album.objects.filter(api_id=album['id']).exists():
        print("id already exists")
    else :   
        bulk_list.append(Album(api_id=album['id'], title=album['name'], release_date=album['release_date'], cover_image=album['images'][0]['url'] ))
        
print(bulk_list)
# %%
