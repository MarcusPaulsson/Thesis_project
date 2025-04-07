from datetime import datetime, timedelta

class CalendarUtil:
    """
    A class to manage calendar events, schedule appointments, and perform conflict checks.
    """

    def __init__(self):
        """
        Initializes the calendar with an empty list of events.
        """
        self.events = []

    def add_event(self, event):
        """
        Adds an event to the calendar.

        :param event: The event to be added.  Must be a dictionary with keys:
                      'date' (datetime), 'start_time' (datetime), 'end_time' (datetime),
                      and 'description' (str).
        :raises TypeError: If event is not a dictionary.
        :raises ValueError: If event dictionary is missing required keys or if date/time values are invalid.
        """
        if not isinstance(event, dict):
            raise TypeError("Event must be a dictionary.")

        required_keys = ['date', 'start_time', 'end_time', 'description']
        if not all(key in event for key in required_keys):
            raise ValueError(f"Event dictionary missing required keys: {required_keys}")

        if not all(isinstance(event[key], datetime) for key in ['date', 'start_time', 'end_time']):
            raise ValueError("Date, start_time, and end_time must be datetime objects.")

        if event['start_time'] > event['end_time']:
            raise ValueError("Start time must be before end time.")

        self.events.append(event)

    def remove_event(self, event):
        """
        Removes an event from the calendar.  Events are compared for equality.

        :param event: The event to be removed.  Must be a dictionary matching the
                      structure used in `add_event`.
        :raises TypeError: If event is not a dictionary.
        """
        if not isinstance(event, dict):
            raise TypeError("Event must be a dictionary.")

        try:
            self.events.remove(event)
        except ValueError:
            # Event not found in the list.  No error, just don't do anything.
            pass

    def get_events(self, date):
        """
        Retrieves all events on a given date.

        :param date: The date to retrieve events for as a datetime object.
        :return: A list of events (dictionaries) occurring on the given date.
        :raises TypeError: If date is not a datetime object.
        """
        if not isinstance(date, datetime):
            raise TypeError("Date must be a datetime object.")

        return [event for event in self.events if event['date'].date() == date.date()]

    def is_available(self, start_time, end_time):
        """
        Checks if the calendar is available for a given time slot.

        :param start_time: The start time of the time slot as a datetime object.
        :param end_time: The end time of the time slot as a datetime object.
        :return: True if the calendar is available, False otherwise.
        :raises TypeError: If start_time or end_time are not datetime objects.
        :raises ValueError: If start_time is not before end_time.
        """
        if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
            raise TypeError("Start time and end time must be datetime objects.")

        if start_time >= end_time:
            raise ValueError("Start time must be before end time.")

        for event in self.events:
            if event['date'].date() == start_time.date():
                if (start_time < event['end_time'] and end_time > event['start_time']):
                    return False  # Overlap
        return True

    def get_available_slots(self, date):
        """
        Retrieves all available time slots on a given date.  Available slots
        are returned as a list of (start_time, end_time) tuples, where each
        start_time and end_time is a datetime object.

        :param date: The date to retrieve available slots for as a datetime object.
        :return: A list of (start_time, end_time) tuples representing available slots.
        :raises TypeError: If date is not a datetime object.
        """
        if not isinstance(date, datetime):
            raise TypeError("Date must be a datetime object.")

        available_slots = []
        events_on_date = self.get_events(date)
        events_on_date.sort(key=lambda event: event['start_time'])

        start_of_day = datetime(date.year, date.month, date.day, 0, 0, 0)
        end_of_day = datetime(date.year, date.month, date.day, 23, 59, 59)

        last_event_end = start_of_day

        for event in events_on_date:
            if event['start_time'] > last_event_end:
                available_slots.append((last_event_end, event['start_time']))
            last_event_end = event['end_time']

        if last_event_end < end_of_day:
            available_slots.append((last_event_end, end_of_day + timedelta(seconds=1)))

        return available_slots

    def get_upcoming_events(self, num_events):
        """
        Retrieves the next n upcoming events.  Events are sorted by date.

        :param num_events: The number of upcoming events to retrieve.
        :return: A list of the next n upcoming events.
        :raises TypeError: If num_events is not an integer.
        :raises ValueError: If num_events is negative.
        """
        if not isinstance(num_events, int):
            raise TypeError("num_events must be an integer.")

        if num_events < 0:
            raise ValueError("num_events must be non-negative.")

        self.events.sort(key=lambda event: event['date'])
        return self.events[:num_events]