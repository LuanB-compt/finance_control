from src import Finance
from src import utils

if __name__ == "__main__":
    utils.title(os_="Linux")

    monthSpends = {
        'Gym':9.9,
        'Transport':50,
        'Health':20
    }
    my_control = Finance.Finance(
        rawSalary=1100,
        porcentStore=0.4,
        porcentInvest=0.1,
        monthSpends=monthSpends,
        amountStore=200,
        todaySpends=5.5,
        pathData='./my_control.csv'
    )

    my_control.show_info()