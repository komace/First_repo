import re
def normalize_phone(phone_number):
    cleaned_number = re.sub(r'[^\d+]', '', phone_number.strip())
    if cleaned_number.startswith('+'):
        if cleaned_number.startswith('+380'):
            return cleaned_number
        else:
            return '+38' + cleaned_number.lstrip('+')
    elif cleaned_number.startswith('380'):
            return '+' + cleaned_number    
    else:
         return '+38' + cleaned_number        

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(sanitized_numbers)