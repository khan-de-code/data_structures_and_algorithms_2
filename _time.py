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

    def add_time(self, hour=None, minute=None, fractions_of_a_minute=None):
        """Adds to the existing time

        Args:
            hour (int, optional): The Hour. Defaults to None.
            minute (int, optional): The Minute. Defaults to None.
            fractions_of_a_minute (float, optional): Fractions of a minute. Defaults to None.
        """

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
