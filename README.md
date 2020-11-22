# Book_Finder_bot
a reddit bot that searches a given subreddit's hot page for a keyword, and if found, leaves a comment that interfaces with the RemindMe! bot. Stores posts it comments on to prevent spam.

## Running

### install praw
```
pip install praw
```

### create a bot on reddit
```
https://www.reddit.com/prefs/apps/
```

### add configuration information to praw.ini file
```
client_id=
client_secret=
password=
username=
user_agent=
```

### move praw.ini file into your repo (I have not included mine in this repo as it contains account information)

### run script
```
python3 Book_Finder.py
```
