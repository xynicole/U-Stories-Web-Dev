import flask
import datetime
from google.cloud import datastore

def get_client():
    return datastore.Client()

def get_stories():
    story_list = []
    client = get_client()
    query = client.query(kind='story')
    for entity in query.fetch():
        story_list.append(entity)
    return story_list

def get_head_stories():
    story_list = []
    client = get_client()
    query = client.query(kind='head_story')
    for entity in query.fetch():
        story_list.append(entity)
    return story_list

def create_story():
    client = get_client()
    key = client.key('story')
    return datastore.Entity(key)

def create_head_story():
    client = get_client()
    key = client.key('head_story')
    return datastore.Entity(key)

def retrieve_story(id):
    client = get_client()
    key = client.key('story', int(id))
    return client.get(key)

def update_entries(story_entry):
    client = get_client()
    client.put(story_entry)

def init_story_head(story_list, author, title, text):
    story_list['author'] = author
    story_list['title'] = title
    story_list['text'] = text
    story_list['time'] = datetime.datetime.now()
    story_list['is_finished'] = False
    story_list['total_votes'] = 0
    story_list['parent_id'] = story_list.id
    story_list['child_id'] = 0
