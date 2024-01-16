**MiMuse** (Mini Music Base)

Members: Jieying Lin (Project Manager), Xinyi Ruan, Reya Miller

APIs Used:  Spotify - https://rapidapi.com/Glavier/api/spotify23 

Summary: 
Our code gets 5 recommended songs based on your favorite song, or based on our favorite song (Allergy), and then gets the information for the artists of those 5 recommended songs, and gets the albums and singles for those artists as well. With the songs being protected paid content (unfortunately), you can only play the songs' preview, and not the entirety of the songs.

Launch Codes:
- create requirements_env folder
- create virtual env in root folder --> activate virtual env
- in the project directory, go to mimuse/secrets_template.json -> copy the code and create file secrets.json and paste the code there and enter in your database information.
- run: 
  - pip install bs4
- Navigate to scripts/fill_database.py
- Inside the run function enter in your api keys in api_key and api_key2, and if you want you can replace seed_track with the track id of your favorite song -> can find the id in the search endpoint here https://rapidapi.com/Glavier/api/spotify23 
- run:
  - python manage.py runscript fill_database
  - python manage.py runserver
