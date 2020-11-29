class Time:
    """Initializes a time object

    Args:
        hour (int): The Hour
        minute (int): The Minute
        am_pm (str): AM or PM
    """

    hour: int
    minute: int
    am_pm: str
    minutes_from_8: int
    fractions_of_a_minute: float

    def __init__(self, hour: int, minute: int, am_pm: str, fractions_of_a_minute=0.0):
        self.hour = hour
        self.minute = minute
        self.am_pm = am_pm
        self.minutes_from_8 = 0
        self.fractions_of_a_minute = fractions_of_a_minute

        self.__minutes_from_8()

    def update_time(self, hour=None, minute=None, am_pm=None, fractions_of_a_minute=None):
        """Updates the time

        Args:
            hour (int, optional): The Hour. Defaults to None.
            minute (int, optional): The Minute. Defaults to None.
            am_pm (str, optional): AM or PM. Defaults to None.
            fractions_of_a_minute (float, optional): Fractions of a minute. Defaults to None.
        """

        if hour != None:
            self.hour = hour

        if minute != None:
            self.minute = minute

        if am_pm != None:
            self.am_pm = am_pm

        if fractions_of_a_minute != None:
            self.fractions_of_a_minute = fractions_of_a_minute

        self.__minutes_from_8()

    def add_time(self, hour=None, minute=None, fractions_of_a_minute=None, minutes_with_fractions=None):
        """Adds to the existing time

        Args:
            hour (int, optional): The Hour. Defaults to None.
            minute (int, optional): The Minute. Defaults to None.
            fractions_of_a_minute (float, optional): Fractions of a minute. Defaults to None.
            minutes_with_fractions (float, optional): Minutes with fractions of a minute. Defaults to None.
        """
        if (minutes_with_fractions != None and minute == None and fractions_of_a_minute == None):
            minute = int(minutes_with_fractions)
            fractions_of_a_minute = minutes_with_fractions - minute

        if fractions_of_a_minute != None:
            self.minute += int(self.fractions_of_a_minute + fractions_of_a_minute)
            self.fractions_of_a_minute = fractions_of_a_minute - int(fractions_of_a_minute)

        if minute != None:
            self.minute += minute

        if self.minute > 60:
            hours_to_add = self.minute // 60
            self.minute = self.minute % 60
            self.hour += hours_to_add

        if hour != None:
            self.hour += hour

        if self.hour > 12 and self.am_pm == 'AM':
            self.hour = self.hour - 12
            self.am_pm = 'PM'
        elif self.hour > 12 and self.am_pm == 'PM':
            self.hour = self.hour - 12
            self.am_pm = 'AM'

        self.__minutes_from_8()

    def clone(self):
        """Returns a clone of the current Time object.

        Returns:
            Time: A clone of the current Time object
        """

        return Time(self.hour, self.minute, self.am_pm, self.fractions_of_a_minute)

    def __minutes_from_8(self):
        self.minutes_from_8 = ((self.hour - 8) * 60) + self.minute

        if self.am_pm == 'PM':
            self.minutes_from_8 += 12 * 60

    def __str__(self):
        hour = self.hour if self.hour > 9 else f'0{self.hour}'
        minute = self.minute if self.minute > 9 else f'0{self.minute}'
        return f'{hour}:{minute} {self.am_pm}'

    def __eq__(self, other):
        if isinstance(other, Time):
            return self.hour == other.hour and self.minute == other.minute and self.am_pm == other.am_pm
        return False

    def __gt__(self, other):
        if isinstance(other, Time):
            if self.am_pm == 'AM' and other.am_pm == 'PM':
                return False
            elif self.am_pm == 'PM' and other.am_pm == 'AM':
                return True

            if self.am_pm == other.am_pm:
                if self.hour != other.hour:
                    return self.hour > other.hour
                elif self.minute != other.minute:
                    return self.minute > other.minute

            return False

    def __ge__(self, other):
        if isinstance(other, Time):
            return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Time):
            if self.am_pm == 'AM' and other.am_pm == 'PM':
                return True
            elif self.am_pm == 'PM' and other.am_pm == 'AM':
                return False

            if self.am_pm == other.am_pm:
                if self.hour != other.hour:
                    return self.hour < other.hour
                elif self.minute != other.minute:
                    return self.minute < other.minute

            return False

    def __le__(self, other):
        if isinstance(other, Time):
            return self.__lt__(other) or self.__eq__(other)
