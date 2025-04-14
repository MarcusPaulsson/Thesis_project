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
        return [event for event in self.events if event['date'].date() == date.date()]

    def is_available(self, start_time, end_time):
        """
        Check if the calendar is available for a given time slot.
        :param start_time: The start time of the time slot,datetime.
        :param end_time: The end time of the time slot,datetime.
        :return: True if the calendar is available for the given time slot, False otherwise,bool.
        """
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
        available_slots = []
        current_time = datetime.combine(date.date(), datetime.min.time())
        end_of_day = datetime.combine(date.date(), datetime.max.time())

        self.events.sort(key=lambda x: x['start_time'])

        if not self.events:
            available_slots.append((current_time, end_of_day + timedelta(seconds=1)))
            return available_slots
        
        if self.events[0]['date'].date() != date.date():
            available_slots.append((current_time, end_of_day + timedelta(seconds=1)))
            return available_slots

        
        occupied_slots = []
        for event in self.events:
            if event['date'].date() == date.date():
                occupied_slots.append((event['start_time'], event['end_time']))

        if not occupied_slots:
            available_slots.append((current_time, end_of_day + timedelta(seconds=1)))
            return available_slots

        occupied_slots.sort()
        
        if current_time < occupied_slots[0][0]:
            available_slots.append((current_time, occupied_slots[0][0]))
        
        for i in range(len(occupied_slots) - 1):
            available_slots.append((occupied_slots[i][1], occupied_slots[i+1][0]))
        
        if occupied_slots[-1][1] < end_of_day + timedelta(seconds=1):
            available_slots.append((occupied_slots[-1][1], end_of_day + timedelta(seconds=1)))
        
        return available_slots

    def get_upcoming_events(self, num_events):
        """
        Get the next n upcoming events from a given date.
        :param date: The date to get upcoming events from,datetime.
        :param n: The number of upcoming events to get,int.
        :return: A list of the next n upcoming events from the given date,list.
        """
        upcoming_events = []
        now = datetime.now()
        
        sorted_events = sorted(self.events, key=lambda x: x['date'])
        
        for event in sorted_events:
            if event['date'] > now:
                upcoming_events.append(event)
        
        return upcoming_events[:num_events]