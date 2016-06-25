import twitter

import logging

class Client(object):
    @classmethod
    def from_config(cls, config):
        return cls(
            config['consumer_key'],
            config['consumer_secret'],
            config['access_token_key'],
            config['access_token_secret']
        )
        
    def __init__(self,
        consumer_key,
        consumer_secret,
        access_token_key,
        access_token_secret
    ):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token_key = access_token_key
        self.access_token_secret = access_token_secret
        self._twitter = None
        
    @property
    def twitter(self):
        if self._twitter is None:
            self._twitter = twitter.Api(
                self.consumer_key,
                self.consumer_secret,
                self.access_token_key,
                self.access_token_secret
            )
        return self._twitter
        
    @property
    def credentials_ok(self):
        return self.twitter.VerifyCredentials()
        
    def post(self, message):
        logging.info("Posting message {message}".format(
            message=message
        ))
        self.twitter.PostUpdate(message)
        
    def post_from_tweet(self, tweet):
        self.post(tweet['text'])
        
    def consume(self, tweet_filter, **specifically):
        logging.info("Consuming from: {specifically}".format(
            specifically=specifically
        ))
        for tweet in self.twitter.GetStreamFilter(**specifically):
            logging.debug("Got message: {tweet}".format(
                tweet=tweet
            ))
            tweet_filter(tweet)
        
    
