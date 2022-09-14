from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import json
from datetime import datetime
from src.get_boxes import Recon
import time
import random
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    emoji_list = ["🫣", "🫡", "🤔", "🙂", "🫠", "🥲", "🤑", "🤐", "😶‍🌫️", "😮‍💨", "😵", "🤯", "🥸", "😲", "😈", 
    "👿", "👾", "💥", "👨‍💻", "🦸‍♀️", "🦠",]

    if request.method == "POST":
        start = time.time()

        Recon("192.168.1.0/24").save_box_data()
        end = time.time()

    with open("data/hosts.json", "r") as f:
        box_list = json.load(f)["hosts"]

    return render_template("index.html", boxes=box_list, lastupdate=datetime.now(), emoji=random.choice(emoji_list))


@app.route("/<name>", methods=["GET"])
def switch_info(name: str):
    """
    This page shows detailed stats on an individual switch
    queried by name number
    """
    with open("data/hosts.json", "r") as f:
        box_list = json.load(f)["hosts"]


    for i, box in enumerate(box_list):
        if box["name"] == name:
            return render_template(
                "manage.html",
                title=name,
                box=box_list[i],
            )

    return render_template(
        "manage.html",
        title=name,
        box={
            "name": "host-00",
            "ip": "0.0.0.0",
            "OS": "Null",
            "services": [],
            "isOn": False
        }
    )

@app.route("/network-wide", methods=["GET"])
def network_wide():
    """
    This page shows a summary of all port counts, etc
    across the entire network
    """
    # network = getNetworkWide()
    return render_template("network-wide.html", network={})

if __name__ == "__main__":
    Bootstrap(app)
    app.run(host="0.0.0.0", port=8080, debug=True)