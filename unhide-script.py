import praw
import time

days = input("Unhide within how many days?")

reddit = praw.Reddit('bot')

date = int(time.time()) - (int(days) * 24 * 3600)
unhidden = 0
lastUnhidden = 1
hidden = None 

while lastUnhidden != unhidden:
    lastUnhidden = unhidden
    hidden = reddit.user.me().hidden(limit=1000)

    for post in hidden:
        if int(post.created_utc) < date :
            print("Unhiding ", post.title)
            post.unhide()
            unhidden += 1
print("Successfully unhidden ", unhidden, " posts")