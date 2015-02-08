from django.db import models

from djangotoolbox.fields import ListField


class Tweets(models.Model):
    STD_MAX = 100
    TWEET_MAX = 140

    screen_name = models.CharField(max_length=STD_MAX)
    full_name = models.CharField(max_length=STD_MAX)
    location = models.CharField(max_length=STD_MAX)
    stock = ListField()
    num_stock = models.IntegerField()
    tweet = models.CharField(max_length=TWEET_MAX)
    buy_sentiment = models.BooleanField()
    sentiment_word = ListField()
    favorited = models.IntegerField()
    retweeted = models.IntegerField()
    is_retweet = models.BooleanField()
    hashtags = ListField()
    user_mentions = ListField()
    geo = models.CharField(max_length=STD_MAX, null=True)
    coordinates = models.CharField(max_length=STD_MAX, null=True)
    created_at = models.DateTimeField()
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return self.screen_name
