from event_topic import EventTopic


class EventProducer:
    """Publishes anomaly events to an in-memory topic."""

    def __init__(self, topic: EventTopic):
        self.topic = topic

    def publish(self, event):
        if not event:
            return False

        print("Producer: publishing anomaly event")
        self.topic.publish(event)
        print(f"Topic: {self.topic.name} received event")
        return True