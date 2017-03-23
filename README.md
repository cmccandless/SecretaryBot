# SecretaryBot  
Forwards all received PMs to approved submitters in specified subreddit  

## Set up  
1. Create a new Reddit account for bot.  
2. Add bot account as full moderator on your subreddit  
3. Download bot.py and oauth.ini from https://github.com/cmccandless/SecretaryBot  
4. Replace contents of oauth.ini with this:  
``` INI  
[app]  
scope = identity,account,edit,flair,history,livemanage,modconfig,modflair,modlog,modothers,modposts,modself,modwiki,mysubreddits,privatemessages,read,report,save,submit,subscribe,vote,wikiedit,wikiread  
refreshable = True  
app_key = {APP_KEY}  
app_secret = {APP_SECRET}  
[server]  
server_mode = False  
url = 127.0.0.1  
port = 65010  
redirect_path = authorize_callback  
link_path = oauth  
[token]  
token = SRVMd0L4nvo9S056ctBZcz7s1mE  
refresh_token = 57919852-3PFMgkJWKYdPdP-RrAFVUMY9UrM
valid_until = 1465404401.6118257  
```
5. In bot.py, replace the following:  
| Line No | Before           | After                    |  
|---------|------------------|--------------------------|  
| 4       | {BOT_NAME}       | \<name of bot account\>    |  
| 5       | {SUBREDDIT_NAME} | \<name of your subreddit\> |  
6. If you intend to have the SecretaryBot always running, uncomment line 18 and increase the indent on lines 19+. If not, bot script will run once as-is, processing all unread messages in inbox.  
7. Make sure oauth.ini is in the same folder as bot.py and run bot.py  
