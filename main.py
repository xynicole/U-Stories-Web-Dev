import flask

from random import randint
from hashlib import sha256
from datastore import *
from story_object import StoryEntry

app = flask.Flask(__name__)
app.secret_key = "homiez"

@app.route('/delete-stories')
def delete():
    parent_name = flask.request.values['parent_name']

    delete_stories(parent_name)
    return receive_story()

@app.route('/stop-story')
def stop():
    parent_name = flask.request.values['parent_name']

    stop_story(parent_name)

    stories = get_story_list(parent_name)

    return flask.render_template('confirm-receive-story.html', story_list=stories, username = get_user())

@app.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    username = flask.request.values['username']
    users = get_users()

    # check to see if username is already taken; if so, reload page
    for user in users:
        if user['username'] == username:
            return flask.render_template('sign-up.html')

    hashed_pw = sha256(flask.request.values['password'].encode('utf-8')).hexdigest()

    create_user(username, hashed_pw)
    flask.session['user'] = username
    return flask.render_template('homepage.html', username = get_user())

@app.route('/login', methods=['POST', 'GET'])
def login():
    username = flask.request.values['username']
    user = lookup_user(username)

    # check to see that username exists
    if user == None:
        return flask.render_template('login.html')

    hashed_pw = sha256(flask.request.values['password'].encode('utf-8')).hexdigest()

    # check to see that passwords match
    if hashed_pw != user['hashed_pw']:
        return flask.render_template('login.html')

    flask.session['user'] = username

    return flask.render_template('homepage.html', username = username)

def get_user():
    return flask.session.get('user', None)

@app.route('/sign-out')
def sign_out():
    flask.session['user'] = None
    return flask.redirect('/')
    #return flask.render_template('index.html')

@app.route('/create-new-story', methods=['POST', 'GET'])
def create_new_story():
    # Grab title and text from HTML
    title = flask.request.values['title']
    text = flask.request.values['story-text']
    author = get_user()
    story_list = create_head_story()

    init_story_head(story_list, author, title, text)

    update_entries(story_list)
    return flask.render_template('homepage.html', username = get_user())

@app.route('/create-new-child-story', methods=['POST', 'GET'])
def create_new_child_story():
    parent_id = flask.request.values['parent-id']
    text = flask.request.values['story-text']
    author = get_user()

    parent_story = retrieve_head_story(parent_id)

    if parent_story["is_finished"] :
        stories = get_story_list(parent_id)
        return flask.render_template('confirm-receive-story.html', story_list=stories, username = get_user())

    new_story = create_story()

    while parent_story['child_id'] != "" :
        parent_story = retrieve_story(parent_story['child_id'])

    init_story_child(new_story, parent_story, author, text)

    new_story['parent_id'] = parent_story.key.name
    parent_story['child_id'] = new_story.key.name

    update_entries(parent_story)
    update_entries(new_story)

    stories = get_story_list(parent_id)

    return flask.render_template('confirm-receive-story.html', story_list=stories, username = get_user())

def get_story_list(id):
    datastore_story_entry = retrieve_head_story(id)
    stories = [datastore_story_entry]

    while datastore_story_entry['child_id'] != "" :
        datastore_story_entry = retrieve_story(datastore_story_entry['child_id'])
        stories.append(datastore_story_entry)

    return stories


# ---------- Actual Web Pages Start Here ----------
@app.route('/')
@app.route('/index.html')
def root():
    return flask.render_template('index.html')

@app.route('/p/homepage.html')
def homepage():
    return flask.render_template('homepage.html', username=get_user())

@app.route('/p/write-story.html', methods=['POST', 'GET'])
def write_story():
    return flask.render_template('write-story.html', username=get_user())

@app.route('/p/user-stories.html', methods=['POST', 'GET'])
def user_stories():
    user = get_user()
    stories = get_head_stories()

    user_story_list = []

    for story in stories:
        if story['author'] == user:
            user_story_list.append(story)

    return flask.render_template('user-stories.html', story_list=user_story_list, username=get_user())

@app.route('/p/receive-story.html', methods=['POST', 'GET'])
def receive_story():
    stories = get_head_stories()

    # grab the id of a random story from the list of stories
    stories_list = list(stories)

    random_story_idx = randint(0, len(stories_list)-1)
    random_story_id = stories_list[random_story_idx].key.name

    return flask.render_template('receive-story.html', story_list=stories, random_story_id=random_story_id, username=get_user())

@app.route('/p/append-story.html', methods=['POST', 'GET'])
def append_story():
    id = flask.request.values['id']

    stories = get_story_list(id)

    return flask.render_template('append-story.html', story_list=stories, username=get_user())

@app.route('/p/confirm-receive-story.html', methods=['POST', 'GET'])
def confirm_receive_story():
    id = flask.request.values['id']

    stories = get_story_list(id)

    return flask.render_template('confirm-receive-story.html', story_list=stories, username=get_user())


# Any page that is not specified will default here with no functionality
@app.route('/p/<requested_page>')
def templater(requested_page):
    return flask.render_template(requested_page)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
