import random

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
month = random.choice(MONTHS)


def what_to_eat(month):
    is_month_ending_with_r = month.lower().endswith("r")
    is_month_ending_with_ary = month.lower().endswith("ary")
    is_month_between_may_and_aug = 8 > MONTHS.index(month) > 4
    if is_month_ending_with_r or is_month_ending_with_ary:
        print(f"{month}: oysters")
    elif is_month_between_may_and_aug:
        print(f"{month}: tomatoes")
    else:
        print(f"{month}: asparagus")
