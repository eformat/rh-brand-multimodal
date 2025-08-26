from flask import Flask, jsonify, request
#from functools import lru_cache
import requests
import json
from rich import print
import copy
import math
import os

MODEL_URL = os.getenv("MODEL_URL", "localhost:8081")

app = Flask(__name__,
            static_url_path='', 
            static_folder='')

icon = {
      "adult": False,
      "backdrop_path": "",
      "genre_ids": [
        18,
        80
      ],
      "id": 278,
      "original_language": "en",
      "original_title": "",
      "overview": "",
      "production_countries": [
            {
            "iso_3166_1": "US",
            "name": "United States of America"
            }
      ],
      "popularity": 27.7525,
      "poster_path": None,
      "release_date": "1994-09-23",
      "revenue": 28341469,
      "runtime": 142,
      "title": "",
      "video": False,
      "vote_average": 8.712,
      "vote_count": 28753
    }

items = {
  "page": 0,
  "results": [],
  "total_pages": 0,
  "total_results": 0
}

page_results = 10
k = 100

#@lru_cache(maxsize=1000000)
def populate_items(query, pageNumber):
    # api_url = 'http://localhost:8081/api/search?query=What+is+a+large+icon+for+OpenShift&k=10'
    it = copy.deepcopy(items)
    q = f"{query}&k={k}"
    api_url = f"http://{MODEL_URL}/api/search?query={q}"
    #print(api_url)
    response = requests.get(api_url)
    start = (int(pageNumber) * page_results) - page_results
    end = (int(pageNumber) * page_results)
    for i, result in enumerate(response.json()):
        #print(f">> start: {start} < i: {i} > end: {end}")
        if i in range(int(start), int(end)):
            image_name = result["document_metadata"][0]["source"]
            image_path = result["document_metadata"][1]["source"]
            print(i, " ", image_name, " ", image_path)
            ic = copy.copy(icon)
            ic["id"] = i
            ic["title"] = image_name
            ic["backdrop_path"] = "/" + image_path
            ic["overview"] = result["content"]
            ic["vote_count"] = result["rank"]
            ic["vote_average"] = result["score"]
            it["results"].append(ic)
            #print(it)
    it["total_results"] = i
    it["total_pages"] = math.ceil(k/page_results)
    app.live_items = copy.deepcopy(it)
    #print(">> results: ", len(app.live_items["results"]))
    return it

@app.route("/items", methods=["GET"])
def get_items():
    pageNumber = request.args.get('pageNumber')
    return jsonify(populate_items("What+is+a+large+icon+for+OpenShift", pageNumber))

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in app.live_items["results"] if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item not found"}), 404

@app.route("/search/<query>", methods=["GET"])
def search(query):
    pageNumber = request.args.get('pageNumber')
    return jsonify(populate_items(f"{query}", pageNumber))

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)

