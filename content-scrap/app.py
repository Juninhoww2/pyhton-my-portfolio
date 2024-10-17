from flask import Flask, render_template
from scraper import scrape_techcrunch
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    headlines = scrape_techcrunch() 
    return render_template("index.html", headlines=headlines)

if __name__ == "__main__":
    app.run(debug=True)