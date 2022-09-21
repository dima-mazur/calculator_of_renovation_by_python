from to_sheets import main

class Calculator:
    def __init__(self, datacost: dict):
        self.datacost = datacost
        self.date_list = []
        self.value_list = []

    def date_to_int(self):
        for dt in self.datacost.values():
            date = list(dt.keys())[0]
            new_date = date[6::] + date[3:5] + date[0:2]
            self.date_list.append(new_date)

    def value_to_list(self):
        for value in self.datacost.values():
            val = list(value.values())[0]
            self.value_list.append(val)


# calc = Calculator(main())
# # calc.date_to_int()
# # print(calc.date_list)
# calc.value_to_list()
# # print(calc.date_list)
# print(calc.value_list)
# print(sum(calc.value_list))

