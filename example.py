from Finance_control import finance_control

# ***MAIN*** 
def main():
    spend = {'Medication':110, 'Doctor':32, 'Transport':142}
    spended = {'Medication':110, 'Doctor':64, 'Transport':100}

    my_finance = finance_control(1100, 0.75, 0.25, spend)

    finance_control.title('windows')
    print(finance_control.importance)

    print(f"ONE PERCENT FROM {my_finance.raw_salary}: {my_finance.calc_percent(1, my_finance.raw_salary)}")
    print("TOTAL CASH: R$", str(my_finance.raw_salary) + ".00\n")

    print(f"- TOTAL TO SPEND ({my_finance.porcent_spend*100}%): R$ {my_finance.raw_salary*my_finance.porcent_spend}0")
    print("- TOTAL EXPENDITURES:     R$", str(my_finance.calc_total_dict(spend)) + ".00")
    print("- LIQUID SALARY: (expenditures, to store): R$", str(my_finance.calc_liquid_salary()) + "0\n")

    print(f"- TOTAL TO STORE ({my_finance.porcent_store*100}%): {my_finance.raw_salary*my_finance.porcent_store}\n")

    print("- PAYS FIXED:")
    print(my_finance.show_dict(spend))
    print("- ALREDY SPENDED:")
    print(my_finance.show_dict(my_finance.calc_spends(spended)))

if __name__ == "__main__":
    main()