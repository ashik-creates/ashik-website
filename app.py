from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "London"
  },
  {
    "id": 2,
    "title": "Computer Scientist",
    "location": "New York"
  },
  {
    "id": 3,
    "title": "Hacker",
    "location": "Dubai"
  },
  {
    "id": 4,
    "title": "Graphic Designer",
    "location": "Dhaka"
  }
]

@app.route("/")
def home():
  return render_template("index.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080, debug=True)
  