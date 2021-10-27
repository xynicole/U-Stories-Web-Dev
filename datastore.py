import flask
from google.cloud import datastore

def get_client():
    return datastore.Client()

def create_story():
    client = get_client()
    key = client.key("story")
    return datastore.Entity(key)

def update_entries(story_entry):
    client = get_client()
    client.put(story_entry)