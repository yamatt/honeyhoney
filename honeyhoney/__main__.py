from .config import load_config
from .client import Client
from .tweet_filter import Filter

import argparse

import logging

def load_args():
    parser = argparse.ArgumentParser(
        description='Discretely mirror a Twitter account.'
    )
    parser.add_argument('--config', "-c", help='Path to config file')
    parser.add_argument('--log', help='Logging level: DEBUG,INFO, etc.')

    opts = parser.parse_args()
    
    arg_auto(opts)

    return opts
    
def arg_auto(opts):
    level = getattr(logging, opts.log.upper(), None)
    logging.basicConfig(level=level)

if __name__ == "__main__":
    opts = load_args()
    config = load_config(opts)
    client = Client.from_config(config)
    filter = Filter(client.post_from_tweet)
    client.consume(filter, follow=config['source_user_ids'])
