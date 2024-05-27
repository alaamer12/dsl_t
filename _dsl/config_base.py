class QueryBase:
    def __init__(self, data):
        self.data = data

    def filter(self, condition):
        self.data = [row for row in self.data if condition(row)]
        return self

    def select(self, *columns):
        self.data = [{col: row[col] for col in columns} for row in self.data]
        return self

class UserQuery(QueryBase):
    pass

# Example usage:
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

query = UserQuery(data).filter(lambda x: x["age"] > 25).select("name")
print(query.data)  # Output: [{'name': 'Alice'}, {'name': 'Charlie'}]
