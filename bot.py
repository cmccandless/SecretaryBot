import praw,OAuth2Util

subreddit=''
user_agent='Forwards all received PMs to approved submitters in /r/{}'.format(subreddit)

r = praw.Reddit(user_agent)
o = OAuth2Util.OAuth2Util(r)
o.refresh(force=True)

url=r.get_authorize_url('uniqueKey','identity',True)
import webbrowser
webbrowser.open(url)

while(True)
  for m in r.get_unread(limit=None):
    