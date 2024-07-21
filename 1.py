from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    today = datetime.today().date()
    next_week = today + timedelta(days=7)
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        birthday_this_year = birthday.replace(year=today.year)

        # If birthday has already passed this year, consider next year's birthday
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        # Check if the birthday is within the next 7 days
        if today <= birthday_this_year <= next_week:
            congratulation_date = birthday_this_year
            # If birthday falls on a weekend, move it to the next Monday
            if congratulation_date.weekday() == 5:  # Saturday
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # Sunday
                congratulation_date += timedelta(days=1)
            
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })
    
    return upcoming_birthdays

users = [
    {"name" : "John Doe", "birthday" : "1985.01.23"},
    {"name" : "Jane Smith", "birthday" : "1990.01.27"},
    {"name" : "Alice Johnson", "birthday" : "1995.05.25"},
    {"name" : "Bob Brown", "birthday" : "2000.04.05"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

