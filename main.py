import praw
import io
import json


r = praw.Reddit(client_id='CLIENT_ID', 
                client_secret='CLIENT_SECRET',
			    password='PASSWORD',
                user_agent='subreddit flair distribution counter by /u/zebradolphin5',
			    username='USER',
				)
#r.login(user, passw, disable_warning=True)
subreddit = r.subreddit("SUBREDDIT_NAME")

flairs = {}
for x in subreddit.flair(limit=None):
    flairName = x['flair_css_class']
    if not flairName in flairs:
        flairs[flairName] = 0

    flairs[flairName] += 1

sorted_flairs = sorted(flairs.items(), key=lambda x: x[1], reverse=True)
with io.open('flaircount.json', 'w+', encoding='utf-8') as f:
	f.write(str(json.dumps(sorted_flairs, ensure_ascii=False, indent=4, separators=(',', ': '))))    
