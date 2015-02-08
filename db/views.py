from django.http import HttpResponse

from db.models import Tweets

from streaming.settings import STOCK_CODES


def api (request):
    data = []
    query = request.GET.get('search', None)
    if query:
        first_char = query[0]
        query_code = query[1:]
        stock_codes = STOCK_CODES.keys()

        if query == 'ALL_STOCKS':
            tweets = Tweets.objects.order_by('-created_at')[:50]
            data = compile_data(tweets)
        elif first_char == '$' and query_code in stock_codes:
            tweets = Tweets.objects.filter(stock=query_code)
            data = compile_data(tweets.order_by('-created_at')[:50])

    if not data:
        name = request.GET.get('name', None)
        location = request.GET.get('loc', None)
        before = request.GET.get('before', None)
        after = request.GET.get('after', None)
        tweets = Tweets.objects
        if name:
            tweets = tweets.filter(screen_name=name)
        if location:
            tweets = tweets.filter(location=location)
        if before:
            tweets = tweets.filter(created_at__lte=before)
        if after:
            tweets = tweets.filter(created_at__gte=after)

        if not name and not location and not before and not after:
            data = []
        else:
            data = compile_data(tweets.order_by('-created_at')[:50])

    return HttpResponse(data, mimetype='application/json')


def compile_data(tweets):
    data = []
    sentiment = 0
    for tweet in tweets:
        data.append({
            'screen_name'   : tweet.screen_name,
            # 'full_name'     : tweet.full_name,
            'location'      : tweet.location,
            # 'stock'         : tweet.stock,
            # 'num_stock'     : tweet.num_stock,
            'tweet'         : tweet.tweet,
            'buy_sentiment' : tweet.buy_sentiment,
            'sentiment_word': tweet.sentiment_word,
            # 'favorited'     : tweet.favorited,
            # 'retweeted'     : tweet.retweeted,
            # 'is_retweet'    : tweet.is_retweet,
            # 'hashtags'      : tweet.hashtags,
            # 'user_mentions' : tweet.user_mentions,
            # 'geo'           : tweet.geo,
            # 'coordinates'   : tweet.coordinates,
            'created_at'    : tweet.created_at,
            # 'timestamp'     : tweet.timestamp
        })
        if tweet.buy_sentiment == True:
            sentiment += 1
        elif tweet.buy_sentiment == False:
            sentiment -= 1
    data.append(sentiment)
    return data
