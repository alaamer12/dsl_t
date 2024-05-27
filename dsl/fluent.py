class QueryBuilder:
    def __init__(self):
        self.query = ""

    def select(self, *fields):
        self.query = f"SELECT {', '.join(fields)}"
        return self

    def from_table(self, table):
        self.query += f" FROM {table}"
        return self

    def where(self, condition):
        self.query += f" WHERE {condition}"
        return self

    def build(self):
        return self.query

# Example usage
query = (
    QueryBuilder()
    .select("id", "name")
    .from_table("users")
    .where("age > 21")
    .build()
)

print(query)  # Output: SELECT id, name FROM users WHERE age > 21
