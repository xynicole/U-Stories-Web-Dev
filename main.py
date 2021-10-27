import flask

from datastore import create_story, update_entries
from story_object import StoryEntry

app = flask.Flask(__name__)

@app.route('/')
@app.route('/index.html')
def root():
    return flask.render_template('index.html')

@app.route('/p/write-story.html', methods=['POST', 'GET'])
def write_story():
    return flask.render_template('write-story.html')

@app.route('/create-story', methods=['POST', 'GET'])
def create_new_story():
    title = flask.request.values['title']
    text = flask.request.values['text']
    entry = StoryEntry("test", title, text, False)
    story_list = create_story()
    story_list["entry"] = entry
    update_entries(story_list)

    return flask.render_template('homepage.html')
    


@app.route('/p/<requested_page>')
def templater(requested_page):
    return flask.render_template(requested_page)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)