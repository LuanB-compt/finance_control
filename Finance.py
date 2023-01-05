import os
import pandas as pd




class Finance:
    importance = "'Organization is essencial to financial stability, \nand reach the your goals. Either to buy something, \nor to help someone you love.'\n"

    def __init__(
        self,
        rawSalary:float,
        porcentStore:float,
        porcentInvest:float,
        monthSpends:dict,
        todaySpends:float,
        pathData:str
    ):
        self.__rawSalary = rawSalary
        self.__porcentSpend = 100 - (porcentStore + porcentInvest)
        self.__porcentStore = porcentStore
        self.__porcentInvest = porcentInvest
        self.__monthSpends = monthSpends
        self.__todaySpends = todaySpends
        try:
            self.__database = pd.read_csv(filepath_or_buffer=pathData).drop(columns=['Unnamed: 0'])
        except:
            self.__create_csv(path=pathData)




    # CREATE CSV
    def __create_csv(self, path:str):
        self.__database['RawSalary'] = self.__rawSalary
        self.__database['PorcentStore'] = self.__porcentStore
        self.__database['PorcentInvest'] = self.__porcentInvest
        self.__database['PorcentSpend'] = self.__porcentSpend
        self.__database['TodaySpends'] = self.__todaySpends
        self.__database = pd.DataFrame(columns=list(self.__monthSpends.keys()))
        self.__database.to_csv(path_or_buf=path)

    # UPDATE THE CSV
    def update_csv(self, spend):  
        new_line = list(spend.values())
        self.df.loc[len(self.df.index)] = new_line
        self.df.to_csv('finance_control_data.csv')
        return self.df

    # SHOW DICTS
    def show_dict(self, dict):
        for i in dict:
            print(f"\t{i}: R$ {dict[i]}")

    # PORCENT CALCULUS
    def calc_percent(self, percent, total):
        if type(percent) == int:
            percent = percent/100
            result_percent = total * percent
            return result_percent
        elif type(percent) == float:
            result_percent = total * percent
            return result_percent

    # LIQUID SALARY CALCULUS
    def calc_liquid_salary(self):
        liquid_salary = self.raw_salary

        for i in self.spend:
            liquid_salary = liquid_salary - self.spend[i]
        liquid_salary = liquid_salary - (self.raw_salary*self.porcent_store)

        return liquid_salary

    # TOTAL SPEND CALCULUS 
    def calc_total_dict(self, dict):
        total_spends = 0

        for i in dict:
            total_spends = total_spends + dict[i]

        return total_spends

    # TOTAL REST CALCULUS
    def calc_spends(self, spended):
        rest_spend = self.spend

        for i in self.spend:
            rest_spend[i] = self.spend[i] - spended[i]

        return rest_spend

    # PRINT A TITLE
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