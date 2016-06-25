# HoneyHoney
Allows you to discretely mirror another users Twitter account. The use case for this (for me) is to have an account that looks as much like my own so as to ensnare automated users, by looking like a normal account plus a bit, while also not duplicating things like replies, favourites and retweets that might look a bit odd.
## Usage
This is designed for Python 3 in mind. (It might work for Python 2)
Consumes Tweets the users specified in `source_user_ids` from the config file (example below) and posts them to the user account with the `access_token` assiged to this script.
### Command Line

    python3 -m honeyhoney -c config.yaml --log=DEBUG
    
### Config File (config.yaml)

    ---
    consumer_key: something
    consumer_secret: something
    access_token_key: something
    access_token_secret: something
    source_user_ids:
        - "1234567890"
        - "0987654321"

## Getting
### User IDs
http://gettwitterid.com/
### Consumer Key
https://python-twitter.readthedocs.io/en/latest/getting_started.html
