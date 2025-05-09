class TimeInterval:
    """
    Represents a time interval with hours, minutes, and seconds.
    """

    def __init__(self, hours=0, minutes=0, seconds=0):
        """
        Initializes a TimeInterval object using keyword arguments.

        Args:
            hours (int, optional): The number of hours. Defaults to 0.
            minutes (int, optional): The number of minutes. Defaults to 0.
            seconds (int, optional): The number of seconds. Defaults to 0.

        Raises:
            TypeError: If any of the keyword arguments are not integers.
        """
        if not all(isinstance(arg, int) for arg in [hours, minutes, seconds]):
            raise TypeError("Hours, minutes, and seconds must be integers.")

        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
        self._normalize()

    def _normalize(self):
        """
        Normalizes the time interval so that seconds and minutes are within [0, 59].
        """
        self.minutes += self.seconds // 60
        self.seconds %= 60
        self.hours += self.minutes // 60
        self.minutes %= 60

    def __str__(self):
        """
        Returns a string representation of the time interval in HH:MM:SS format.
        """
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __add__(self, other):
        """
        Adds two TimeInterval objects.

        Args:
            other (TimeInterval): The TimeInterval object to add.

        Returns:
            TimeInterval: A new TimeInterval object representing the sum.

        Raises:
            TypeError: If 'other' is not a TimeInterval object.
        """
        if not isinstance(other, TimeInterval):
            raise TypeError("Can only add TimeInterval objects.")
        total_seconds = (self.hours + other.hours) * 3600 + \
                        (self.minutes + other.minutes) * 60 + \
                        (self.seconds + other.seconds)
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return TimeInterval(hours=hours, minutes=minutes, seconds=seconds)

    def __sub__(self, other):
        """
        Subtracts another TimeInterval object from this one.

        Args:
            other (TimeInterval): The TimeInterval object to subtract.

        Returns:
            TimeInterval: A new TimeInterval object representing the difference.

        Raises:
            TypeError: If 'other' is not a TimeInterval object.
            ValueError: If the subtraction results in a negative time interval.
        """
        if not isinstance(other, TimeInterval):
            raise TypeError("Can only subtract TimeInterval objects.")
        total_seconds_self = self.hours * 3600 + self.minutes * 60 + self.seconds
        total_seconds_other = other.hours * 3600 + other.minutes * 60 + other.seconds
        difference_seconds = total_seconds_self - total_seconds_other
        if difference_seconds < 0:
            raise ValueError("Subtraction results in a negative time interval.")
        hours = difference_seconds // 3600
        minutes = (difference_seconds % 3600) // 60
        seconds = difference_seconds % 60
        return TimeInterval(hours=hours, minutes=minutes, seconds=seconds)

    def __mul__(self, scalar):
        """
        Multiplies the TimeInterval object by an integer scalar.

        Args:
            scalar (int): The integer scalar to multiply by.

        Returns:
            TimeInterval: A new TimeInterval object representing the product.

        Raises:
            TypeError: If 'scalar' is not an integer.
        """
        if not isinstance(scalar, int):
            raise TypeError("Can only multiply by an integer.")
        total_seconds = (self.hours * 3600 + self.minutes * 60 + self.seconds) * scalar
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return TimeInterval(hours=hours, minutes=minutes, seconds=seconds)

    def multiply(self, scalar):
        """
        Multiplies the TimeInterval object by an integer scalar.
        This is an alternative method to __mul__.

        Args:
            scalar (int): The integer scalar to multiply by.

        Returns:
            TimeInterval: A new TimeInterval object representing the product.

        Raises:
            TypeError: If 'scalar' is not an integer.
        """
        return self.__mul__(scalar)

    def add_interval(self, other):
        """
        Adds another TimeInterval object to this one.
        This is an alternative method to __add__.

        Args:
            other (TimeInterval): The TimeInterval object to add.

        Returns:
            TimeInterval: A new TimeInterval object representing the sum.

        Raises:
            TypeError: If 'other' is not a TimeInterval object.
        """
        return self.__add__(other)

    def subtract_interval(self, other):
        """
        Subtracts another TimeInterval object from this one.
        This is an alternative method to __sub__.

        Args:
            other (TimeInterval): The TimeInterval object to subtract.

        Returns:
            TimeInterval: A new TimeInterval object representing the difference.

        Raises:
            TypeError: If 'other' is not a TimeInterval object.
            ValueError: If the subtraction results in a negative time interval.
        """
        return self.__sub__(other)

    def add_seconds(self, seconds):
        """
        Adds a specified number of seconds to this TimeInterval object.

        Args:
            seconds (int): The number of seconds to add.

        Returns:
            TimeInterval: A new TimeInterval object representing the sum.
        """
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds + seconds

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return TimeInterval(hours=hours, minutes=minutes, seconds=seconds)

    def subtract_seconds(self, seconds):
        """
        Subtracts a specified number of seconds from this TimeInterval object.

        Args:
            seconds (int): The number of seconds to subtract.

        Returns:
            TimeInterval: A new TimeInterval object representing the difference.
        """
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds - seconds
        if total_seconds < 0:
            raise ValueError("Subtraction results in a negative time interval.")
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return TimeInterval(hours=hours, minutes=minutes, seconds=seconds)