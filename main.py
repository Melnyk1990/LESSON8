print('*'*10, 'TASK 2', 10*'*')
quantity_star = int(input('Enter the number of stars from \"1" before \"6": '))

def star_line(star):
    if star<=1:
        return star
    return star * (star_line(star - 1))

print('*'*star_line(quantity_star))
print('The number of stars is equal to: ', len('*'*star_line(quantity_star)))


def test(quantity_star):
    print('\t***** TEST *****')
    nums_start = quantity_star
    nume_end =quantity_star -1


    test2 = f'star({nums_start}) 2 *->star({nume_end})= {(nums_start)*(nume_end)}\n' \
            f'star({nume_end})= {nume_end}'
    test3 = f'star({nums_start}) 3 *->star({nume_end})= {(nums_start)*((nume_end)*(nume_end-1))}\n' \
            f'star({nume_end}) 2 *->star{nume_end-1}= {(nume_end)*(nume_end-1)}\n' \
            f'star{nume_end-1} = {nume_end-1}'
    test4 = f'star({nums_start}) 4 *->star({nume_end})= {(nums_start)*((nume_end)*((nume_end-1)*(nume_end-2)))}\n' \
            f'star({nume_end}) 3 *->star({nume_end-1})= {(nume_end)*((nume_end-1)*(nume_end-2))}\n' \
            f'star({nume_end-1}) 2 *->star({nume_end-2})= {(nume_end-1)*(nume_end-2)}\n' \
            f'star({nume_end-2}) = {nume_end-2}'

    test5 = f'star({nums_start}) 5 *->star({nume_end})= {(nums_start)*((nume_end)*((nume_end-1)*((nume_end-2)*(nume_end-3))))}\n' \
            f'star({nume_end}) 4 *->star({nume_end-1})= {(nume_end)*((nume_end-1)*((nume_end-2)*(nume_end-3)))}\n' \
            f'star({nume_end-1}) 3 *->star({nume_end-2})= {(nume_end-1)*((nume_end-2)*(nume_end-3))}\n' \
            f'star({nume_end-2}) 2 *->star({nume_end-3})= {(nume_end-2)*(nume_end-3)}\n' \
            f'star({nume_end-3}) = {nume_end-3}'

    test6 = f'star({nums_start}) 6 *->star({nume_end})= {(nums_start)*(nume_end)*(nume_end-1)*((nume_end-2)*((nume_end-3)*(nume_end-4)))}\n' \
            f'star({nume_end}) 5 *->star({nume_end-1})= {(nume_end)*(nume_end-1)*((nume_end-2)*((nume_end-3)*(nume_end-4)))}\n' \
            f'star({nume_end-1}) 4 *->star({nume_end-2})= {(nume_end-1)*((nume_end-2)*((nume_end-3)*(nume_end-4)))}\n' \
            f'star({nume_end-2}) 3 *->star({nume_end-3})= {(nume_end-2)*((nume_end-3)*(nume_end-4))}\n' \
            f'star({nume_end-3}) 2 *->star({nume_end-4})= {(nume_end-3)*(nume_end-4)}\n' \
            f'star({nume_end-4}) = {nume_end-4}'

    if quantity_star == 1:
        print(f'star({nums_start})= {nums_start}')
    elif quantity_star ==2:
        print(f'{test2}')

    elif quantity_star ==3:
        print(f'{test3}')

    elif quantity_star ==4:
        print(f'{test4}')

    elif quantity_star ==5:
        print(f'{test5}')
    elif quantity_star ==6:
        print(f'{test6}')
    elif quantity_star< 1:
        print('Enter a greater number "1"')
    elif quantity_star> 6:
        print('Enter a number less than "6"')

print(test(quantity_star))
##############################################################################################
###########################################################################################


print('*'*10, 'TASK 3', 10*'*')
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

def summ_numbers(num1, num2):
    if num1>num2:
        return 0

    return num1 + summ_numbers(num1 + 1, num2)

print(summ_numbers(num1, num2))



print('''#ПРИМЕРЫ:
########################################################################
1) Если    num1 = 0;    num2 = 5;

# sum_numbers(0, 5) => 0 + sum_numbers(1, 5) =>15
# sum_numbers(1, 5) => 1 + sum_numbers(2, 5) =>15
# sum_numbers(2, 5) => 2 + sum_numbers(3, 5) =>14
# sum_numbers(3, 5) => 3 + sum_numbers(4, 5) =>12
# sum_numbers(4, 5) => 4 + sum_numbers(5, 5) =>9
# sum_numbers(5, 5) =>5

########################################################################
2) Если    num1 = -3;    num2 = 2;

# sum_numbers(-3, 2) => -3 + sum_numbers(-2, 2) =>-3
# sum_numbers(-2, 2) => -2 + sum_numbers(-1, 2) =>0
# sum_numbers(-1, 2) => -1 + sum_numbers(0, 2) => 2
# sum_numbers(0, 2) => 0 + sum_numbers(1, 2) => 3
# sum_numbers(1, 2) => 1 + sum_numbers(2, 2) => 3
# sum_numbers(2, 2) => 2
######################################################################
3) Если    num1 = -1;    num2 = 6;


# sum_numbers(-1, 6) => -1 + sum_numbers(0, 6) =>20
# sum_numbers(0, 5) => 0 + sum_numbers(1, 5) =>21
# sum_numbers(1, 5) => 1 + sum_numbers(2, 5) =>21
# sum_numbers(2, 5) => 2 + sum_numbers(3, 5) =>20
# sum_numbers(3, 5) => 3 + sum_numbers(4, 5) =>18
# sum_numbers(4, 5) => 4 + sum_numbers(5, 5) =>15
# sum_numbers(5, 5) => 5 + sum_numbers(6, 5) =>11
# sum_numbers(6, 6) =>6
######################################################################
''')
