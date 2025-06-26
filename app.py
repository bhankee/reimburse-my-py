from datetime import date

'''
TODOS:
- Set up data and rate logic
- Format date into date object
- Combine projects that are overlapping / next to eachother
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
    # print(date_str)
    month = split_date[0]
    day = split_date[1]
    year = split_date[2]

    return date(century + int(year), int(month), int(day))

# referenced some snippets online for help on this one below as it is one of those date util functions used often and wanted to account for leap years


def days_in_month(year, month):
    # account for leap years
    if month == 2:
        is_leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
        return 29 if is_leap else 28

    if month in (4, 6, 9, 11):
        return 30
    return 31


def next_day(this_date):

    year = this_date.year
    month = this_date.month
    day = this_date.day

    # account for last day of month
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

    # Combine projects into a list

    combined_projects = []
    # interate over lists (nested loop) and create new one with all dates in range
    for project in project_set:
        # print("project", project)
        date_range = get_date_range(
            project["start"], project["end"])
        # print("dates", dates)
        # Do not need start and end dates since we can pull from final list
        for date in date_range:
            combined_projects.append({
                "date": date,
                "city_type": project["city_type"]
            })

    return combined_projects


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

print("SET 2", project_reimbursement(SETS[1]))
print("SET 3", project_reimbursement(SETS[2]))
