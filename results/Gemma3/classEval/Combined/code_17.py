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
        self.events.append(event)

    def remove_event(self, event):
        """
        Remove an event from the calendar.
        :param event: The event to be removed from the calendar,dict.
        """
        self.events = [e for e in self.events if e != event]

    def get_events(self, date):
        """
        Get all events on a given date.
        :param date: The date to get events for,datetime.
        :return: A list of events on the given date,list.
        """
        return [event for event in self.events if event['date'].date() == date.date()]

    def is_available(self, start_time, end_time):
        """
        Check if the calendar is available for a given time slot.
        :param start_time: The start time of the time slot,datetime.
        :param end_time: The end time of the time slot,datetime.
        :return: True if the calendar is available for the given time slot, False otherwise,bool.
        """
        for event in self.events:
            if (start_time < event['end_time'] and end_time > event['start_time']):
                return False
        return True

    def get_available_slots(self, date):
        """
        Get all available time slots on a given date.
        :param date: The date to get available time slots for,datetime.
        :return: A list of available time slots on the given date,list.
        """
        events_on_date = self.get_events(date)
        events_on_date.sort(key=lambda x: x['start_time'])
        available_slots = []
        start_of_day = datetime(date.year, date.month, date.day, 0, 0)
        end_of_day = datetime(date.year, date.month, date.day, 23, 59)

        if not events_on_date:
            available_slots.append((start_of_day, end_of_day))
            return available_slots

        if start_of_day < events_on_date[0]['start_time']:
            available_slots.append((start_of_day, events_on_date[0]['start_time']))

        for i in range(len(events_on_date) - 1):
            available_slots.append((events_on_date[i]['end_time'], events_on_date[i + 1]['start_time']))

        if events_on_date[-1]['end_time'] < end_of_day:
            available_slots.append((events_on_date[-1]['end_time'], end_of_day))

        return available_slots

    def get_upcoming_events(self, date, num_events):
        """
        Get the next n upcoming events from a given date.
        :param date: The date to get upcoming events from,datetime.
        :param n: The number of upcoming events to get,int.
        :return: A list of the next n upcoming events from the given date,list.
        """
        upcoming_events = [event for event in self.events if event['start_time'] > date]
        upcoming_events.sort(key=lambda x: x['start_time'])
        return upcoming_events[:num_events]