
print('START main.py')
print()


from datetime import date
from application.salary import calculate_salary
from application.db.people import get_employees



print(f'Сегодняшняя дата - {date.today()}')
print()

if __name__ == '__main__':
    calculate_salary()
    get_employees()

print()
print('END main.py')