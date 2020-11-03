from misc import IllegalArgumentError
from _time import Time
from typing import Union


class Package():
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

    def __str__(self):
        return f'{{ Package Id: {self.package_id}| Address: {self.delivery_address}, {self.delivery_city}, {self.delivery_state}, {self.delivery_zip}| Deadline: {self.delivery_deadline}| Weight: {self.weight}| Special Notes: {self.special_notes}| Status: {self.status} }}'

    def delivered(self, minutes_past_8):
        self.delivered_time = minutes_past_8
        self.status = 'delivered'

    def get_address_info(self):
        return (self.delivery_address, self.delivery_city, self.delivery_state, self.delivery_zip)
