# Music Mixer

This application will supports following actions

1. Reads an input json file that contains list of users and songs. User element further contains a list of playlists
which is composed of a list of songs

2. Reads another json file that contains a list of change actions to be performed.
Supported change actions: 
    - add_song
    - add_playlist
    - remove_playlist

3. Creates a output json file that will contain music-data 
after changes in change json files were performed on mixtape json

### How to run this app

Use following command to execute this application

```./music_mixer mixtape.json change1.json output1.json ```

This command uses a self-container executable of music-mixer application.

#### Instructions to create self contained executable

1. Run ```pip install pyinstaller```
2. Open music-mixer code directory and run ```pyinstaller --onefile music-mixer.py```

Alternatively use following command to execute this application as python script

```python main.py mixtape.json change1.json output.json```

NOTE: python 3 must be installed if used python command is to execute this application