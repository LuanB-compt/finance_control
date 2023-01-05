import Finance

if __name__ == "__main__":
    Finance.title(os_="Linux")

    monthSpends = {
        'Spotify':9.9,
        'Convênio':50,
        'Higiêne':20,
        'Pai':150,
        'Transporte':200
    }
    my_control = Finance.Finance(
        rawSalary=1200,
        porcentStore=0.33,
        porcentInvest=0,
        monthSpends=monthSpends,
        todaySpends=0,
        pathData='./my_control.csv'
    )

    print(my_control.getDatabase())
    print(my_control.calculateLiquidSalary())
    print(my_control.calculateSpendNumeric())
    print(my_control.calculateStoreNumeric())
    print(my_control.calculateInvestNumeric())