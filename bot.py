import praw,OAuth2Util,time


botName='FILL_IN4'
subreddit='FILL_IN'
user_agent='Forwards all received PMs to approved submitters in /r/{}'.format(subreddit)

r = praw.Reddit(user_agent)
o = OAuth2Util.OAuth2Util(r)
o.refresh(force=True)

#UNCOMMENT TO REAUTHORIZE
# url=r.get_authorize_url('uniqueKey','identity',True)
# import webbrowser
# webbrowser.open(url)

#UNCOMMENT AND INCREASE INDENT FOR ALL LINES BELOW TO RUN CONTINUOUSLY
# while(True):
submitters=[]
for u in r.get_contributors(subreddit,limit=None):
	submitters.append(str(u))
for m in r.get_unread(limit=None):
	mark_as_read()
	print("a:{}s:{};m:{}".format(m.author.name,m.subject,m.message))
	for recipient in submitters:
		if recipient != m.author.name and recipient != botName:
			r.send_message(recipient, m.subject, m.message)
time.sleep(3600) #Wait for 10 minutes