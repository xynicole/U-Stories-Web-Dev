import flask
from google.cloud import datastore

def get_client():
    return datastore.Client()

def create_story():
    client = get_client()
    key = client.key('story')
    return datastore.Entity(key)

def retrieve_story(id):
    client = get_client()
    key = client.key('story', int(id))
    return client.get(key)

def update_entries(story_entry):
    client = get_client()
    client.put(story_entry)