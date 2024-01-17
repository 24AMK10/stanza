from flask import Flask, Blueprint, jsonify, request

pg_search = Blueprint('search_pg', __name__)

@pg_search.route('/get')
def get_pg():
    if request.method == "GET":
        city = request.args.get('city', default=None, type=str)
        locality = request.args.get('locality', default=None, type=str)
        if not city:
            return jsonify({"error": "missing city param"}), 400

        # write a db method to get the data in case city is given 
        # and in case city and locality given
        

        return jsonify({"status": True}), 200
    return jsonify({"error": 'invalid method'}), 400