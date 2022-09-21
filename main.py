import calculate
import to_nbu
import to_sheets

sheets_data = to_sheets.main()
calc = calculate.Calculator(sheets_data)
calc.date_to_int()
calc.value_to_list()

sum_of_exp = 0

for i, date in enumerate(calc.date_list):
    rate = to_nbu.get_rate(date)
    in_usd = calc.value_list[i] / rate
    sum_of_exp += in_usd

print(sum_of_exp)

