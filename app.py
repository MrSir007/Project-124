from flask import Flask, jsonify, request

app = Flask(__name__)
# To create an area of tasks with different objects in each
tasks = [
  {
    "id": 1,
    "contact": u"001",
    "name": u"A",
    "done": False
  },
  {
    "id": 2,
    "contact": u"002",
    "name": u"B",
    "done": False
  },
  {
    "id": 3,
    "contact": u"003",
    "name": u"C",
    "done": False
  }
]

@app.route("/add-data", methods=["POST"])
def add_task () :
  if not request.json :
    return jsonify ({
      "status": "error",
      "message": "please provide data"
    },400)
  # To add new tasks
  task = {
    "id": tasks[-1]["id"] + 1,
    "contact": request.json["contact"],
    "name": request.json.get("name",""),
    "done": False
  }
  tasks.append(task)
  return jsonify ({
    "status": "success",
    "message": "contact added"
  })

@app.route("/get-data")
def get_task () :
  return jsonify ({
    "data": tasks
  })

if (__name__ == "__main__") :
  app.run(debug=True)