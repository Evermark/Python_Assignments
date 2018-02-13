You will create two classes. One class should be Call, the other CallCenter.

Each instance of Call() should have:

Attributes:
• unique id
• caller name
• caller phone number
• time of call
• reason for call

Methods:
• display: that prints all Call attributes.

CallCenter Class
• Each instance of CallCenter()
should have the following attributes:

Attributes:
• calls: should be a list of call objects
• queue size: should be the length of the call list

Methods:
• add: adds a new call to the end of the call list
• remove: removes the call from the beginning of the list (index 0).
• info: prints the name and phone number for each call in the queue as well as the length of the queue.

class Call(object):
    def __init__(self, id, name, phone_number, call_time, call_reason):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.call_time = call_time
        self.call_reason = call_reason

    def display_call(self):
        print self.id
        print self.name
        print self.phone_number
        print self.call_time
        print self.call_reason

class CallCenter(object):
    def __init__(self, calls, queue_size):
        self.calls = list(calls)
        self.queue_size = len(list(calls))
    def add(self):
        self.calls[len(self.calls)] += self.calls
    def remove(self):
        self.calls[0] -= self.calls
    def info(self):
        print self.name
        print self.phone_number
        print self.queue_size
