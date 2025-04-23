from datetime import datetime, timedelta

class CalendarUtil:
    """
    A utility class for managing calendar events, scheduling appointments, and performing conflict checks.
    """

    def __init__(self):
        """
        Initializes the calendar with an empty list of events.
        """
        self.events = []

    def add_event(self, event):
        """
        Adds an event to the calendar.
        :param event: The event to be added, expected to be a dictionary with 'date', 'start_time', 'end_time', and 'description'.
        """
        self.events.append(event)

    def remove_event(self, event):
        """
        Removes an event from the calendar.
        :param event: The event to be removed, expected to be a dictionary.
        """
        self.events = [e for e in self.events if e != event]

    def get_events(self, date):
        """
        Retrieves all events on a given date.
        :param date: The date to get events for, expected to be a datetime object.
        :return: A list of events on the given date.
        """
        return [event for event in self.events if event['date'].date() == date.date()]

    def is_available(self, start_time, end_time):
        """
        Checks if the calendar is available for a given time slot.
        :param start_time: The start time of the time slot, expected to be a datetime object.
        :param end_time: The end time of the time slot, expected to be a datetime object.
        :return: True if the calendar is available for the given time slot, False otherwise.
        """
        return all(not (event['start_time'] < end_time and event['end_time'] > start_time) for event in self.events)

    def get_available_slots(self, date):
        """
        Retrieves all available time slots on a given date.
        :param date: The date to get available time slots for, expected to be a datetime object.
        :return: A list of available time slots on the given date.
        """
        slots = []
        start_of_day = datetime.combine(date, datetime.min.time())
        end_of_day = datetime.combine(date, datetime.max.time())
        current_time = start_of_day

        for event in sorted(self.events, key=lambda x: x['start_time']):
            if current_time < event['start_time']:
                slots.append((current_time, event['start_time']))
            current_time = max(current_time, event['end_time'])

        if current_time < end_of_day:
            slots.append((current_time, end_of_day))

        return slots

    def get_upcoming_events(self, num_events):
        """
        Retrieves the next n upcoming events from the current date.
        :param num_events: The number of upcoming events to retrieve, expected to be an integer.
        :return: A list of the next n upcoming events from the current date.
        """
        now = datetime.now()
        upcoming_events = [event for event in self.events if event['start_time'] > now]
        return sorted(upcoming_events, key=lambda x: x['start_time'])[:num_events]