import json

class Contact(object):
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

class Event(object):
    def __init__(self, id, name, description, start_time, duration, location, contact):
        self.id = 0
        self.name = name
        self.description = description
        self.start_time_sec = start_time
        self.duration_sec = duration
        self.location = location
        self.contact = contact

def contact_from_json(json):
    return Contact(json['name'], json['email'], json['phone_number'])

def event_to_json(event):
    return json.dumps({
      'id': event.id,
      'name': event.name,
      'description': event.description,
      'start_time_sec': event.start_time_sec,
      'duration_sec': event.duration_sec,
      'location': event.location,
      'contact': {
        'name': event.contact.name,
        'email': event.contact.email,
        'phone_number': event.contact.phone_number
      }
    })

def event_from_json(json):
    return Event(json['id'], json['name'], json['description'],
        json['start_time_sec'], json['duration_sec'], json['location'],
        contact_from_json(json['contact']))
