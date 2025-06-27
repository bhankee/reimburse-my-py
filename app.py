from datetime import date

'''
TODOS:
- Set up data and rate logic
- Format date into date object
- Combine projects that are overlapping / next to eachother
- Remove dups
- Do math on days (costs)
- Account for last days of months
- Add a day to have current date
'''


RATES = {
    "low": {"travel": 45, "full": 75},
    "high": {"travel": 55, "full": 85}
}

# Converts date strings to date object from 10/3/24 to 2024-10-03


def format_date(date_str):
    century = 2000
    split_date = date_str.split('/')
    month = split_date[0]
    day = split_date[1]
    year = split_date[2]

    return date(century + int(year), int(month), int(day))


def days_in_month(year, month):
    # referenced some snippets online for help on this one below as it is one of those date util functions used often and wanted to account for leap years

    if month == 2:
        is_leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
        return 29 if is_leap else 28

    if month in (4, 6, 9, 11):
        return 30
    return 31


def next_day(curr_date):
    year = curr_date.year
    month = curr_date.month
    day = curr_date.day

    current_amt_days = days_in_month(year, month)

    if day < current_amt_days:
        return date(year, month, day + 1)

    return date(year, month + 1, 1)  # first of next month


def get_date_range(date_start, date_end):
    result = []
    day = format_date(date_start)
    while day <= format_date(date_end):
        result.append(day)
        day = next_day(day)
    return result


def project_reimbursement(project_set):

    projects_combined = []
    # interate over lists (nested loop) and create new one with all dates in range
    for project in project_set:
        date_range = get_date_range(
            project["start"], project["end"])

        for date in date_range:
            projects_combined.append({
                "date": date,
                "city_type": project["city_type"]
            })

    # Create only one instance of a date and prioritize higher cost
    project_dictionary = {}
    for data in projects_combined:
        date_entry = data["date"]
        city_type = data["city_type"]
        if date_entry not in project_dictionary:
            project_dictionary[date_entry] = city_type

    # Lists
    sorted_dictionary = sorted(project_dictionary)
    project_groups = []  # for ordering date groups and getting travel days
    day_data = []  # for prioritizing high cost

    # Checking for gaps while building prject_groups if needed
    for i, sorted_date in enumerate(sorted_dictionary):

        if i > 0:
            prev_day = sorted_dictionary[i - 1]
        else:
            prev_day = None

        gap_exists = not prev_day or sorted_date != next_day(prev_day)

        if gap_exists:
            for j, next_date in enumerate(project_groups):
                is_travel = j == 0 or j == len(
                    project_groups) - 1  # first and last day travel
                day_data.append({
                    "date": next_date,
                    "type": "travel" if is_travel else "full",
                    "city_type": project_dictionary[next_date]
                })
            project_groups = []  # reset for another potential grouping

        project_groups.append(sorted_date)

    if project_groups:
        for j, next_date in enumerate(project_groups):
            is_travel = j == 0 or j == len(project_groups) - 1
            day_data.append({
                "date": next_date,
                "type": "travel" if is_travel else "full",
                "city_type": project_dictionary[next_date]
            })

    total_reimbursement = 0

    for info in day_data:
        city_type = info["city_type"]
        day_type = info["type"]
        rate = RATES[city_type][day_type]
        total_reimbursement += rate

    return total_reimbursement


# Project Data
SETS = [
    [
        {"city_type": "low", "start": "10/1/24", "end": "10/4/24"}
    ],
    [
        {"city_type": "low", "start": "10/1/24", "end": "10/1/24"},
        {"city_type": "high", "start": "10/2/24", "end": "10/6/24"},
        {"city_type": "low", "start": "10/6/24", "end": "10/9/24"}
    ],
    [
        {"city_type": "low", "start": "9/30/24", "end": "10/3/24"},
        {"city_type": "high", "start": "10/5/24", "end": "10/7/24"},
        {"city_type": "high", "start": "10/8/24", "end": "10/8/24"}
    ],
    [
        {"city_type": "low", "start": "10/1/24", "end": "10/1/24"},
        {"city_type": "low", "start": "10/1/24", "end": "10/1/24"},
        {"city_type": "high", "start": "10/2/24", "end": "10/3/24"},
        {"city_type": "high", "start": "10/2/24", "end": "10/6/24"}
    ]
]
# ----------------   OUTPUT   ----------------
for i, set in enumerate(SETS):
    print(f"SET {i+1}: ${project_reimbursement(set)} ")
