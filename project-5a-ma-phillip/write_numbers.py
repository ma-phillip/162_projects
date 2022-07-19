number_list = ['25','34','25','55']

with open('numbers.txt', 'w') as numbers:
    for number in number_list:
        numbers.write(str(number) + '\n')
