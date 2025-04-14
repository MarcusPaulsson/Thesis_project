from datetime import datetime, timedelta

class CalendarUtil:
    """
    This is a class as CalendarUtil that provides functionalities to manage calendar events, schedule appointments, and perform conflict checks.
    """

    def __init__(self):
        """
        Initialize the calendar with an empty list of events.
        """
        self.events = []

    def add_event(self, event):
        """
        Add an event to the calendar.
        :param event: The event to be added to the calendar,dict.
        """
        if not isinstance(event, dict):
            raise TypeError("Event must be a dictionary.")
        
        required_keys = ['date', 'start_time', 'end_time', 'description']
        if not all(key in event for key in required_keys):
            raise ValueError(f"Event must contain the following keys: {required_keys}")
        
        if not all(isinstance(event[key], datetime) for key in ['date', 'start_time', 'end_time']):
            raise TypeError("Date, start_time, and end_time must be datetime objects.")
        
        if event['start_time'] >= event['end_time']:
            raise ValueError("Start time must be before end time.")
        
        self.events.append(event)

    def remove_event(self, event):
        """
        Remove an event from the calendar.
        :param event: The event to be removed from the calendar,dict.
        """
        try:
            self.events.remove(event)
        except ValueError:
            pass  # Event not found, do nothing

    def get_events(self, date):
        """
        Get all events on a given date.
        :param date: The date to get events for,datetime.
        :return: A list of events on the given date,list.
        """
        if not isinstance(date, datetime):
            raise TypeError("Date must be a datetime object.")
        return [event for event in self.events if event['date'].date() == date.date()]

    def is_available(self, start_time, end_time):
        """
        Check if the calendar is available for a given time slot.
        :param start_time: The start time of the time slot,datetime.
        :param end_time: The end time of the time slot,datetime.
        :return: True if the calendar is available for the given time slot, False otherwise,bool.
        """
        if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
            raise TypeError("Start time and end time must be datetime objects.")

        if start_time >= end_time:
            raise ValueError("Start time must be before end time.")

        for event in self.events:
            if event['date'].date() == start_time.date():
                if (start_time < event['end_time'] and end_time > event['start_time']):
                    return False
        return True

    def get_available_slots(self, date):
        """
        Get all available time slots on a given date.
        :param date: The date to get available time slots for,datetime.
        :return: A list of available time slots on the given date,list.
        """
        if not isinstance(date, datetime):
            raise TypeError("Date must be a datetime object.")

        available_slots = []
        start_of_day = datetime(date.year, date.month, date.day, 0, 0, 0)
        end_of_day = datetime(date.year, date.month, date.day, 23, 59, 59)
        current_time = start_of_day

        events_on_date = sorted([event for event in self.events if event['date'].date() == date.date()], key=lambda x: x['start_time'])

        for event in events_on_date:
            if current_time < event['start_time']:
                available_slots.append((current_time, event['start_time']))
            current_time = event['end_time']

        if current_time <= end_of_day:
            available_slots.append((current_time, end_of_day + timedelta(seconds=1)))

        return available_slots

    def get_upcoming_events(self, num_events):
        """
        Get the next n upcoming events from a given date.
        :param date: The date to get upcoming events from,datetime.
        :param n: The number of upcoming events to get,int.
        :return: A list of the next n upcoming events from the given date,list.
        """
        if not isinstance(num_events, int):
            raise TypeError("n must be an integer.")
        if num_events < 0:
            raise ValueError("n must be a non-negative integer.")

        now = datetime.now()
        upcoming_events = sorted([event for event in self.events if event['date'] >= now], key=lambda x: event['date'])
        return upcoming_events[:num_events]