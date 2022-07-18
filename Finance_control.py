import os
import pandas as pd

class finance_control:
    importance = "'Organization is essencial to financial stability, \nand reach the your goals. Either to buy something, \nor to help someone you love.'\n"

    def __init__(self, r_s, p_sp, p_st, spends):
        self.raw_salary = r_s
        self.porcent_spend = p_sp
        self.porcent_store = p_st
        self.spend = spends

    def calc_percent(self, percent, total):
        if type(percent) == int:
            percent = percent/100
            result_percent = total * percent
            return result_percent
        elif type(percent) == float:
            result_percent = total * percent
            return result_percent

    def calc_liquid_salary(self):
        liquid_salary = self.raw_salary

        for i in enumerate(self.spend):
            liquid_salary = liquid_salary - i[0]
        liquid_salary = liquid_salary - (self.raw_salary*self.porcent_store)

        return liquid_salary

    def calc_total_spends(self):
        total_spends = 0

        for i in enumerate(self.spend):
            total_spends = total_spends + i[0]

        return total_spends

    def title():
        os.system("cls")
        print("***********************************")
        print("        LUAN FINANCE CONTROL")
        print("***********************************\n")



# ***MAIN*** 
def main():
    spend_medication = 110
    spend_doctor = 32
    spend_transport = 142
    spend_father = 150
    spend_hygienic = 50
    spend = {'medication':110, 'doctor':32, 'transport':142, 'father':150, 'hygienic':50}

    my_finance = finance_control(1100, 0.8, 0.2, spend)

    finance_control.title()
    print(finance_control.importance)

    print(f"ONE PERCENT FROM {my_finance.raw_salary}: {my_finance.calc_percent(1, my_finance.raw_salary)}")
    print("TOTAL CASH: R$", str(my_finance.raw_salary) + ".00\n")

    print(f"- TOTAL TO SPEND ({my_finance.porcent_spend*100}%): R$ {my_finance.raw_salary*my_finance.porcent_spend}0")
    print("- TOTAL EXPENDITURES:     R$", str(my_finance.calc_total_spends()) + ".00")
    print("- LIQUID SALARY: (expenditures, to store): R$", str(my_finance.calc_liquid_salary()) + "0\n")

    print(f"- TOTAL TO STORE ({my_finance.porcent_store*100}%): {my_finance.raw_salary*my_finance.porcent_store}")

if __name__ == "__main__":
    main()