from datetime import datetime, timedelta

class CalendarUtil:
    """
    A class that provides functionalities to manage calendar events,
    schedule appointments, and perform conflict checks.
    """

    def __init__(self):
        """Initialize the calendar with an empty list of events."""
        self.events = []

    def add_event(self, event):
        """
        Add an event to the calendar.
        :param event: The event to be added to the calendar, dict.
        """
        self.events.append(event)

    def remove_event(self, event):
        """
        Remove an event from the calendar.
        :param event: The event to be removed from the calendar, dict.
        """
        if event in self.events:
            self.events.remove(event)

    def get_events(self, date):
        """
        Get all events on a given date.
        :param date: The date to get events for, datetime.
        :return: A list of events on the given date, list.
        """
        return [event for event in self.events if event['date'].date() == date.date()]

    def is_available(self, start_time, end_time):
        """
        Check if the calendar is available for a given time slot.
        :param start_time: The start time of the time slot, datetime.
        :param end_time: The end time of the time slot, datetime.
        :return: True if the calendar is available for the given time slot, False otherwise, bool.
        """
        for event in self.events:
            if (event['start_time'] < end_time and event['end_time'] > start_time):
                return False
        return True

    def get_available_slots(self, date):
        """
        Get all available time slots on a given date.
        :param date: The date to get available time slots for, datetime.
        :return: A list of available time slots on the given date, list.
        """
        day_start = datetime.combine(date.date(), datetime.min.time())
        day_end = datetime.combine(date.date(), datetime.max.time())
        busy_slots = [(event['start_time'], event['end_time']) for event in self.get_events(date)]
        
        if not busy_slots:
            return [(day_start, day_end)]

        available_slots = []
        current_start = day_start

        for start, end in sorted(busy_slots):
            if current_start < start:
                available_slots.append((current_start, start))
            current_start = max(current_start, end)

        if current_start < day_end:
            available_slots.append((current_start, day_end))

        return available_slots

    def get_upcoming_events(self, num_events):
        """
        Get the next n upcoming events from the current date.
        :param num_events: The number of upcoming events to get, int.
        :return: A list of the next n upcoming events from the current date, list.
        """
        now = datetime.now()
        upcoming_events = [event for event in self.events if event['start_time'] > now]
        return sorted(upcoming_events, key=lambda x: x['start_time'])[:num_events]