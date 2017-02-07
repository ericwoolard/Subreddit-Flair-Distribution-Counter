REQUIREMENTS
------------
1. Python 3
2. Reddit account with Moderator privileges for a particular subreddit
3. Client ID and Secret to supply with the script

How to use
----------
1. Place the script in a new folder by itself. 
2. Edit lines 6, 7, 8, 10 and 13 with your Client-ID, Client Secret, password, username and subreddit name, respectively.
3. Start the script from the location that you saved the script to, with `python main.py`.
*TIP* - As a shortcut on Windows, you can open the folder containing the script and SHIFT + Right Click in the empty space,
then choose "Open command window here" if you don't want to have to CD to the correct directory, or if you're unsure how. 
Then, complete step #3.

INFO
----------
First and foremost, in order for this to work you *must* provide credentials that are tied to a Reddit account which has 
moderator access to the subreddit you run the script against. If you are unsure how to generate a Client-ID and Secret, 
login to the Reddit account to be authenticated with the script and go to Preferences>apps. Create a 'Personal Use Script'
and fill out the needed info. Since you will be registering a personal-use script, there won't be a need for a redirect-URI,
but Reddit still requires that you provide something here, so just 'http://localhost/reddit-oauth' will suffice. 

Due to the nature of methods related to Reddit flairs, this script may take a bit to complete depending on the size of the subreddit,
because it has to manually loop through each user that has selected a flair. At the time of writing this (Feb 6, 2017), the included
`flaircount.json` example was ran against r/GlobalOffensive and took roughly 7-8 minutes to complete, with a total of 97,354 users having
a flair selected out of a total subscriber count of 464,511. Don't be alarmed if you don't see anything progress right away.