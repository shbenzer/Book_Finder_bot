import praw
import pdb
import re
import os

reddit = praw.Reddit('Book_Finder')

subreddit = reddit.subreddit("booksuggestions")

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))

for submission in subreddit.hot(limit=10):
    if submission.id not in posts_replied_to:
        if re.search("fantasy", submission.title):
            print("commented to: ", submission.id)
            submission.reply("RemindMe! 1 week")
            posts_replied_to.append(submission.id)
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
