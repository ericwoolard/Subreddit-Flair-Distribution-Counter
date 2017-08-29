REQUIREMENTS
------------
1. Python 3
2. [Praw 4.x](https://praw.readthedocs.io/en/latest/)
3. Reddit account with Moderator privileges for a subreddit
4. Client ID and Secret to supply with the script

How to use
----------
1. Place the script and cfg file in a new folder by itself.
2. Edit lines 3-7 of the cfg file with your Client-ID, Client Secret, password, username and subreddit name, respectively (**DON'T** wrap these credentials in quotes like a typical string).
3. Start the script *from within the folder you saved it to* by entering `python main.py` in CMD. 
**Note** - From your command prompt, you will need to `cd` (Change Directory command) into the directory where the script is saved. See the tip below if you don't know how to do this.

**TIP** - As a shortcut on Windows, you can open the folder containing the script and SHIFT + Right Click in the empty space,
then choose "Open command window here" if you don't want to have to CD to the correct directory, or if you're unsure how. 
Then, complete step #3.

INFO
----------
First and foremost, in order for this to work you *must* provide credentials that are tied to a Reddit account which has 
moderator access to the subreddit you run the script against. If you are unsure how to generate a Client-ID and Secret, 
login to the Reddit account to be authenticated with the script and go to Preferences>apps. Create a 'Personal Use Script'
and fill out the needed info. Since you will be registering a personal-use script, there won't be a need for a redirect-URI,
but Reddit still requires that you provide something here, so just 'http://localhost/reddit-oauth' will suffice. 

Due to the nature of the Reddit API, this script may take a bit to complete depending on the size of the subreddit,
because it has to manually loop through each user that has selected a flair. At the time of writing this (Feb 6, 2017), the included
`flaircount.json` example was ran against r/GlobalOffensive and took roughly 7-8 minutes to complete, with a total of 97,354 users having
a flair selected out of a total subscriber count of 464,511. Don't be alarmed if you don't see anything progress right away.

You can receive more verbose output by changing line 22 of the cfg file from "INFO" to "DEBUG".

Once the script completes, it will dump all of the stats to a JSON file in the same folder as the script itself named
`flaircount.json`. You can configure this filename on line 22 of the cfg file.

Common Errors
---------------
If you have both Python 2 and 3 installed on your system and receive errors when starting the script with `python main.py`, 
run the script with `python3 main.py` instead. This can be the case if you only have one environment variable set for python 
on your system (pointing to python 2), but have both versions installed. If you have to do it this way, you'll also need to 
make sure you actually installed praw for python3 instead of 2. You can check which version its tied to with `pip show praw`.
If it got tossed in with python2, install it for python3 with `pip3 install praw`.

**HTTP 401 error (unauthorized)** - 
  * This typically means there's an issue with the Client-ID you supplied. When you go to preferences>apps and click 'edit' 
  under the application you created, your Client-ID will be [here](https://i.imgur.com/n3dKYcF.png)

**OAuthException: unauthorized_client error processing request (Only script apps may use password auth)** - 
  * If you see this error, it's likely you didn't create the application correctly under preferences>apps. When setting this up,
  there are 3 options to choose from: web app, installed app, script. You *must* register the app as a **script app** for this 
  to work. [Example](https://i.imgur.com/ZV30NVg.png)