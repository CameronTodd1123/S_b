from flask import Flask, request, jsonify, Response
import json
from . import routes
import requests
from pprint import pprint
VERIFY_TOKEN = '0tM7EsCgkndOcUANhS4LHxSsmv2QoZk4w9AaVJkVr2Qzr2qujmG3gAQc9iciCjRYQh5zF0s1C0UdtZR5jorPq5BpdntixNh0oc3RiXt11uvGjNLVflni5UcDvaL975xq4zvjFjs0xvDSlIFmOcNOhTjYKiIKxFUCfgyZwZiQa7HfVgD5pejgkQwjhXO17RT9eUtFX2I9'
ACCESS_TOKEN = 'EAAGZCfOZCdjZBwBANkL6JEMJ8BQodNR76c2HLpteN63F3phr4b9sqVjeGsapiCS1ZC5MzGJxXZA4dpLk6OHUZA0KJp1ZAnYaEijZBllkvbpnFCejFyCxj9y8nrCmjASxWTspIZAhBuEnWh3UBTOyJxGSDiZBAIxeKZBHiUeLcTBuZCkrHwZDZD'

def reply(user_id, msg):	
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    url = "https://graph.facebook.com/v2.6/me/messages?access_token={}".format(ACCESS_TOKEN)
    resp = requests.post(url, json=data)
    print(resp.content)



@routes.route("/auth", methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply(sender, message)
    return "ok"