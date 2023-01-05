import os
import pandas as pd
import datetime




def title(so:str) -> None:
    if so.upper() == "WINDOWS":
        os.system("cls")
        print("***********************************")
        print("        LUAN FINANCE CONTROL")
        print("***********************************\n")
    elif so.upper() == "LINUX":
        os.system("clear")
        print("***********************************")
        print("        LUAN FINANCE CONTROL")
        print("***********************************\n")




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
            self.__createCSV(path=pathData)




    def getDatabase(self) -> pd.DataFrame():
        return self.__database



    def update_csv(self, spend):  
        new_line = list(spend.values())
        self.df.loc[len(self.df.index)] = new_line
        self.df.to_csv('finance_control_data.csv')
        return self.df



    def __createCSV(self, path:str) -> None:
        self.__database = pd.DataFrame()
        self.__database['Date'] = [datetime.date.today()]
        self.__database['RawSalary'] = [self.__rawSalary]
        self.__database['PorcentStore'] = [self.__porcentStore]
        self.__database['PorcentInvest'] = [self.__porcentInvest]
        self.__database['PorcentSpend'] = [self.__porcentSpend]
        self.__database['TodaySpends'] = [self.__todaySpends]
        for spends in self.__monthSpends:
            self.__database[spends] = [self.__monthSpends[spends]]
        self.__database.set_index(keys="Date")
        self.__database.to_csv(path_or_buf=path)

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