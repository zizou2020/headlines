import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)
rss_feed = {'wsj': "https://feeds.a.dj.com/rss/RSSWSJD.xml",
            'cnbc': "https://www.cnbc.com/id/100003114/device/rss/rss.html",
            'washington_post': "http://feeds.washingtonpost.com/rss/politics?itid=lk_inline_manual_2"}

@app.route("/")
@app.route('/<publication>')
def get_news(publication='wsj'):
    feed = feedparser.parse(rss_feed[publication])
    first_article = feed['entries'][0]
    return render_template("home.html", articles=feed['entries'])

if __name__ == "__main__":
    app.run(port=5000, debug=True)
