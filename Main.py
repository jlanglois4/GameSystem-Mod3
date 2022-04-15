from Grades import Grades
from Hours import Hours


def get_grades(grade_count):
    return int(input(f"How many {grade_count} did you earn last semester? "))


def get_hours(hour_type):
    return int(input(f"How many hours of {hour_type}? "))


grades = Grades(float(input("How much is the system? ")), get_grades('A'), get_grades('B'), get_grades('C'))
hours = Hours(get_hours("homework"), get_hours("chores"), get_hours("sports"))

print("--------------")
if grades.can_buy_console():
    print("You may buy a game system")
else:
    print("You do not have enough for a game system")
print(f"You have earned {hours.get_reward_total()} hours of playtime")
