from misc import IllegalArgumentError


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
    delivered_time: int

    def __init__(self, package_id: int, delivery_address: str, delivery_city: str, delivery_state: str, delivery_zip: int, delivery_deadline: str, weight: int, special_notes='', status='in route'):
        statuses = ['delayed on flight', 'in route', 'delivered']

        if (status not in statuses):
            raise IllegalArgumentError(
                f"'{status}' is not a valid value for the package status")

        self.package_id = package_id
        self.delivery_address = delivery_address
        self.delivery_city = delivery_city
        self.delivery_state = delivery_state
        self.delivery_zip = int(delivery_zip)
        self.delivery_deadline = delivery_deadline
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
