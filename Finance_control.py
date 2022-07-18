import os
import pandas as pd

class finance_control:
    importance = "'Organization is essencial to financial stability, \nand reach the your goals. Either to buy something, \nor to help someone you love.'\n"

    def __init__(self, r_s, p_sp, p_st, spends):
        self.raw_salary = r_s
        self.porcent_spend = p_sp
        self.porcent_store = p_st
        self.spend = spends

    def show_dict(self, dict):
        for i in dict:
            print(f"\t{i}: R$ {dict[i]}")

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

        for i in self.spend:
            liquid_salary = liquid_salary - self.spend[i]
        liquid_salary = liquid_salary - (self.raw_salary*self.porcent_store)

        return liquid_salary

    def calc_total_dict(self, dict):
        total_spends = 0

        for i in dict:
            total_spends = total_spends + dict[i]

        return total_spends

    def calc_spends(self, spended):
        rest_spend = self.spend

        for i in self.spend:
            rest_spend[i] = self.spend[i] - spended[i]

        return rest_spend

    def title(so):
        if so == "windows":
            os.system("cls")
            print("***********************************")
            print("        LUAN FINANCE CONTROL")
            print("***********************************\n")
        elif so == "linux":
            os.system("clear")
            print("***********************************")
            print("        LUAN FINANCE CONTROL")
            print("***********************************\n")