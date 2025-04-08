from datetime import datetime, timedelta

class CalendarUtil:
    """
    A class for managing calendar events, scheduling appointments, and performing conflict checks.
    """

    def __init__(self):
        """
        Initializes the calendar with an empty list of events.
        """
        self.events = []

    def add_event(self, event):
        """
        Adds an event to the calendar.

        :param event: A dictionary representing the event, containing keys like 'date', 'start_time', 'end_time', and 'description'.
        :raises TypeError: if event is not a dictionary.
        :raises ValueError: if event dictionary is missing required keys.
        """
        if not isinstance(event, dict):
            raise TypeError("Event must be a dictionary.")

        required_keys = ['date', 'start_time', 'end_time', 'description']
        if not all(key in event for key in required_keys):
            raise ValueError(f"Event dictionary must contain the following keys: {required_keys}")

        self.events.append(event)

    def remove_event(self, event):
        """
        Removes an event from the calendar.

        :param event: A dictionary representing the event to be removed.
        """
        try:
            self.events.remove(event)
        except ValueError:
            # Event not found in the list, no action needed
            pass

    def get_events(self, date):
        """
        Retrieves all events on a given date.

        :param date: The date for which to retrieve events (datetime object).
        :return: A list of event dictionaries occurring on the specified date.
        """
        return [event for event in self.events if event['date'].date() == date.date()]

    def is_available(self, start_time, end_time):
        """
        Checks if the calendar is available for a given time slot.

        :param start_time: The start time of the time slot (datetime object).
        :param end_time: The end time of the time slot (datetime object).
        :return: True if the time slot is available, False otherwise.
        """
        for event in self.events:
            if event['date'].date() == start_time.date():
                if (event['start_time'] <= start_time < event['end_time']) or \
                   (event['start_time'] < end_time <= event['end_time']) or \
                   (start_time <= event['start_time'] and end_time >= event['end_time']):
                    return False
        return True

    def get_available_slots(self, date):
        """
        Retrieves all available time slots on a given date.

        :param date: The date for which to retrieve available time slots (datetime object).
        :return: A list of tuples, where each tuple represents an available time slot (start_time, end_time).
        """
        available_slots = []
        current_time = datetime(date.year, date.month, date.day, 0, 0, 0)
        end_of_day = datetime(date.year, date.month, date.day, 23, 59, 59)

        sorted_events = sorted([event for event in self.events if event['date'].date() == date.date()], key=lambda x: x['start_time'])

        if not sorted_events:
            available_slots.append((current_time, datetime(date.year, date.month, date.day + 1, 0, 0, 0)))
            return available_slots

        if current_time < sorted_events[0]['start_time']:
            available_slots.append((current_time, sorted_events[0]['start_time']))

        for i in range(len(sorted_events) - 1):
            if sorted_events[i]['end_time'] < sorted_events[i+1]['start_time']:
                available_slots.append((sorted_events[i]['end_time'], sorted_events[i+1]['start_time']))

        if sorted_events[-1]['end_time'] < datetime(date.year, date.month, date.day + 1, 0, 0, 0):
             available_slots.append((sorted_events[-1]['end_time'], datetime(date.year, date.month, date.day + 1, 0, 0, 0)))

        return available_slots

    def get_upcoming_events(self, num_events):
        """
        Retrieves the next n upcoming events from the current date and time.

        :param num_events: The number of upcoming events to retrieve.
        :return: A list of the next n upcoming event dictionaries, sorted by date.
        """
        now = datetime.now()
        upcoming_events = sorted([event for event in self.events if event['date'] >= now], key=lambda x: x['date'])
        return upcoming_events[:num_events]