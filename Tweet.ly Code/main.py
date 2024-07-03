from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = '2FfWFnHOE10SvPKThcXaWrPkd'
consumer_secret = 'pVaLgffcfTgwLRHpVFKuyKgXCzjYrPjLtyC6gUIEcrSLyMXGSM'

access_token = '1177614138631045120-8FRARQGV3axs67fk8WyPRmJCcYt4yg'
access_token_secret = 'ow7VVhnQZxsQjSE2m9niTXr4TU2OfTtwV4XgDfls0kxHo'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})

app.run()