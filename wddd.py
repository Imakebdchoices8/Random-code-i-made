menu_prices={
    1:2.5,
    2:2.0,
    3:1.5
}
total_price=0
print("      Food store")
print("         menu")
print('=========================')
print('1)burger 2)fries 3)coke')
order=int(input('enter order 1st item: '))
if order in menu_prices:
    total_price += menu_prices[order]

order2=int(input('enter 2nd item, if none input 0: '))
if order2 in menu_prices:
    total_price += menu_prices[order]

if order2==0:
    print('order completed')
elif order2>=0:
    order3=int(input('input 3rd item: '))
    if order3 in menu_prices:
        total_price += menu_prices[order]
    print('order completed')
print('the total sum of your order cost is:',total_price)

