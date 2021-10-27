import flask

from datastore import create_story, update_entries, retrieve_story
from story_object import StoryEntry

app = flask.Flask(__name__)

@app.route('/create-story', methods=['POST', 'GET'])
def create_new_story():
    # Grab title and text from HTML 
    title = flask.request.values['title']
    text = flask.request.values['text']
    # entry = StoryEntry("test", title, text, False)

    story_list = create_story()
    story_list['author'] = 'test'
    story_list['title'] = title
    story_list['text'] = text
    story_list['is_finished'] = False
    
    update_entries(story_list)
    return flask.render_template('homepage.html')

@app.route('/get-story', methods=['POST', 'GET'])
def get_story():
    id = flask.request.values['id']
    datastore_story_entry = retrieve_story(id)
        

# ---------- Actual Web Pages Start Here ----------
@app.route('/')
@app.route('/index.html')
def root():
    return flask.render_template('index.html')

@app.route('/p/write-story.html', methods=['POST', 'GET'])
def write_story():
    return flask.render_template('write-story.html')

@app.route('/p/<requested_page>')
def templater(requested_page):
    return flask.render_template(requested_page)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)