import pandas as pd
import datetime



class Finance:
    """
    This class receive your finance information and do a diary control and saving a CSV with the data. 
    Therefore, you can stay the finance control, have a sense about your cash and 
    consequently know what you have to do to achieve your goals.
    """
    importance = "'Organization is essencial to financial stability,\n and reach the your goals. Either to buy something,\n or to help someone you love.'\n"

    def __init__(
        self,
        rawSalary:float,
        porcentStore:float,
        porcentInvest:float,
        monthSpends:dict,
        amountStore:float,
        todaySpends:float,
        pathData:str
    ) -> None:
        self.__rawSalary = rawSalary
        self.__porcentSpend = 1 - (porcentStore + porcentInvest)
        self.__porcentStore = porcentStore
        self.__porcentInvest = porcentInvest
        self.__amountStore = amountStore
        self.__monthSpends = monthSpends
        self.__todaySpends = todaySpends
        try:
            self.__database = pd.read_csv(filepath_or_buffer=pathData).drop(columns=['Unnamed: 0'])
            self.__update_csv(path=pathData)
        except:
            self.__createCSV(path=pathData)

    def getDatabase(self) -> pd.DataFrame():
        """
        Get the DataFrame with the month data.
        """
        return self.__database

    def getRawSalary(self) -> float:
        """
        Get the Raw Salary.
        """
        return self.__rawSalary

    def calculateMonthSpend(self) -> float:
        """
        Method to numerically calculate the month spends.
        """
        sum = 0
        for spend in self.__monthSpends.values():
            sum += spend
        return sum

    def calculateLiquidSalary(self) -> float:
        """
        Method to numerically calculate the liquid salary.
        """
        return self.__rawSalary - (
            self.calculateMonthSpend() + self.__amountStore + self.calculateInvestNumeric()
        )
    
    def calculateSpendNumeric(self) -> float:
        """
        Method to numerically calculate the amount reserved to spend.
        """
        return self.__rawSalary * self.__porcentSpend
    
    def calculateStoreNumeric(self) -> float:
        """
        Method to numerically calculate the amount reserved to store.
        """
        return self.__rawSalary * self.__porcentStore

    def calculateInvestNumeric(self) -> float:
        """
        Method to numerically calculate the amount reserved to invest.
        """
        return self.__rawSalary * self.__porcentInvest
    
    def calculateCurrentBalance(self) -> float:
        total = self.calculateLiquidSalary()
        for spend in self.__database.TodaySpends.to_list():
            total -= spend
        return total

    def show_info(self) -> None:
        """
        Method to show the info about the finances.
        """
        print('- Your raw salary: R$', self.__rawSalary, sep='')
        print('- Your amount reserved to spend: R$', self.calculateSpendNumeric(), sep='')
        print('- Your amount reserved to store: R$', self.calculateStoreNumeric(), sep='')
        print('- Your amount reserved to invest: R$', self.calculateInvestNumeric(), sep='')
        print('- Your amount stored this mounth: R$', self.__amountStore)
        print('- Your free amount to spend: R$', self.calculateLiquidSalary(), sep='')
        print('- Your current balance: R$', self.calculateCurrentBalance(), sep='')

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
        self.__database['AmountStored'] = [self.__amountStore]
        self.__database['TodaySpends'] = [self.__todaySpends]
        for spends in self.__monthSpends:
            self.__database[spends] = [self.__monthSpends[spends]]
        self.__database.set_index(keys="Date")
        self.__database.to_csv(path_or_buf=path)

    def __update_csv(self, path:str) -> None:
        """
        Update the month DataFrame/CSV and save.
        -----------------------
        Parameters:
        path: The path and name to save the CSV
        """
        new_line = [
            str(datetime.date.today()),
            self.__rawSalary,
            self.__porcentStore,
            self.__porcentInvest,
            self.__porcentSpend,
            self.__amountStore,
            self.__todaySpends
        ]
        for spend in self.__monthSpends:
            new_line.append(self.__monthSpends[spend])

        if self.__database.iloc[-1].Date == str(datetime.date.today()):
            pass
        else:
            self.__database.loc[len(self.__database)] = new_line
            self.__database.to_csv(path_or_buf=path)