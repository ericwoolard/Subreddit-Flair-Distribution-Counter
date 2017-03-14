import praw
import praw.exceptions
import prawcore.exceptions
import io
import json
import logging.config
import configparser
import os
import sys
import time


config = configparser.ConfigParser()
configfile_path = os.path.abspath(os.path.dirname(sys.argv[0]))
configfile_path = os.path.join(configfile_path, 'Subreddit-Flair-Distribution-Counter.cfg')
config.read(configfile_path)
logging.config.fileConfig(configfile_path)

while True:
    try:
        r = praw.Reddit(client_id=config['reddit']['client_id'],
                        client_secret=config['reddit']['client_secret'],
                        user_agent=config['reddit']['user_agent'],
                        username=config['reddit']['username'],
                        password=config['reddit']['password'])
        logging.info('Logged in as {0}.'.format(r.user.me()))
        break
    except prawcore.OAuthException as e:
        logging.error('OAuth Error: {0}'.format(e.description))
        logging.info('If you received an \'invalid_grant\' error, make sure the user and pass are correct \n'
                     'and that they are the same as the account you registered the script with.')
        logging.info('Retrying in 20 seconds, or CTRL+C to stop the script...')
        time.sleep(20)
    except KeyboardInterrupt:
        logging.info('Shutting down due to keyboard interrupt.')
        exit()
    except prawcore.exceptions.ResponseException as e:
        if e.response.status_code == 401:
            logging.error('HTTP 401: Ensure authentication credentials are configured \n'
                          'in Subreddit-Flair-Distribution-Counter.cfg')
        else:
            logging.error('Error: {0}'.format(e))
        exit()
    except Exception as e:
        logging.error('Error: {0}'.format(e))
        exit()

subreddit = r.subreddit(config['reddit']['subreddit'])

flairs = {}

logging.debug('Counting flairs...')
for flair in subreddit.flair(limit=None):
    flairName = flair['flair_css_class']
    if flairName not in flairs:
        flairs[flairName] = 0
        logging.debug('Flair added: {0}'.format(flairName))

    flairs[flairName] += 1
    logging.debug('Flair counted: {0}'.format(flairName))

logging.info('Sorting flairs...')
sorted_flairs = sorted(flairs.items(), key=lambda x: x[1], reverse=True)
logging.info('Writing flairs...')
with io.open(config['output']['filename'], 'w+', encoding='utf-8') as f:
    f.write(str(json.dumps(sorted_flairs, ensure_ascii=False, indent=4, separators=(',', ': '))))
logging.info('Done!')
