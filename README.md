# MiMuse (Mini Music Base)

## Members 
Jieying Lin (Project Manager)
Xinyi Ruan
Reya Miller

## API used in this project  
Spotify - https://rapidapi.com/Glavier/api/spotify23 

## Project Summary
Our code gets 5 recommended songs based on your favorite song, or based on our favorite song (Allergy), and then gets the information for the artists of those 5 recommended songs, and gets the albums and singles for those artists as well. With the songs being protected paid content (unfortunately), you can only play the songs' preview, and not the entirety of the songs.

## Project Launch Code
In order to access this project, following these directions:

#### Clone the project
1. Open up the project on GitHub 
2. Under <> Code then SSH, copy the URL
3. In your terminal, enter `git clone [copied_url]`
4. Open up the project in your preferred IDE

#### Set Up Python Environment
1. Make sure you're inside the project folder
2. `pyenv local 3.11.5`
3. `python -m venv env_3.11.5`
4. `source env_3.11.5/bin/activate`

#### Set Up Environment Packages
1. Run:
   ```
   pip install --upgrade pip-tools pip setuptools wheel
   pip-compile --upgrade --generate-hashes --output-file requirements_env/main.txt requirements_env/main.in
   pip-compile --upgrade --generate-hashes --output-file requirements_env/dev.txt requirements_env/dev.in  
   pip-sync requirements_env/main.txt requirements_env/dev.txt
   ```
   
#### Connecting to Local Database
1. Locate the file called `secrets_template.json` in the `project_folder/final/` directory
2. Make a copy of the file and name it to `secrets.json`
3. Replace the data with your own database information

#### Running the Project
1. Navigate to scripts/fill_database.py
2. Inside the run function enter in your api keys in api_key and api_key2, and if you want you can replace seed_track with the track id of your favorite song -> can find the id in the search endpoint here https://rapidapi.com/Glavier/api/spotify23 
3. Move into the directory on the same level as the file `manage.py`
4. Make sure you migrate your changes before running anything with the command `python manage.py makemigrations` then `python manage.py migrate`
5. Run the command `python manage.py runserver`
6. Open the server in your browser
