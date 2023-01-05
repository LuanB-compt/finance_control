import os
import pandas as pd
import datetime




def title(os_:str) -> None:
    """
    Clean the terminal with 'cls' (windows) or 'clear' (linux) and show the program title.
    ------------------------
    Parameters:
    os: Operational System that will runing the program
    """
    if os_.upper() == "WINDOWS":
        os.system("cls")
        print("***********************************")
        print("        LUAN FINANCE CONTROL")
        print("***********************************\n")
    elif os_.upper() == "LINUX":
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
            self.__update_csv()
        except:
            self.__createCSV(path=pathData)



    def getDatabase(self) -> pd.DataFrame():
        """
        Get the DataFrame with the month data
        """
        return self.__database



    def __update_csv(self) -> None:  
        new_line = [
            datetime.date.today(),
            self.__rawSalary,
            self.__porcentStore,
            self.__porcentInvest,
            self.__porcentSpend,
            self.__todaySpends
        ]
        for spend in self.__monthSpends:
            new_line.append(self.__monthSpends[spend])

        print('\n', self.__database.loc[-1, 'Date'], '\n')
        #self.df.loc[len(self.df.index)] = new_line
        #self.df.to_csv('finance_control_data.csv')


    def __createCSV(self, path:str) -> None:
        """
        Create the month DataFrame and CSV if don't exist.
        -----------------------
        Parameters:
        path: The path and name to save the CSV
        """
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