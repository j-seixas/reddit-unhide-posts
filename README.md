# reddit-unhide-posts

Usefull script to unhide reddit posts.

## Usage

* Go to your [app preferences](https://www.reddit.com/prefs/apps/). Click the "Create app" or "Create another app" button. Fill out the form like so:

    - *name*: Unhide App
    - *App type*: Choose the *script* option
    - *description*: You can leave this blank
    - *about url*: You can leave this blank
    - *redirect url*: http://www.example.com/unused/redirect/uri (We won't be using this as a redirect)
    `Note`: These examples will only work for script type apps, which will ONLY have access to accounts registered as "developers" of the app and require the application to know the user's password.

* Click on "Create"

* Create a `praw.ini` file with the following structure. 

```
[bot]
client_id=
client_secret=
password=
username=
user_agent='bot user agent'
```

* Add the corresponding values in front of it (no need to add single/double quotes aka ' or ") 

* Run with py `unhide-script.py`