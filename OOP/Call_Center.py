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

from datetime import datetime

class Call(object):
    num_calls = 0
    def __init__(self, name, phone_number, call_reason):
        self.name = name
        self.phone_number = phone_number
        self.call_time = datetime.now()
        self.call_reason = call_reason
        self.id = Call.num_calls

        Call.num_calls += 1

    def display_call(self):
        for attr, val in self.__dict__.iteritems():
            if attr == "call_time":
                print "{}: {} ".format(attr, val.strftime("%b-%a-%I"))
            else:
                print "{}: {}".format(attr, val)

class CallCenter(object):
    def __init__(self, calls, queue_size):
        self.calls = []
        self.queue_size = self.the_queue_size()
    def the_queue_size(self):
        return len(self.calls)
    def add(self, new_call):
        self.calls.append(new_call)
    def remove(self, re_call):
        self.calls.remove(re_call)
    def info(self):
        for call in self.calls:
            call.display_call()
