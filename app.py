from datetime import date

'''
TODOS:
- Set up data and rate logic
- Format date into date object
- Combine projects that are overlapping / next to eachother
- Do math on days (costs)
- Account for last days of months
'''

# Project Data
SETS = [
    [
        {"city": "low", "start": "10/1/24", "end": "10/4/24"}
    ],
    [
        {"city": "low", "start": "10/1/24", "end": "10/1/24"},
        {"city": "high", "start": "10/2/24", "end": "10/6/24"},
        {"city": "low", "start": "10/6/24", "end": "10/9/24"}
    ],
    [
        {"city": "low", "start": "9/30/24", "end": "10/3/24"},
        {"city": "high", "start": "10/5/24", "end": "10/7/24"},
        {"city": "high", "start": "10/8/24", "end": "10/8/24"}
    ],
    [
        {"city": "low", "start": "10/1/24", "end": "10/1/24"},
        {"city": "low", "start": "10/1/24", "end": "10/1/24"},
        {"city": "high", "start": "10/2/24", "end": "10/3/24"},
        {"city": "high", "start": "10/2/24", "end": "10/6/24"}
    ]
]

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


def project_reimbursement(project_set):

    date_start = format_date(
        project_set[0]["start"])

    return date_start


# ----------------   OUTPUT   ----------------

print(project_reimbursement(SETS[0]))
