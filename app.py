import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup
import random

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    """はてブのホットエントリーから記事を入手して、ランダムに1件返却します."""

    """
        **** ここを実装します（基礎課題） ****

        1. はてブのホットエントリーページのHTMLを取得する
        2. BeautifulSoupでHTMLを読み込む
        3. 記事一覧を取得する
        4. ランダムに1件取得する
        5. 以下の形式で返却する.
            {
                "content" : "記事のタイトル",
                "link" : "記事のURL"
            }
    """
    # 1. はてブのホットエントリーページのHTMLを取得する
    with urlopen("https://b.hatena.ne.jp/") as res:
        html = res.read().decode("utf-8")
    # 2. BeautifulSoupでHTMLを読み込む
    soup = BeautifulSoup(html, "html.parser")
    # 3. 記事一覧を取得する
    newses = soup.select(".entrylist-item .entrylist-contents-title a")
    # 4. ランダムに1件取得する
    news = random.choice(newses)
    title = news.string
    url = news["href"]
    # 5. 以下の形式で返却する.
    # ダミー
    return json.dumps({
        "content" : title,
        "link" : url
    })

@app.route("/api/weather_report")
def api_get_weather_report():
    """
        **** ここを実装します（発展課題） ****
        ・自分の好きなサイトをWebスクレイピングして情報をフロントに返却します
        ・お天気APIなども良いかも
        ・関数名は適宜変更してください
    """

    with urlopen("https://www.jma.go.jp/bosai/forecast/") as res:
        html = res.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    weathers = soup.select(".forecast-table div")
    print(weathers)
    return json.dumps({
    "weather" : weathers,
    })

if __name__ == "__main__":
    app.run(debug=True, port=5004)
