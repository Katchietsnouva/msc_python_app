from datetime import datetime

current_date = datetime.now()
print(current_date)


current_date = datetime.now()
formatted_date = current_date.strftime("%d/%m/%Y/ %H:%M:%S")

print(formatted_date)
