import flask
from google.cloud import datastore

def get_client():
    return datastore.Client()

def create_thing():
    client = get_client()