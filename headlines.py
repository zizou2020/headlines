import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

rss_feed = {'wsj': "https://feeds.a.dj.com/rss/RSSWSJD.xml",
            'cnbc': "https://www.cnbc.com/id/100003114/device/rss/rss.html",
            'washington_post': "http://feeds.washingtonpost.com/rss/politics?itid=lk_inline_manual_2"}

@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in rss_feed:
        publication = "wsj"
    else:
        publication = query.lower()
    feed = feedparser.parse(rss_feed[publication])
    return render_template("home.html", articles=feed['entries'])


if __name__ == "__main__":
    app.run(port=5000, debug=True)
