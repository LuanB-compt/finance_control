from Finance import Finance

if __name__ == "__main__":
    monthSpends = {
        'Spotify':9.9,
        'Convênio':50,
        'Higiêne':20
    }
    my_control = Finance(
        rawSalary=1200,
        porcentStore=0.33,
        porcentInvest=0,
        monthSpends=monthSpends,
        todaySpends=0,
        pathData='.\my_control.csv'
    )