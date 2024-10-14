import random

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
month = random.choice(MONTHS)


def what_to_eat(month):
    if month.lower().endswith("r") or month.lower().endswith("ary"):
        print(f"{month}: oysters")
    elif 8 > MONTHS.index(month) > 4:
        print(f"{month}: tomatoes")
    else:
        print(f"{month}: asparagus")
