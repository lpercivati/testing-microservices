from flask import jsonify

class PingController:
    def ping(self):
        return jsonify("OK")