"""
"Observer" section example showing simple event subscription
with observer pattern.

"""
class Event:
    _observers = []

    def __init__(self, subject):
        self.subject = subject

    @classmethod
    def register(cls, observer):
        if observer not in cls._observers:
            cls._observers.append(observer)

    @classmethod
    def unregister(cls, observer):
        if observer in cls._observers:
            cls._observers.remove(observer)

    @classmethod
    def notify(cls, subject):
        event = cls(subject)
        for observer in cls._observers:
            observer(event)


class WriteEvent(Event):
    def __repr__(self):
        return 'WriteEvent'


def log(event):
    print(
        '{!r} was fired with subject "{}"'
        ''.format(event, event.subject)
    )


class AnotherObserver(object):
    def __call__(self, event):
        print(
            "{!r} trigerred {}'s action"
            "".format(event, self.__class__.__name__)
        )


WriteEvent.register(log)
WriteEvent.register(AnotherObserver())


if __name__ == "__main__":
    Event.notify("telephone rang")
