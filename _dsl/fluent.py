class DataProcessor:
    def __init__(self, data):
        self.data = data

    def select(self, *columns):
        self.data = [{col: row[col] for col in columns} for row in self.data]
        return self

    def filter(self, condition):
        self.data = [row for row in self.data if condition(row)]
        return self

    def group_by(self, *columns):
        grouped_data = {}
        for row in self.data:
            key = tuple(row[col] for col in columns)
            grouped_data.setdefault(key, []).append(row)
        self.data = grouped_data
        return self

    def aggregate(self, agg_func):
        if isinstance(self.data, dict):  # Grouped data
            self.data = {key: agg_func(rows) for key, rows in self.data.items()}
        else:
            self.data = agg_func(self.data)
        return self

    def get_result(self):
        return self.data

# Example usage:
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "New York"}
]

result = (
    DataProcessor(data)
    .select("name", "age")
    .filter(lambda row: row["age"] > 25)
    # .group_by("city")
    .aggregate(lambda rows: len(rows))
    .get_result()
)

print(result)
