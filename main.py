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