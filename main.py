import flask

from datastore import create_story, create_head_story, update_entries, retrieve_head_story, retrieve_story, init_story_head, init_story_child, get_head_stories
from story_object import StoryEntry

app = flask.Flask(__name__)

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

    while parent_story['child_id'] != 0 :
        parent_story = retrieve_story(parent_story['child_id'])

    init_story_child(new_story, parent_story, author, text)

    new_story['parent_id'] = int(parent_story.id)
    parent_story['child_id'] = int(new_story.id)    

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
    return flask.render_template('receive-story.html', story_list=stories)

@app.route('/p/append-story.html', methods=['POST', 'GET'])
def append_story():
    id = flask.request.values['id']
    datastore_story_entry = retrieve_head_story(id)
    stories = [datastore_story_entry]

    while datastore_story_entry['child_id'] != 0 :
        datastore_story_entry = retrieve_story(datastore_story_entry['child_id'])
        stories.append(datastore_story_entry)
        
    return flask.render_template('append-story.html', story_list=stories)

@app.route('/p/confirm-receive-story.html', methods=['POST', 'GET'])
def confirm_receive_story():
    id = flask.request.values['id']
    datastore_story_entry = retrieve_head_story(id)
    stories = [datastore_story_entry]

    while datastore_story_entry['child_id'] != 0 :
        datastore_story_entry = retrieve_story(datastore_story_entry['child_id'])
        stories.append(datastore_story_entry)

    return flask.render_template('confirm-receive-story.html', story_list=stories)


# Any page that is not specified will default here with no functionality
@app.route('/p/<requested_page>')
def templater(requested_page):
    return flask.render_template(requested_page)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)