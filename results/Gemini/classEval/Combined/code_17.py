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
        if isinstance(event, dict):
            self.events.append(event)
        else:
            raise TypeError("Event must be a dictionary.")

    def remove_event(self, event):
        """
        Remove an event from the calendar.
        :param event: The event to be removed from the calendar,dict.
        """
        try:
            self.events.remove(event)
        except ValueError:
            pass

    def get_events(self, date):
        """
        Get all events on a given date.
        :param date: The date to get events for,datetime.
        :return: A list of events on the given date,list.
        """
        if not isinstance(date, datetime):
            raise TypeError("Date must be a datetime object.")
        return [event for event in self.events if isinstance(event, dict) and 'date' in event and event['date'].date() == date.date()]

    def is_available(self, start_time, end_time):
        """
        Check if the calendar is available for a given time slot.
        :param start_time: The start time of the time slot,datetime.
        :param end_time: The end time of the time slot,datetime.
        :return: True if the calendar is available for the given time slot, False otherwise,bool.
        """
        if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
            raise TypeError("Start time and end time must be datetime objects.")

        for event in self.events:
            if not isinstance(event, dict) or 'date' not in event or 'start_time' not in event or 'end_time' not in event:
                continue

            if event['date'].date() == start_time.date():
                if (start_time >= event['start_time'] and start_time < event['end_time']) or \
                   (end_time > event['start_time'] and end_time <= event['end_time']) or \
                   (start_time <= event['start_time'] and end_time >= event['end_time']):
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
        current_time = datetime.combine(date.date(), datetime.min.time())
        end_of_day = datetime.combine(date.date(), datetime.max.time())

        valid_events = [event for event in self.events if isinstance(event, dict) and 'start_time' in event and 'end_time' in event and 'date' in event]
        valid_events.sort(key=lambda x: x['start_time'] if 'start_time' in x else datetime.min)

        for event in self.get_events(date):
            if not isinstance(event, dict) or 'start_time' not in event or 'end_time' not in event:
                continue
            if current_time < event['start_time']:
                available_slots.append((current_time, event['start_time']))
            current_time = event['end_time']

        if current_time < end_of_day:
            available_slots.append((current_time, datetime.combine(date.date() + timedelta(days=1), datetime.min.time())))

        return available_slots

    def get_upcoming_events(self, num_events):
        """
        Get the next n upcoming events from a given date.
        :param date: The date to get upcoming events from,datetime.
        :param n: The number of upcoming events to get,int.
        :return: A list of the next n upcoming events from the given date,list.
        """
        if not isinstance(num_events, int) or num_events < 0:
            raise ValueError("Number of events must be a non-negative integer.")

        now = datetime.now()
        upcoming_events = sorted([event for event in self.events if isinstance(event, dict) and 'date' in event and event['date'] >= now], key=lambda x: x['date'] if isinstance(x, dict) and 'date' in x else now)
        return upcoming_events[:num_events]