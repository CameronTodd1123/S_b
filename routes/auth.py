from flask import Flask, request, jsonify, Response
import json
from . import routes
import requests
from pprint import pprint
VERIFY_TOKEN = "0tM7EsCgkndOcUANhS4LHxSsmv2QoZk4w9AaVJkVr2Qzr2qujmG3gAQc9iciCjRYQh5zF0s1C0UdtZR5jorPq5BpdntixNh0oc3RiXt11uvGjNLVflni5UcDvaL975xq4zvjFjs0xvDSlIFmOcNOhTjYKiIKxFUCfgyZwZiQa7HfVgD5pejgkQwjhXO17RT9eUtFX2I9"

@routes.route("/auth", methods=['GET'])
def handle_verification():
    if request.args['hub.verify_token'] == VERIFY_TOKEN:
        return request.args['hub.challenge']
    else:
        return "Invalid verification token"
