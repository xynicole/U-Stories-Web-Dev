import datetime

class StoryEntry():

    def __init__(self, author, story_title, story_text, is_finished):
        ''' Initializes a story entry, will be organized by the shared title between stories
            Time is set to now, as a story entry will only be initialized when it is submitted by a user'''

        self.author = author
        self.story_title = story_title
        self.story_text = story_text
        self.time = datetime.datetime.now()
        self.is_finished = is_finished
        self.total_votes = 0

    def upvote(self):
        self.total_votes += 1

    def downvote(self):
        self.total_votes -= 1
