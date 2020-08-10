import feedparser
from flask import Flask

app = Flask(__name__)
rss_feed = {'wsj': "https://feeds.a.dj.com/rss/RSSWSJD.xml",
            'cnbc': "https://www.cnbc.com/id/100003114/device/rss/rss.html",
            'washington_post': "http://feeds.washingtonpost.com/rss/politics?itid=lk_inline_manual_2"}

@app.route("/")
@app.route('/<publication>')
def get_news(publication='wsj'):
    feed = feedparser.parse(rss_feed[publication])
    first_article = feed['entries'][0]
    return """<html>
        <body>
            <h1>Headlines </h1>
            <b>{0}</b> </ br>
            <i>{1}</i> </ br>
            <p>{2}</p> </ br>
            <link>{3}</link> </ br>
        </body>
    </html>""".format(first_article.get("title"),
                      first_article.get("published"),
                      first_article.get("summary"),
                      first_article.get("link"))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
