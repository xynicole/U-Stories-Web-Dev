import datetime

class StoryEntry():

    def __init__(self, author, storyTitle, storyText, isFinished):
        ''' Initializes a story entry, will be organized by the shared title between stories
            Time is set to now, as a story entry will only be initialized when it is submitted by a user'''

        self.author = author
        self.storyTitle = storyTitle
        self.storyText = storyText
        self.time = datetime.datetime.now()
        self.isFinished = isFinished
