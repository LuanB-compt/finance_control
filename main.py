import Finance

if __name__ == "__main__":
    Finance.title(so="Windows")
    
    monthSpends = {
        'Spotify':9.9,
        'Convênio':50,
        'Higiêne':20
    }
    my_control = Finance.Finance(
        rawSalary=1200,
        porcentStore=0.33,
        porcentInvest=0,
        monthSpends=monthSpends,
        todaySpends=0,
        pathData='.\my_control.csv'
    )

    print(my_control.getDatabase())