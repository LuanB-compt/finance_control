import Finance

if __name__ == "__main__":
    Finance.title(os_="Linux")

    monthSpends = {
        'Spotify':9.9,
        'Convênio':50,
        'Higiêne':20,
        'Pai':150,
        'Transporte':200,
        'Recarga':35,
        'Academia':40
    }
    my_control = Finance.Finance(
        rawSalary=1300,
        porcentStore=0.33,
        porcentInvest=0,
        monthSpends=monthSpends,
        todaySpends=20,
        pathData='./my_control.csv'
    )

    my_control.show_info()