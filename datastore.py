import flask
import datetime

import sys
import random

from google.cloud import datastore

def get_client():
    return datastore.Client()

def get_stories():
    story_list = []
    client = get_client()
    query = client.query(kind='child_story')
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
    key = client.key('story', random.randint(1, sys.maxsize))
    return datastore.Entity(key)

def create_head_story():
    client = get_client()
    key = client.key('head_story', random.randint(1, sys.maxsize))
    return datastore.Entity(key)

def retrieve_head_story(id):
    client = get_client()
    key = client.key('head_story', int(id))
    return client.get(key)

def retrieve_story(id):
    client = get_client()
    key = client.key('child_story', int(id))
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
    story_list['child_id'] = 0
    
def init_story_child(new_story, parent_story, author, text):
    new_story['author'] = author
    new_story['text'] = text
    new_story['time'] = datetime.datetime.now()
    new_story['is_finished'] = False
    new_story['total_votes'] = 0
    new_story['parent_id'] = parent_story.id
    new_story['child_id'] = 0
    parent_story['child_id'] = new_story.id