# names: list[str] = ["Alice", "Bob", "Charlie"]
# salary: list[int] = [5000, 6000, 7000]
# bonus: list[str] = ["10%", "5%", "15%"]

# print({name: (salary * float(bonus[:-1])/100) for name, salary, bonus in zip(names, salary, bonus)})


def generate_salary_dict(names_list, salaries_list, bonuses_list):
    return {name: (salary * float(bonus[:-1])/100) for name, salary, bonus in zip(names, salary, bonus)}
# names = ["Alice", "Bob", "Charlie"]
# salary = [5000, 6000, 7000]
# bonus = ["10%", "5%", "15%"]
names = ["Grace", "John", "Linda"]
salary = [6200, 5800, 7500]
bonus = ["9%", "3%", "12%"]

salary_dict = generate_salary_dict(names, salary, bonus)
print(salary_dict)