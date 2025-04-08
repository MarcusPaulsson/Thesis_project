from datetime import datetime, timedelta

class CalendarUtil:
    """
    A utility class for managing calendar events, scheduling appointments, and performing conflict checks.
    """

    def __init__(self):
        """Initialize the calendar with an empty list of events."""
        self.events = []

    def add_event(self, event):
        """
        Add an event to the calendar.
        :param event: The event to be added, dict containing 'date', 'start_time', 'end_time', and 'description'.
        """
        if not self.is_valid_event(event):
            raise ValueError("Invalid event data.")
        self.events.append(event)

    def remove_event(self, event):
        """
        Remove an event from the calendar.
        :param event: The event to be removed, dict.
        """
        try:
            self.events.remove(event)
        except ValueError:
            pass  # Event not found; do nothing

    def get_events(self, date):
        """
        Get all events on a given date.
        :param date: The date to get events for, datetime.
        :return: A list of events on the given date.
        """
        return [event for event in self.events if event['date'].date() == date.date()]

    def is_available(self, start_time, end_time):
        """
        Check if the calendar is available for a given time slot.
        :param start_time: The start time of the time slot, datetime.
        :param end_time: The end time of the time slot, datetime.
        :return: True if available, False otherwise.
        """
        for event in self.events:
            if (start_time < event['end_time'] and end_time > event['start_time']):
                return False
        return True

    def get_available_slots(self, date):
        """
        Get all available time slots on a given date.
        :param date: The date to check for available time slots, datetime.
        :return: A list of available time slots on the given date.
        """
        slots = []
        day_start = datetime.combine(date, datetime.min.time())
        day_end = datetime.combine(date, datetime.max.time())
        current_start = day_start

        for event in sorted(self.events, key=lambda x: x['start_time']):
            if event['date'].date() == date.date():
                if current_start < event['start_time']:
                    slots.append((current_start, event['start_time']))
                current_start = max(current_start, event['end_time'])

        if current_start < day_end:
            slots.append((current_start, day_end))

        return slots

    def get_upcoming_events(self, num_events):
        """
        Get the next n upcoming events.
        :param num_events: The number of upcoming events to retrieve, int.
        :return: A list of the next n upcoming events.
        """
        now = datetime.now()
        upcoming_events = sorted(
            [event for event in self.events if event['start_time'] > now],
            key=lambda x: x['start_time']
        )
        return upcoming_events[:num_events]

    @staticmethod
    def is_valid_event(event):
        """
        Validate the event dictionary.
        :param event: The event dictionary to validate.
        :return: True if valid, False otherwise.
        """
        required_keys = {'date', 'start_time', 'end_time', 'description'}
        return all(key in event for key in required_keys) and event['start_time'] < event['end_time']