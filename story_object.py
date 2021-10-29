
class StoryEntry():

    def __init__(self, datastore_entry):
        ''' Initializes a story entry, will be organized via linked list essentially,
            Time is set to now, as a story entry will only be initialized when it is submitted by a user'''

        self.author = datastore_entry['author']
        self.story_title = datastore_entry['title']
        self.story_text =  datastore_entry['text']
        self.time = datastore_entry['time']
        self.is_finished = datastore_entry['is_finished']
        self.total_votes = datastore_entry['total_votes']
        self.parent_id = datastore_entry['parent_id']
        self.child_id = datastore_entry['child_id']


    def upvote(self):
        self.total_votes += 1

    def downvote(self):
        self.total_votes -= 1

    def get_parent_id(self):
        return self.parent_id

    def get_child_id(self):
        return self.child_id

    # ---------- Comparisons ----------
    def __lt__(self, other):
        return self.time < other.time
    
    def __le__(self, other):
        return self.time <= other.time

    def __gt__(self, other):
        return self.time > other.time

    def __ge__(self, other):
        return self.time >= other.time 

    def __eq__(self, other):
        return self.time == other.time

    def __ne__(self, other):
        return self.time != other.time
