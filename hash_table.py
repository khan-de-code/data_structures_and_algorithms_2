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

        for i in range(initial_capacity):
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
        table_index = hash(key) % len(self.table)
        table_index_list = self.table[table_index]

        for hash_table_item in table_index_list:
            if key == hash_table_item[0]:
                table_index_list.remove(hash_table_item)

        table_index_list.append([key, item])
        self.size += 1

        if self.size > self.capacity * self.resize_percentage:
            self.__resize()

    def find(self, key: str):
        table_index = hash(key) % len(self.table)
        table_index_list = self.table[table_index]

        for i, item in enumerate(table_index_list):
            if key == item[0]:
                return table_index_list[i][1]
        else:
            return None

    def remove(self, key: str):
        table_index = hash(key) % len(self.table)
        table_index_list = self.table[table_index]

        for item in table_index_list:
            if key == item[0]:
                table_index_list.remove(item)

    def __resize(self):
        self.capacity = self.capacity * 2
        temp_store_for_values = []

        for table_index_list in self.table:
            for item in table_index_list:
                temp_store_for_values.append(item)

        self.table = []
        for i in range(self.capacity):
            self.table.append([])

        self.size = 0

        for value in temp_store_for_values:
            self.add(value[0], value[1])
