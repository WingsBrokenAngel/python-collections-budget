from . import Expense
import matplotlib.pyplot as plt

def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()

    if divided_for_loop[0] != divided_set_comp[0] or divided_for_loop[1] != divided_set_comp[1] or divided_for_loop[2] != divided_set_comp[2]:
        print('Sets are NOT equal by == test')

    for a, b in zip(divided_for_loop, divided_set_comp):
        if not (a.issubset(b) and b.issubset(a)):
            print('Sets are NOT equal by subset test')


if __name__ == "__main__":
    main()
