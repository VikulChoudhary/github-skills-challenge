from event_topic import EventTopic


class EventConsumer:
    """Consumes events from an in-memory topic."""

    def __init__(self, topic: EventTopic):
        self.topic = topic

    def consume(self):
        messages = self.topic.get_messages()
        print(f"Consumer: received {len(messages)} event(s) from {self.topic.name}")
        return messages