from flask import Flask, request, jsonify

app = Flask(__name__)
db = {}


@app.route('/db/<key>', methods=['POST', 'GET'])
def db_request_hanler(key):
    '''
    get / sets a key value
    '''
    if request.method == 'POST':
        db[key] = request.get_json()

    if key not in db:
        return jsonify(msg='key:{0} not found'.format(key), status=404), 404

    return jsonify(db[key])


app.run(port=8080)
