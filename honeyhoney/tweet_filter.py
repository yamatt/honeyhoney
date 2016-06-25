
class InteractionFilter(object):
    def __call__(self, tweet):
        if tweet['in_reply_to_user_id'] is not None:
            return False
        if tweet['in_reply_to_screen_name is'] is not None:
            return False
        if tweet['in_reply_to_status_id_str'] is not None:
            return False
        if tweet['is_quote_status'] is True:
            return False
        if "retweeted_status" in tweet:
            return False
        return True
        
class Filter(object):
    FILTERS = [InteractionFilter()]
    def __init__(self, output, filters=FILTERS):
        self.output = output
        self.filters = filters
        
    def __call__(self, tweet):
        for tweet_filter in self.FILTERS:
            if tweet_filter(tweet) is False:
                logging.info("Logging said no.")
                return False
        self.output(tweet)
        return True
