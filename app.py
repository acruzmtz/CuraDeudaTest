from flask import Flask, request, jsonify
from models import setup, query


app = Flask(__name__)


@app.before_first_request
def create_tables():
    setup.create_tables()


@app.route('/state/', methods=['GET'])
def search_sate_by_name():

    state = request.json.get('state')

    if state:
        data = query.search_by_name(state, 'estado')

        if data:
            response = jsonify(
                {
                    "code": f"{data[0][0]}",
                    "description": f"{data[0][1]}"
                }
            )
        else:
            response = jsonify({"message": f"There isn`t state whit name: {state}"})
    elif state == '':
        response = jsonify({"message": "Please, the state is required!"})
    else:
        response = jsonify({"message": "An error was ocurred, please try again!"})

    return response


@app.route('/township/', methods=['GET'])
def search_township_by_name():

    township = request.json.get('township')

    if township:
        data = query.search_by_name(township, 'municipio')

        if data:
            response = jsonify(
                {
                    "code": f"{data[0][0]}",
                    "description": f"{data[0][1]}"
                }
            )
        else:
            response = jsonify({"message": f"There isn`t township whit name: {township}"})
    elif township == '':
        response = jsonify({"message": "Please, the township is required!"})
    else:
        response = jsonify({"message": "An error was ocurred, please try again!"})

    return response


@app.route('/suburb/', methods=['GET'])
def search_suburb_by_name():

    suburb = request.json.get('suburb')

    if suburb:
        data = query.search_by_name(suburb, 'colonia')

        if data:
            response = jsonify(
                {
                    "code": f"{data[0][0]}",
                    "description": f"{data[0][1]}"
                }
            )
        else:
            response = jsonify({"message": f"There isn`t suburb whit name: {suburb}"})
    elif suburb == '':
        response = jsonify({"message": "Please, the suburb is required!"})
    else:
        response = jsonify({"message": "An error was ocurred, please try again!"})

    return response


@app.route('/suburb/postal_code/', methods=['GET'])
def search_suburb_by_postal_code():

    suburb_postal_code = request.json.get('postal_code')

    if suburb_postal_code and suburb_postal_code.isdigit():
        data = query.search_suburb_by_postal_code(suburb_postal_code)

        if data:
            response = jsonify(
                {
                    "code": f"{data[0][0]}",
                    "description": f"{data[0][1]}"
                }
            )
        else:
            response = jsonify({"message": f"There isn`t suburb whit postal code: {suburb_postal_code}"})
    elif suburb_postal_code == '':
        response = jsonify({"message": "Please, the postal code is required!"})
    else:
        response = jsonify({"message": "An error was ocurred, please try again!"})

    return response


@app.route('/state', methods=['POST'])
def create_new_state():

    if request.method == 'POST':
        code = request.json.get('code')
        description = request.json.get('description')

        if code and description and query.create_new_state(code, description):
            response = jsonify({
                "message": f"The state '{description}' with code: {code} , was created successfully!"
            })
        elif code == '' or description == '':
            response = jsonify({
                "message": "Please, the code and description are required!"
            })
        else:
            response = jsonify({
                "message": "An error was ocurred, please try again!"
            })

    return response


@app.route('/township', methods=['POST'])
def create_new_township():

    if request.method == 'POST':
        code = request.json.get('code')
        description = request.json.get('description')
        state_code = request.json.get('state_code')

        if code and description and state_code and query.create_new_township(code, description, state_code):
            response = jsonify({
                "message": f"The township '{description}' with code: {code} , was created successfully!"
            })
        elif code == '' or description == '' or state_code == '':
            response = jsonify({
                "message": "Please, the code, description and state code are required!"
            })
        else:
            response = jsonify({
                "message": "An error was ocurred, please try again!"
            })

    return response


@app.route('/suburb', methods=['POST'])
def create_new_suburb():

    if request.method == 'POST':
        code = request.json.get('code')
        description = request.json.get('description')
        township_code = request.json.get('township_code')

        if code and description and township_code and query.create_new_suburb(code, description, township_code):
            response = jsonify({
                "message": f"The suburb '{description}' with code: {code} , was created successfully!"
            })
        elif code == '' or description == '' or township_code == '':
            response = jsonify({
                "message": "Please, the code, description and township code are required!"
            })
        else:
            response = jsonify({
                "message": "An error was ocurred, please try again!"
            })

    return response


@app.errorhandler(404)
def error(error):
    return jsonify({"message": "The endpoint does not exist, please try again!"})


if __name__ == '__main__':
    app.run(debug=True)
