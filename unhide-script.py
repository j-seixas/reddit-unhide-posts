import praw

print('Insert your reddit username: ')
nickname = input()
print(nickname)
print('Insert your reddit password: ')
passw = input()
print(passw)

reddit = praw.Reddit(password='1guiwevlfo00esyy', user_agent='testscript by /u/fakebot3', username='fakebot3')