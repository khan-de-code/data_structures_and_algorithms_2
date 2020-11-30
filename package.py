from misc import IllegalArgumentError
from _time import Time
from typing import Union


class Package():
    """Initialize a package

    Args:
        package_id (int): The id of the package
        delivery_address (str): The address the package is to be delivered to
        delivery_city (str): The city the package is to be delivered to
        delivery_state (str): The state the package is to be delivered to
        delivery_zip (int): The zip code the package is to be delivered to
        delivery_deadline (str): The deadline by which the package must be delivered
        weight (int): The weight of the package
        special_notes (str, optional): Special notes for the package. Defaults to ''.
        status (str, optional): The current status of the package. Defaults to 'in route'.

    Raises:
        IllegalArgumentError: Raised if the provided status is not a valid status
    """

    package_id: int
    delivery_address: str
    delivery_city: str
    delivery_state: str
    delivery_zip: int
    delivery_deadline: str
    weight: int
    special_notes: str
    status: str
    delivered_time: Union[Time, str]

    def __init__(self, package_id: int, delivery_address: str, delivery_city: str, delivery_state: str, delivery_zip: int, delivery_deadline: str, weight: int, special_notes='', status='in route'):
        """Initialize a package

        Args:
            package_id (int): The id of the package
            delivery_address (str): The address the package is to be delivered to
            delivery_city (str): The city the package is to be delivered to
            delivery_state (str): The state the package is to be delivered to
            delivery_zip (int): The zip code the package is to be delivered to
            delivery_deadline (str): The deadline by which the package must be delivered
            weight (int): The weight of the package
            special_notes (str, optional): Special notes for the package. Defaults to ''.
            status (str, optional): The current status of the package. Defaults to 'in route'.

        Raises:
            IllegalArgumentError: Raised if the provided status is not a valid status

        Space & Time Complexity:
            Time Complexity:
                Big-O(N)
            Space Complexity:
                Big-O(1)
        """

        statuses = ['delayed on flight', 'in route', 'delivered']

        if (status not in statuses):
            raise IllegalArgumentError(
                f"'{status}' is not a valid value for the package status")

        hour = ''
        minute = ''
        am_pm = ''
        if delivery_deadline != 'EOD':
            colon = False
            space = False
            for char in delivery_deadline:
                if char == ':':
                    colon = True
                    continue
                elif char == ' ':
                    space = True
                    continue

                if not colon and not space:
                    hour += char
                elif colon and not space:
                    minute += char
                elif colon and space:
                    am_pm += char

            hour = int(hour)
            minute = int(minute)

        self.package_id = package_id
        self.delivery_address = delivery_address
        self.delivery_city = delivery_city
        self.delivery_state = delivery_state
        self.delivery_zip = int(delivery_zip)
        self.delivery_deadline = Time(hour, minute, am_pm) if delivery_deadline != 'EOD' else 'EOD'
        self.weight = weight
        self.special_notes = special_notes
        self.status = 'delayed on flight' if 'delayed' in special_notes.lower() else status
        self.delivered_time = None

    def __str__(self):
        """Allows the object to be represented in a string value.

        Returns:
            str: The string returned for this object.

        Space & Time Complexity:
            Time Complexity:
                Big-O(1)
            Space Complexity:
                Big-O(1)
        """

        return f'{{ Package Id: {self.package_id}| Address: {self.delivery_address}, {self.delivery_city}, {self.delivery_state}, {self.delivery_zip}| Deadline: {self.delivery_deadline}| Weight: {self.weight}| Special Notes: {self.special_notes}| Status: {self.status} }}'

    def delivered(self, time: Time):
        """Sets the package's delivered_time and status.

        Args:
            time (Time): The time the package was delivered.

        Space & Time Complexity:
            Time Complexity:
                Big-O(1)
            Space Complexity:
                Big-O(1)
        """

        self.delivered_time = time
        self.status = 'delivered'

    def get_address_info(self):
        """Retrieves the address for the package.

        Returns:
            str: The address for the package.

        Space & Time Complexity:
            Time Complexity:
                Big-O(1)
            Space Complexity:
                Big-O(1)
        """

        return (self.delivery_address, self.delivery_city, self.delivery_state, self.delivery_zip)
