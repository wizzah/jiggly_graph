from flask import Flask, render_template, request, jsonify, url_for

# from get_data import data_service
import requests
import json
app = Flask(__name__)
# app.register_blueprint(data_service)
app.debug = True

@app.route("/")
def index():
	"""
	Main entry point to web application, call all the things and send the data to the template
	"""
	print url_for('static', filename='miserables.json')

	return render_template("test.html")


# @app.route("/mis")
# def mis():
# 	"""
# 	Main entry point to web application, call all the things and send the data to the template
# 	"""

# 	return flask.jsonify("miserables.json")
# 	json_data = open(os.path.join(your_static_dir, "data", "taiwan.json"), "r")


if __name__ == "__main__":
	app.run()
