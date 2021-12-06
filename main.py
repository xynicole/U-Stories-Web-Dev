import flask

from random import randint
from hashlib import sha256

from datastore import get_users, create_user, create_story, create_head_story, update_entries, retrieve_head_story, retrieve_story, init_story_head, init_story_child, get_head_stories
from story_object import StoryEntry

app = flask.Flask(__name__)

@app.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    print("I got here!")
    username = flask.request.values['username']
    users = get_users()
    print("2")

    # check to see if username is already taken; if so, reload page
    for user in users:
        if user['username'] == username or user['username'] == "":
            return flask.render_template('sign-up.html')

    print("pt3")
    hashed_pw = sha256(flask.request.values['password'].encode('utf-8')).digest()

    create_user(username, hashed_pw)
    #flask.response.set_cookie('username', username)
    print("4")
    return flask.render_template('homepage.html')

@app.route('/create-new-story', methods=['POST', 'GET'])
def create_new_story():
    # Grab title and text from HTML
    title = flask.request.values['title']
    text = flask.request.values['story-text']
    author = 'user_name'
    story_list = create_head_story()

    init_story_head(story_list, author, title, text)

    update_entries(story_list)
    return flask.render_template('homepage.html')

@app.route('/create-new-child-story', methods=['POST', 'GET'])
def create_new_child_story():
    parent_id = flask.request.values['parent-id']
    text = flask.request.values['story-text']
    author = 'usered-named'

    new_story = create_story()

    parent_story = retrieve_head_story(parent_id)

    while parent_story['child_id'] != "" :
        parent_story = retrieve_story(parent_story['child_id'])

    init_story_child(new_story, parent_story, author, text)

    new_story['parent_id'] = parent_story.key.name
    parent_story['child_id'] = new_story.key.name

    update_entries(parent_story)
    update_entries(new_story)
    return flask.render_template('homepage.html')


# ---------- Actual Web Pages Start Here ----------
@app.route('/')
@app.route('/index.html')
def root():
    return flask.render_template('index.html')

@app.route('/p/write-story.html', methods=['POST', 'GET'])
def write_story():
    return flask.render_template('write-story.html')

@app.route('/p/receive-story.html', methods=['POST', 'GET'])
def receive_story():
    stories = get_head_stories()

    # grab the id of a random story from the list of stories
    stories_list = list(stories)
    random_story_idx = randint(0, len(stories_list)-1)
    random_story_id = stories_list[random_story_idx].key.name

    return flask.render_template('receive-story.html', story_list=stories, random_story_id=random_story_id)

@app.route('/p/append-story.html', methods=['POST', 'GET'])
def append_story():
    id = flask.request.values['id']
    datastore_story_entry = retrieve_head_story(id)
    stories = [datastore_story_entry]

    while datastore_story_entry['child_id'] != "" :
        datastore_story_entry = retrieve_story(datastore_story_entry['child_id'])
        stories.append(datastore_story_entry)

    return flask.render_template('append-story.html', story_list=stories)

@app.route('/p/confirm-receive-story.html', methods=['POST', 'GET'])
def confirm_receive_story():
    id = flask.request.values['id']
    datastore_story_entry = retrieve_head_story(id)
    stories = [datastore_story_entry]

    while datastore_story_entry['child_id'] != "" :
        datastore_story_entry = retrieve_story(datastore_story_entry['child_id'])
        stories.append(datastore_story_entry)

    return flask.render_template('confirm-receive-story.html', story_list=stories)


# Any page that is not specified will default here with no functionality
@app.route('/p/<requested_page>')
def templater(requested_page):
    return flask.render_template(requested_page)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
