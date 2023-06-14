import praw
from datetime import datetime
import time

# Fill these in with your details
reddit = praw.Reddit(client_id='my_client_id',
                     client_secret='my_client_secret',
                     user_agent='my_user_agent',
                     username='my_username',
                     password='my_password')

subreddit_name = 'my_subreddit'
subreddit = reddit.subreddit(subreddit_name)


day_of_week = datetime.today().weekday()

# days of the week start from Monday=0, Sunday=6
if day_of_week in [1, 3]:  # Tuesday and Thursday
    new_settings = {
        'subreddit_type': 'restricted',
        'disable_contributor_requests': False,
    }
    print(f"Subreddit settings updated to restricted on {datetime.today()}")
else:
    new_settings = {
        'subreddit_type': 'public',
        'disable_contributor_requests': False,
    }
    print(f"Subreddit settings updated to public on {datetime.today()}")

subreddit.mod.update(**new_settings)
