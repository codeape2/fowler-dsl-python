"""
This module defines a state machine.

Example:

>>> doorClosed = Event("doorClosed", "D1CL")
>>> unlockPanelCmd = Command("unlockPanel", "PNUL")
>>> unlockDoorCmd = Command("unlockDoor", "D1UL")
>>> idle = State("idle", actions=[unlockDoorCmd], transitions={})
"""

class AbstractEvent(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Command(AbstractEvent):
    pass

class Event(AbstractEvent):
    pass

class State(object):
    def __init__(self, name, actions: "list of commands",
                 transitions: "event -> target state dictionary"):
        self.name = name
        self.actions = actions
        self.transitions = transitions

    def get_all_targets(self):
        retval = []
        for t in self.transitions.valueiter():
            retval.append(t)
        return retval

class Transition(object):
    def __init__(self, source: State, trigger: Event, target: State):
        self.source = source
        self.trigger = trigger
        self.target = target

class StateMachine(object):
    def __init__(self, start: State, reset_events: "list of reset events"):
        self.start = start
        self.reset_events = reset_events

    def get_states(self):
        retval = []
        self.collect_states(retval, self.start)
        return retval

    def collect_states(self, retval: "List of states", s: State):
        if s in retval:
            return
        else:
            retval.append(s)
            for next in s.get_all_targets():
                self.collect_states(retval, next)
