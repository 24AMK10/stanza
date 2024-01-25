import re
from flask import Flask, Blueprint, jsonify, request
from . import db_ops
from . import default_response 

pg_search = Blueprint('pg_search', __name__)


@pg_search.route('/get-pgs/<pattern>')
def get_pg(pattern):
    if request.method == "GET":
        if not pattern:
            return jsonify(default_response.invalid_request_params), 400   
        search_res = db_ops.show_pg_search_res(pattern)
        return jsonify(search_res), 200
    return jsonify(default_response.invalid_request_method), 400


@pg_search.route('/get-by-locality-city', methods=['GET'])
def get_by_locality_city():
    if request.method == "GET":
        locality = request.args.get('locality')
        city = request.args.get('city')
        if city and locality:
            res = db_ops.get_pgs_by_locality_city(locality, city)
            return jsonify(res), 200        
        return jsonify(default_response.invalid_request_params)
    return jsonify(default_response.invalid_request_method)

