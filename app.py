from flask import Flask, request, jsonify
from models import setup, query


app = Flask(__name__)


@app.before_first_request
def create_tables():
    setup.create_tables()


@app.route('/state/', methods=['GET'])
def search_sate_by_name():

    state = request.json.get('state')

    return jsonify({"result": f"{state}"})


@app.route('/township/', methods=['GET'])
def search_township_by_name():

    township = request.json.get('township')

    return jsonify({"result": f"{township}"})


@app.route('/suburb/', methods=['GET'])
def search_suburb_by_name():

    suburb_name = request.json.get('suburb')

    return jsonify({"result": f"{suburb_name}"})


@app.route('/suburb/postal_code/', methods=['GET'])
def search_suburb_by_postal_code():

    suburb_postal_code = request.json.get('postal_code')

    return jsonify({"result": f"{suburb_postal_code}"})


@app.route('/state', methods=['POST'])
def create_new_state():

    if request.method == 'POST':
        code = request.json.get('code')
        description = request.json.get('description')

        new_state = code + '' + description

    return jsonify({"result": f"{new_state}"})


@app.route('/township', methods=['POST'])
def create_new_township():

    if request.method == 'POST':
        code = request.json.get('code')
        description = request.json.get('description')

        new_township = code + '' + description

    return jsonify({"result": f"{new_township}"})


@app.route('/suburb', methods=['POST'])
def create_new_suburb():

    if request.method == 'POST':
        code = request.json.get('code')
        description = request.json.get('description')

        new_suburb = code + '' + description

    return jsonify({"result": f"{new_suburb}"})


if __name__ == '__main__':
    app.run(debug=True)
