import uuid
import model

class Storage(object):

    def __init__(self):
        self._events = {}

    def insert_or_update(self, event):
        event.id = uuid.uuid4().hex
        self._events[event.id] = event
        return  event.id

    def get(self, event_id):
        return self._events[event_id]

    def get_all(self):
        data = {
            'events': []
        }
        for event_id in self._events:
            data['events'].append(model.event_to_json(self.get(event_id)))
        return data

    def remove(self, event_id):
        del self._events[event_id]
