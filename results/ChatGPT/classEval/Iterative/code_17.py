from datetime import datetime, timedelta

class CalendarUtil:
    """
    A utility class to manage calendar events, schedule appointments, and perform conflict checks.
    """

    def __init__(self):
        """
        Initialize the calendar with an empty list of events.
        """
        self.events = []

    def add_event(self, event):
        """
        Add an event to the calendar.
        :param event: The event to be added to the calendar, dict.
        """
        if self.is_valid_event(event):
            self.events.append(event)

    def remove_event(self, event):
        """
        Remove an event from the calendar.
        :param event: The event to be removed from the calendar, dict.
        """
        self.events = [e for e in self.events if e != event]

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
            if event['date'].date() == start_time.date():
                if not (end_time <= event['start_time'] or start_time >= event['end_time']):
                    return False
        return True

    def get_available_slots(self, date):
        """
        Get all available time slots on a given date.
        :param date: The date to get available time slots for, datetime.
        :return: A list of available time slots on the given date, list.
        """
        slots = []
        start_of_day = datetime(date.year, date.month, date.day, 0, 0)
        end_of_day = datetime(date.year, date.month, date.day, 23, 59)
        current_time = start_of_day

        while current_time < end_of_day:
            next_time = current_time + timedelta(hours=1)
            if self.is_available(current_time, next_time):
                slots.append((current_time, next_time))
            current_time = next_time

        return slots

    def get_upcoming_events(self, num_events):
        """
        Get the next n upcoming events from the current date.
        :param num_events: The number of upcoming events to get, int.
        :return: A list of the next n upcoming events, list.
        """
        upcoming_events = sorted(self.events, key=lambda x: (x['date'], x['start_time']))
        return upcoming_events[:num_events]

    def is_valid_event(self, event):
        """
        Validate the event structure.
        :param event: The event to be validated, dict.
        :return: True if valid, False otherwise.
        """
        required_keys = {'date', 'start_time', 'end_time', 'description'}
        return all(key in event for key in required_keys) and event['start_time'] < event['end_time']