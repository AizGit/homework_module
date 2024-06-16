import datetime
import accounting.salary
import accounting.people



if __name__ == '__main__':
    accounting.salary.calculate_salary()
    accounting.people.get_employees()
    dt = datetime.datetime.today()
    print(dt)
