from lottery import Lottery

my_lottery = Lottery(my_ticket=7)
my_lottery.fill_numbers()
print('Do you have any ticket matching with this could win a prize')

my_lottery.lottery_analysis()
my_lottery.print_values()