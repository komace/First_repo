import datetime

def get_upcoming_birthdays(users):
    today = datetime.date.today()
    next_week = today + datetime.timedelta(days=7)
    upcoming_birthdays = []

    for user in users:
        # Перетворюємо дату народження з рядка у об'єкт datetime.date
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо день народження вже минув цього року, використовуємо дату наступного року
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Перевіряємо чи день народження у межах наступного тижня
        if today <= birthday_this_year <= next_week:
            # Якщо день народження припадає на вихідний, переносимо на наступний понеділок
            if birthday_this_year.weekday() >= 5:  # 5 - субота, 6 - неділя
                # Знаходимо наступний понеділок
                days_to_monday = 7 - birthday_this_year.weekday()
                birthday_this_year += datetime.timedelta(days=days_to_monday)
            
            # Додаємо результат до списку
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Тестування
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alice Brown", "birthday": "1992.07.24"},
    {"name": "Bob White", "birthday": "1993.07.25"},
    {"name": "Charlie Black", "birthday": "1994.07.26"},
    {"name": "Eve Blue", "birthday": "1995.07.27"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
