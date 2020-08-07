# WWW Folder Explorer Home Assistant Addon

This addon allows you to explore the files and folders in /config/www using HTTP requests. 

The result is a JSON document of an array of strings(either full paths of files or folders).

### Example File and Folder Layout
<pre>
/config/www
|--- Music/
|    |--- Snoop Dogg/
|         |--- 1.mp3
|         |--- 2.mp3
|         |--- Cool Ringtone.mp3    
|    |--- Roxette/
|         |--- 1980hits.txt
|         |--- boo.wav
</pre>


# Syntax

### Directories under /config/www directory

**http://<HOME_ASSISTANT_IP>:8000/**

The example layout would return ["/Music"]


### Directories under a subdiretory


**http://<HOME_ASSISTANT_IP>:8000/directories/Music**

The example layout would return ["/Music/Snoop Dogg", "/Music/Roxette"]

### Files under a subdirectory

**http://<HOME_ASSISTANT_IP>:8000/files/Music/Roxette**

The example layout would return ["/local/Music/Roxette/1980hits.txt", "/local/Music/Roxette/boo.wav"]

### Filter files under a directory

**http://HOME_ASSISTANT_IP>:8000/files/Music/Snoop Dogg/filter/*.mp3**

The example layout would return ["/local/Music/Snoop Dogg/1.mp3", "/local/Music/Snoop Dogg/2.mp3", "/local/Music/Snoop Dogg/3.mp3"]

### Experimenting with glob

**http://HOME_ASSISTANT_IP>:8000/files/Music/filter/&ast;&ast;/*.wav**

The example layout would return ["/local/Music/Roxette/boo.wav"]








