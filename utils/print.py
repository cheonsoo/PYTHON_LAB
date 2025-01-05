import json
from tabulate import tabulate
from prettytable import PrettyTable



def print_json_in_table_format(json):
    # Convert JSON data to table format
    table = tabulate(json, headers="keys", tablefmt="grid")

    # Print the table
    print(table)

def print_json_in_table_format_2(json_data):
    # Create a PrettyTable object
    table = PrettyTable()

    # Add columns to the table
    keys = json_data[0].keys()
    table.field_names = keys

    # Add rows to the table
    for item in json_data:
        table.add_row(item.values())

    # Print the table
    print(table)

# data = [
#     {"name": "Alice", "age": 30, "city": "New York"},
#     {"name": "Bob", "age": 25, "city": "Los Angeles"},
#     {"name": "Charlie", "age": 35, "city": "Chicago"}
# ]

### tabulate
# print_json_in_table_format(data)

### prettytable
# print_json_in_table_format_2(data)
