class AbstractEvent(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Command(AbstractEvent):
    pass

class Event(AbstractEvent):
    pass
