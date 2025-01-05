from utils.utils import get_start_end_of_month
from utils.print import print_json_in_table_format

start_day, end_day = get_start_end_of_month(2024, 12)
print (f'''
### start_day: {start_day}
### end_day: {end_day}
''')

# data = [
#     {"name": "Alice", "age": 30, "city": "New York"},
#     {"name": "Bob", "age": 25, "city": "Los Angeles"},
#     {"name": "Charlie", "age": 35, "city": "Chicago"}
# ]
data = [
  { "Group": "Detail", "Tickets": 50, "Deploy": 30 },
  { "Group": "Registration", "Tickets": 80, "Deploy": 30 },
  { "Group": "Attribute", "Tickets": 40, "Deploy": 30 },
  { "Group": "FrontEnd", "Tickets": 70, "Deploy": 30 },
  { "Group": "UI", "Tickets": 100, "Deploy": 30 }
]
print_json_in_table_format(data) ### tabulate