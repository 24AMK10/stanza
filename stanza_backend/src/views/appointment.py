import re
from flask import Flask, Blueprint, request, jsonify
from . import appointment_handler
from . import default_response

appoint = Blueprint('appoint', __name__)

@appoint.route('/schedule', methods=['POST'])
def appointment():
    if request.method == "POST":
        req_data = request.get_json(force=True)
        if req_data["mobile_no"] and len(str(int(req_data["mobile_no"]))) == 10:
            res = appointment_handler.schedule_appointment(req_data)
            if res:
                return jsonify({"status": True, "message": "appointment scheduled"}), 200
            return jsonify({"status": False, "message": "Server side error"}), 503
        return jsonify(default_response.invalid_request_params), 400
    return jsonify(default_response.invalid_request_method), 400