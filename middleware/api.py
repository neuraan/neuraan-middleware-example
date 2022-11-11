#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from flask import Blueprint
from flask import request
import requests
import json

API_KEY='<YOUR_API_KEY>'

bp = Blueprint("api", __name__)

def request_entities(text):
    url = "https://invoke.neuraan.com/default/v1"
    payload = json.dumps({
        "name": "Custom NER",
        "input": { "text": text},
        "threshold": 0.7})
    headers = {
        'Authorization': f"Bearer {API_KEY}",
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    api_response = json.loads(response.text)
    if len(api_response["result"]["detected"]) > 0:
        detected = [e[0] for e in api_response["result"]["detected"]]
        return detected, api_response
    return [], api_response

@bp.route("/get-business", methods=("GET", "POST"))
def get_business():
    if request.method == "POST":
        data = json.loads(request.data)
        neuraan_reponse = data["__neuraan_core_response__"]
        #Call custom NER
        entities, api_response = request_entities(neuraan_reponse["query"])
        if len(entities) > 0:
            return {'negocios': entities, 'response': entities[0], 'success': True}
        else:
            return {'negocios': entities, 'response': 'No detecté el negocio. Puedes decirlo de nuevo por favor?', 'success': False}

@bp.route("/get-postal-code", methods=("GET", "POST"))
def get_postal_code():
    if request.method == "POST":
        data = json.loads(request.data)
        neuraan_reponse = data["__neuraan_core_response__"]
        negocios = data["negocio"]
        #Call custom NER
        entities, api_response = request_entities(neuraan_reponse["query"])
        #Query database
        if len(entities) > 0:
            return {'response': query_database(negocios, entities[0]), 'success': True}
        else:
            return {'response': 'Porfavor proporicone un C.P. válido', 'success': False}

def query_database(business, postal_code):
    business_number = random.randint(0, 100)
    return f"En el codigo postal {postal_code} hay {business_number} {business}"

