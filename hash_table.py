from typing import Union, Any


class HashTable:
    table: list
    size: int
    resize_percentage = .75
    capacity: int
    iterable_table: list

    def __init__(self, initial_capacity=10):
        self.table = []
        self.size = 0
        self.capacity = initial_capacity

        for _ in range(initial_capacity):
            self.table.append([])

    def __str__(self):
        return f'{self.table}'

    def __iter__(self):
        self.iterable_table = []

        for i in self.table:
            for x in i:
                self.iterable_table.append(x)

        for item in self.iterable_table:
            yield item[0]

    def add(self, key: str, item):
        """Adds a key pair to the hash table

        Args:
            key (str): The key
            item ([Any]): The data paired with the key
        """

        table_index = hash(key) % len(self.table)
        table_index_list = self.table[table_index]

        for hash_table_item in table_index_list:
            if key == hash_table_item[0]:
                table_index_list.remove(hash_table_item)

        table_index_list.append([key, item])
        self.size += 1

        if self.size > self.capacity * self.resize_percentage:
            self.__resize()

    def find(self, key: str) -> Union[Any, None]:
        """Finds any element in the hash table if it exists

        Args:
            key (str): The key to search for

        Returns:
            [Any, None]: Returns the key pair if it exists or None if it does not.
        """

        table_index = hash(key) % len(self.table)
        table_index_list = self.table[table_index]

        for i, item in enumerate(table_index_list):
            if key == item[0]:
                return table_index_list[i][1]
        else:
            return None

    def remove(self, key: str):
        """Removes a key pair from the hash table

        Args:
            key (str): The key for the key pair you want to remove
        """
        table_index = hash(key) % len(self.table)
        table_index_list = self.table[table_index]

        for item in table_index_list:
            if key == item[0]:
                table_index_list.remove(item)

    def values(self) -> [Any]:
        """Returns a list of all values present in the hashtable.
        """

        if hasattr(self, 'iterable_table'):
            return [value[1] for value in self.iterable_table]
        else:
            self.iterable_table = []

            for i in self.table:
                for x in i:
                    self.iterable_table.append(x)

            return [value[1] for value in self.iterable_table]

    def __resize(self):
        self.capacity = self.capacity * 2
        temp_store_for_values = []

        for table_index_list in self.table:
            for item in table_index_list:
                temp_store_for_values.append(item)

        self.table = []
        for _ in range(self.capacity):
            self.table.append([])

        self.size = 0

        for value in temp_store_for_values:
            self.add(value[0], value[1])
