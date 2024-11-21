import csv

DATE_FORMAT = "%d/%m/%Y"

def appenditems():
    fobj = open('item.csv', 'a', newline='')
    robj = open('item.csv')
    data = csv.writer(fobj)
    recs = csv.reader(robj)
    initial_lines = sum(1 for x in recs)
    robj.close()
    while True:
        n = input('(Type leave to exit)\nNo.of records: ')
        if n.lower() == 'leave':
            return
        if n.isdigit() and int(n) >= 0:
            break
        print('Please enter a valid number ')
        continue
    n = int(n)
    for count in range(1, n + 1):
        icode = 'P00' + str(initial_lines + count)
        particular = input('\nname of item: ').upper()
        while True:
            rate = eval(input('item rate: '))
            if rate > 0.0:
                break
            print('Item rate cannot be negative or zero\nPlease try again')
            continue
        while True:
            quantity = int(input('quantity: '))
            if quantity > 0.0:
                break
            print('Quantity of item cannot be negative or zero\nPlease try again')
            continue
        items = [icode, particular, rate, quantity]
        data.writerow(items)
    fobj.close()
    print('\nitem(s) appended to the file')
    print()
#appenditems()

def print_items():
    fobj = open('item.csv')
    data = csv.reader(fobj)
    c = sum(1 for _ in data)
    fobj.close()
    if c:
        fobj = open('item.csv')
        data = csv.reader(fobj)
        print('ICode ', 'Item Particular ', 'Rate ', 'Quantity ')
        print('---------------------------------------')
        for rec in data:
            print(rec[0], ' ' * (5 - len(rec[0])), rec[1], ' ' * (15 - len(rec[1])), rec[2], ' ' * (5 - len(str(rec[2]))), rec[3], ' ' * (8 - len(str(rec[3]))))

        print('---------------------------------------\n')
    else:
        print('No items available ')
    fobj.close()
# print_items()

def search_item():
    fobj = open('item.csv')
    data = csv.reader(fobj)
    icode = input('Item code to search: ')
    f = 0
    for rec in data:
        if rec[0] == icode.upper():
            n_list = [rec]
            f = 1
    fobj.close()
    if f:
        print('\nICode ', 'Item Particular ', 'Rate ', 'Quantity ')
        for rec in n_list:
            print(rec[0], ' '*(5-len(rec[0])),
                  rec[1], ' '*(15-len(rec[1])),
                  rec[2], ' '*(5-len(str(rec[2]))),
                  rec[3], ' '*(8-len(str(rec[3]))))
            print()
    else:
        print('Item not found\n')
# search_item()

def change_rate():
    print_items()
    fobj=open('item.csv')
    data=csv.reader(fobj)
    icode=input('Item code: ')
    nlist=[]
    f = 0
    for rec in data:
        if rec[0] == icode:
            f = 1
            rate = eval(input('New rate of the item: '))
            rec[2] = rate
        nlist += [rec]
    fobj.close()
    if f:
        fobj=open('item.csv', 'w', newline='')
        data=csv.writer(fobj)
        data.writerows(nlist)
        fobj.close()
        print_items()
    else:
        print('Item code not found ')
# change_rate()           

def show_quantity_items():
    fobj = open('item.csv')
    data = csv.reader(fobj)
    items_list = []
    notavailable = []
    quantity = []
    for rec in data:
        if int(rec[3]) > 0:
            items_list += [rec[1]]
        if int(rec[3]) < 20:
            quantity += [rec[1]]
        if int(rec[3]) == 0:
            notavailable += [rec[1]]
    fobj.close()
    print('\nAvailable items: ')
    if len(items_list) != 0:
        for k in items_list:
            print(k)
    else:
        print('None')
    print('\nItems whose stock is less than 20: ')
    if len(quantity) != 0:
        for k in quantity:
            print(k)
    else:
        print('None')
    print('\nNot available items: ')
    if len(notavailable) != 0:
        for k in notavailable:
            print(k)
    else:
        print('None\n')
# show_quantity_items()

def get_icode_quan():
    fitem = open('item.csv')
    data = csv.reader(fitem)
    quantities = []
    icodes = []
    for i in data:
        quantities += [int(i[3])]
        icodes += [i[0]]
    fitem.close()
    return icodes, quantities
# get_icode_quan()

def delete_item():
    icodes, _ = get_icode_quan()
    print_items()
    while True:
        icode = input('(Type leave to exit this option)\nPlease enter the item code of the product: ')
        if icode.lower() == 'leave':
            print('The function was exited\n')
            return
        if icode.upper() in icodes:
            ans = input('Are you sure u want to delete this item? (Y/N)')
            if ans.upper() == 'Y':
                break
            else:
                continue
        print('please enter a valid icode to delete an item')
        continue
    fobj = open('item.csv')
    data = csv.reader(fobj)
    newlist = [rec for rec in data if rec[0] != icode.upper()]
    fobj.close()
    fitem = open('item.csv', 'w', newline='')
    records = csv.writer(fitem)
    records.writerows(newlist)
    fobj.close()
    print('\nSelected item was deleted\n')
    print_items()
# delete_item()

def date_memo():
    from datetime import date
    fobj = open('sale.csv')
    data = csv.reader(fobj)
    c = sum(rec[0] == 'date' for rec in data)
    fobj.close()
    cashno = 12340 + c + 1
    now = date.today()
    cdate = now.strftime(DATE_FORMAT)
    return cashno, cdate
# print(date_memo())

def append_stock():
    icodes, _ = get_icode_quan()
    print_items()
    while True:
        icode = input('(Type exit to exit this option)\nplease enter the item code of the product: ')
        if icode.lower() == 'exit':
            print('The function was exited\n')
            return
        if icode.upper() in icodes:
            break
        print('Please enter a valid icode')
        continue
    newlist = []
    fobj = open('item.csv')
    data = csv.reader(fobj)
    for rec in data:
        if rec[0] == icode.upper():
            while True:
                quan = input('Please enter the quantity: ')
                if quan.isdigit() and int(quan) > 0:
                    quan = int(quan)
                    break
                print('Please enter a valid amount')
                continue
            rec[3] = int(rec[3])+quan
        newlist += [rec]
    fobj.close()
    fobj = open('item.csv', 'w', newline='')
    recs = csv.writer(fobj)
    recs.writerows(newlist)
    fobj.close()
# append_stock()

def stock_modification():
    icodes, quantities = get_icode_quan()
    print()
    print_items()
    while True:
        icode = input('\nPlease enter the item code of the product: ')
        if icode.upper() in icodes:
            x = icodes.index(icode.upper())
            break
        print('Please enter a valid icode')
        continue
    while True:
        quantity = input('Please enter the quantity of the product: ')
        if quantity.isdigit() and int(quantity) >= 0 and int(quantity) <= quantities[x]:
            break
        print('Please enter a valid quantity ')
        continue
    quantity = int(quantity)
    newlist = []
    fitem = open('item.csv')
    data = csv.reader(fitem)
    for rec in data:
        if rec[0] == icode.upper():
            rec[3] = int(rec[3]) - quantity
            particular = rec[1]
            rate = float(rec[2])
        newlist += [rec]
    fitem.close()
    fobj = open('item.csv', 'w', newline='')
    recs = csv.writer(fobj)
    recs.writerows(newlist)
    fobj.close()
    return icode.upper(), particular, rate, quantity
# stock_modification()

def calc(total):
    discount = 0
    if total >= 3000.0:
        discount = total-(0.3*total)
        print('After discount:', discount)
    elif 1000 <= total < 3000.0:
        discount = total-(0.1*total)
        print('After discount:', discount)
    return discount
#print(calc)

def purchase(n):
    cashno, date = date_memo()
    datenmemo = ['date', date, cashno]
    fsale = open('sale.csv', 'a', newline='')
    purchase = csv.writer(fsale)
    purchase.writerow(datenmemo)
    total = 0
    final_list = []
    for c in range(1, n+1):
        icode, particular, rate, quantity = stock_modification()
        amount = rate*quantity
        total += amount
        print('\n(Total till now:', total, ')')
        final_list += [[c, icode, particular, rate, quantity, amount]]
    discount = calc(total)
    purchase.writerows(final_list)
    purchase.writerow(['Grand Total', total, 'After discount', discount])
    return final_list, date, cashno, total, discount
# purchase(n)

def print_format(final_list):
    print('----------------------------------------------------')
    print('Sno ', 'ICode ', 'Item Particular ',
          'Rate ', 'Quantity ', 'Amount ')
    for rec in final_list:
        print(rec[0], ' '*(4-len(str(rec[0]))),
              rec[1], ' '*(5-len(rec[1])),
              rec[2], ' '*(15-len(rec[2])),
              rec[3], ' '*(5-len(str(rec[3]))),
              rec[4], ' '*(8-len(str(rec[4]))),
              rec[5], ' '*(6-len(str(rec[5]))))
    print('----------------------------------------------------')
# print_format()

def print_bill(n):
    final_list, date, cashno, total, discount = purchase(n)
    print()
    print('Date: ', date, '         ', 'Cash Memo Number: ', cashno)
    print_format(final_list)
    if discount:
        print('Grand Total', total, 'After Discount', discount)
    else:
        print('Grand Total', total, ' (no discount)')
    print('----------------------------------------------------')
# print_bill(n)

def print_reports(rec):
    print(rec[0], ' '*(4-len(str(rec[0]))),
          rec[1], ' '*(5-len(rec[1])),
          rec[2], ' '*(15-len(rec[2])),
          rec[3], ' '*(5-len(str(rec[3]))),
          rec[4], ' '*(8-len(str(rec[4]))),
          rec[5], ' '*(6-len(str(rec[5]))))
# print_reports(rec)

def chk_date():
    while True:
        days = 0
        date = input('Please enter the date in dd/mm/yyyy format: ')
        if '01' <= date[3:5] <= '12':
            if date[3:5] in ['01', '03', '05', '07', '08', '10', '12']:
                days = 31
            elif date[3:5] in ['04', '06', '09', '11']:
                days = 30
            elif int(date[6:]) % 100 and int(date[6:]) % 4 or int(date[6:]) % 400:
                days = 28
            else:
                days = 29
            if '01' <= date[:2] <= str(days):
                break
        print('Please enter a valid date')
        continue
    return date
#print(chk_date)

def daily_reports():
    print('DAILY SALES REPORT\n')
    fobj = open('sale.csv')
    data = csv.reader(fobj)
    c_date = chk_date()
    f = 0
    total = 0
    qtotal = 0
    for rec in data:
        if rec[1] == c_date:
            f += 1
            print('\nDate', rec[1], '          ', 'Cash Memo Number', rec[2])
            print('----------------------------------------------------')
            print('Sno ', 'ICode ', 'Item Particular ', 'Rate ', 'Quantity ', 'Amount ')
            for rec in data:
                if rec[0] == 'date':
                    break
                if rec[0] == 'Grand Total':
                    print('----------------------------------------------------')
                    if float(rec[3]):
                        print('Grand Total ', rec[1], 'After Discount', rec[3])
                        total += float(rec[3])
                    else:
                        print('Grand Total ', rec[1], '(no discount)')
                        total += float(rec[1])
                    break
                qtotal += int(rec[4])
                print_reports(rec)
    print('\nConclusion for date', c_date)
    print('Total qauntity sold: ', qtotal)
    print('Total sales: ', total)
    if not f:
        print('No records found ')
# daily_reports()

def monthly_reports():
    while True:
        c_month = input('Month (mm): ')
        if 0 < int(c_month) < 13:
            break
        print('Please enter a valid month number')
        continue
    print('MONTHLY SALES \n')
    fobj = open('sale.csv')
    data = csv.reader(fobj)
    c = 0
    total = 0
    qtotal = 0
    for rec in data:
        if rec[1][3:5] == c_month:
            c += 1
            print('\nDate', rec[1], '          ', 'Cash Memo Number', rec[2])
            print('----------------------------------------------------')
            print('Sno ', 'ICode ', 'Item Particular ', 'Rate ', 'Quantity ', 'Amount ')
            for rec in data:
                if rec[0] == 'date':
                    break
                if rec[0] == 'Grand Total':
                    print('----------------------------------------------------')
                    if float(rec[3]):
                        print('Grand Total ', rec[1], 'After Discount', rec[3])
                        total += float(rec[3])
                    else:
                        print('Grand Total ', rec[1], '(no discount)')
                        total += float(rec[1])
                    break
                qtotal += int(rec[4])
                print_reports(rec)
    print('\nConclusion for month', c_month)
    print('Total quantity sold: ', qtotal)
    print('Total sales: ', total)
    if not c:
        print('No records found ')
# monthly_reports()

def yearly_reports():
    print('YEARLY SALES REPORT\n')
    fobj = open('sale.csv')
    data = csv.reader(fobj)
    while True:
        c_year = input('Year (yyyy): ')
        if int(c_year)>=2022:
            break
        print('Please enter the correct year ')
    c = 0
    total = 0
    qtotal = 0
    for rec in data:
        if rec[1][6::] == c_year:
            c += 1
            print('\nDate', rec[1], '          ', 'Cash Memo Number', rec[2])
            print('----------------------------------------------------')
            print('Sno ', 'ICode ', 'Item Particular ',
                  'Rate ', 'Quantity ', 'Amount ')
            for rec in data:
                if rec[0] == 'date':
                    break
                if rec[0] == 'Grand Total':
                    print('----------------------------------------------------')
                    if float(rec[3]):
                        print('Grand Total ', rec[1], 'After Discount', rec[3])
                        total += float(rec[3])
                    else:
                        print('Grand Total ', rec[1], '(no discount)')
                        total += float(rec[1])
                    break
                qtotal += int(rec[4])
                print(rec[0], ' '*(4-len(str(rec[0]))),
                      rec[1], ' '*(5-len(rec[1])),
                      rec[2], ' '*(15-len(rec[2])),
                      rec[3], ' '*(5-len(str(rec[3]))),
                      rec[4], ' '*(8-len(str(rec[4]))),
                      rec[5], ' '*(6-len(str(rec[5]))))
    print('\nConclusion for year', c_year)
    print('Total quantity sold:', qtotal)
    print('Total sales:', total)
    if not c:
        print('No records found ')
# yearly_reports()

def itemwise_reports():
    fobj = open('sale.csv')
    data = csv.reader(fobj)
    items = []
    for rec in data:
        if rec[0] not in ['date', 'Grand Total']:
            items += [{'Code': rec[1], 'Particular':rec[2], 'Rate':rec[3], 'Quantity':rec[4], 'Amount':rec[5]}]
            break
    for i in data:
        if i[0] not in ['date', 'Grand Total']:
            for x in items:
                if x['Code'] == i[1]:
                    x['Quantity'] = int(x['Quantity'])+int(i[4])
                    x['Amount'] = float(x['Amount'])+float(i[5])
                    break
            else:
                items += [{'Code': i[1], 'Particular':i[2], 'Rate':i[3], 'Quantity':i[4], 'Amount':i[5]}]
    fobj.close()
    return items
# itemwise_reports()

def count_itemwise():
    items = itemwise_reports()
    qtotal = 0
    total = 0
    for rec in items:
        qtotal += int(rec['Quantity'])
        total += float(rec['Amount'])
    return qtotal, total
# print(count_itemwise())

def insertion_sort():
    items = itemwise_reports()
    n = len(items)
    for x in range(1, n):
        k = x-1
        t = items[x]
        while k >= 0 and items[k]['Code'][1::] > t['Code'][1::]:
            items[k+1] = items[k]
            k -= 1
        items[k+1] = t
    return items
# insertion_sort()

def print_report():
    items = insertion_sort()
    qtotal, total = count_itemwise()
    print('ITEM=WISE SALES REPORT\n')
    print('ICode ', 'Item Particular ', 'Rate ',
          'Total Quantity ', ' Total Amount ')
    print('----------------------------------------------------------')
    for record in items:
        print(record['Code'], ' '*(5-len(record['Code'])),
              record['Particular'], ' '*(15-len(record['Particular'])),
              record['Rate'], ' '*(5-len(str(record['Rate']))),
              record['Quantity'], ' '*(13-len(str(record['Quantity']))),
              record['Amount'], ' '*(11-len(str(record['Amount']))))
    print('----------------------------------------------------------\n')
    print('Conclusion')
    print('Total quantity: ', qtotal)
    print('Total amount: ', total)
# print_report()

while True:
    a=input('(press space and enter to exit) \nAre you a supplier(s) or buyer(b)? ')
    if a.lower()=='s':
        print_items()
        while True:
            print('\n1.Append new item ')
            print('2.search for an item')
            print('3.Add quantity ')
            print('4.Change rate of an item ')
            print('5.Delete an item ')
            print('6.Daily sales report')
            print('7.Monthly sales report')
            print('8.Yearly sales report')
            print('9.Item-wise sales report')
            print('10.Items available,items whose quantity is less than 20 and items whose stock is over')
            print('0.Exit')
            ch=input('Input choice-[0-10]:')
            if ch=='1':
                appenditems()
                print_items()
            if ch=='2':
                search_item()
            if ch=='3':
                append_stock()
                print_items()
            if ch=='4':
                change_rate()
            if ch=='5':
                delete_item()
                print_items()
            if ch=='6':
                daily_reports()
            if ch=='7':
                monthly_reports()
            if ch=='8':
                yearly_reports()
            if ch=='9':
                print_report()
            if ch=='10':
                show_quantity_items()
            if ch=='0':
                print('Thank you\n')
                break
    if a.lower()=='b':
        ans=input('Do you want to continue purchasing(y/n)? ')
        if ans.lower()=='n':
            break
        if ans.lower() not in ['y','n']:
            continue
        while True:
            n=input('\nHow many items do you want to purchase? ')
            if not n.isdigit() or int(n)<0:
                print('Please enter a valid number')
                continue
            n=int(n)
            break
        print()
        print('SPECIAL DISCOUNT')
        print('10% off on shopping over 1000 ')
        print('20% off on shooping over 3000')
        print_bill(n)
        print('Thank you shopping\n')
    if a==' ':
        break
    else:
        continue

'''
Sample Input/Output

(press space and enter to exit) 
Are you a supplier(s) or buyer(b)? S
ICode  Item Particular  Rate  Quantity 
---------------------------------------
P001   PEN              40.0   400      
P002   PENCIL           10.0   400      
P003   CARBON PAPER     20.0   400      
P004   ERASER           5.0    400      
P005   RULER            15.0   400      
P006   NOTEBOOK         75.0   400      
---------------------------------------


1.Append new item 
2.search for an item
3.Add quantity 
4.Change rate of an item 
5.Delete an item 
6.Daily sales report
7.Monthly sales report
8.Yearly sales report
9.Item-wise sales report
10.Items available,items whose quantity is less than 20 and items whose stock is over
0.Exit
Input choice-[0-10]:1
(Type leave to exit)
No.of records: 1

name of item: HIGHLIGHTER PEN
item rate: 30.0
quantity: 390

item(s) appended to the file

ICode  Item Particular  Rate  Quantity 
---------------------------------------
P001   PEN              40.0   400      
P002   PENCIL           10.0   400      
P003   CARBON PAPER     20.0   400      
P004   ERASER           5.0    400      
P005   RULER            15.0   400      
P006   NOTEBOOK         75.0   400      
P007   HIGHLIGHTER PEN  30.0   390      
---------------------------------------


1.Append new item 
2.search for an item
3.Add quantity 
4.Change rate of an item 
5.Delete an item 
6.Daily sales report
7.Monthly sales report
8.Yearly sales report
9.Item-wise sales report
10.Items available,items whose quantity is less than 20 and items whose stock is over
0.Exit
Input choice-[0-10]:2
Item code to search: P003

ICode  Item Particular  Rate  Quantity 
P003   CARBON PAPER     20.0   400      


1.Append new item 
2.search for an item
3.Add quantity 
4.Change rate of an item 
5.Delete an item 
6.Daily sales report
7.Monthly sales report
8.Yearly sales report
9.Item-wise sales report
10.Items available,items whose quantity is less than 20 and items whose stock is over
0.Exit
Input choice-[0-10]:3
ICode  Item Particular  Rate  Quantity 
---------------------------------------
P001   PEN              40.0   400      
P002   PENCIL           10.0   400      
P003   CARBON PAPER     20.0   400      
P004   ERASER           5.0    400      
P005   RULER            15.0   400      
P006   NOTEBOOK         75.0   400      
P007   HIGHLIGHTER PEN  30.0   390      
---------------------------------------

(Type exit to exit this option)
please enter the item code of the product: P007
Please enter the quantity: 10
ICode  Item Particular  Rate  Quantity 
---------------------------------------
P001   PEN              40.0   400      
P002   PENCIL           10.0   400      
P003   CARBON PAPER     20.0   400      
P004   ERASER           5.0    400      
P005   RULER            15.0   400      
P006   NOTEBOOK         75.0   400      
P007   HIGHLIGHTER PEN  30.0   400      
---------------------------------------


1.Append new item 
2.search for an item
3.Add quantity 
4.Change rate of an item 
5.Delete an item 
6.Daily sales report
7.Monthly sales report
8.Yearly sales report
9.Item-wise sales report
10.Items available,items whose quantity is less than 20 and items whose stock is over
0.Exit
Input choice-[0-10]:4
ICode  Item Particular  Rate  Quantity 
---------------------------------------
P001   PEN              40.0   400      
P002   PENCIL           10.0   400      
P003   CARBON PAPER     20.0   400      
P004   ERASER           5.0    400      
P005   RULER            15.0   400      
P006   NOTEBOOK         75.0   400      
P007   HIGHLIGHTER PEN  30.0   400      
---------------------------------------

Item code: P007
New rate of the item: 25.0
ICode  Item Particular  Rate  Quantity 
---------------------------------------
P001   PEN              40.0   400      
P002   PENCIL           10.0   400      
P003   CARBON PAPER     20.0   400      
P004   ERASER           5.0    400      
P005   RULER            15.0   400      
P006   NOTEBOOK         75.0   400      
P007   HIGHLIGHTER PEN  25.0   400      
---------------------------------------


1.Append new item 
2.search for an item
3.Add quantity 
4.Change rate of an item 
5.Delete an item 
6.Daily sales report
7.Monthly sales report
8.Yearly sales report
9.Item-wise sales report
10.Items available,items whose quantity is less than 20 and items whose stock is over
0.Exit
Input choice-[0-10]:5
ICode  Item Particular  Rate  Quantity 
---------------------------------------
P001   PEN              40.0   400      
P002   PENCIL           10.0   400      
P003   CARBON PAPER     20.0   400      
P004   ERASER           5.0    400      
P005   RULER            15.0   400      
P006   NOTEBOOK         75.0   400      
P007   HIGHLIGHTER PEN  25.0   400      
---------------------------------------

(Type leave to exit this option)
Please enter the item code of the product: P007
Are you sure u want to delete this item? (Y/N)Y

Selected item was deleted

No items available 
ICode  Item Particular  Rate  Quantity 
---------------------------------------
P001   PEN              40.0   400      
P002   PENCIL           10.0   400      
P003   CARBON PAPER     20.0   400      
P004   ERASER           5.0    400      
P005   RULER            15.0   400      
P006   NOTEBOOK         75.0   400      
---------------------------------------


1.Append new item 
2.search for an item
3.Add quantity 
4.Change rate of an item 
5.Delete an item 
6.Daily sales report
7.Monthly sales report
8.Yearly sales report
9.Item-wise sales report
10.Items available,items whose quantity is less than 20 and items whose stock is over
0.Exit
Input choice-[0-10]:6
DAILY SALES REPORT

Please enter the date in dd/mm/yyyy format: 10/12/2022

Date 10/12/2022            Cash Memo Number 12371
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P003   CARBON PAPER     20.0   5         100.0  
2     P002   PENCIL           10.0   10        100.0  
3     P005   RULER            15.0   2         30.0   
----------------------------------------------------
Grand Total  230.0 (no discount)

Date 10/12/2022            Cash Memo Number 12372
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P001   PEN              40.0   10        400.0  
----------------------------------------------------
Grand Total  400.0 (no discount)

Conclusion for date 10/12/2022
Total qauntity sold:  27
Total sales:  630.0

1.Append new item 
2.search for an item
3.Add quantity 
4.Change rate of an item 
5.Delete an item 
6.Daily sales report
7.Monthly sales report
8.Yearly sales report
9.Item-wise sales report
10.Items available,items whose quantity is less than 20 and items whose stock is over
0.Exit
Input choice-[0-10]:7
Month (mm): 12
MONTHLY SALES 


Date 10/12/2022            Cash Memo Number 12371
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P003   CARBON PAPER     20.0   5         100.0  
2     P002   PENCIL           10.0   10        100.0  
3     P005   RULER            15.0   2         30.0   
----------------------------------------------------
Grand Total  230.0 (no discount)

Date 10/12/2022            Cash Memo Number 12372
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P001   PEN              40.0   10        400.0  
----------------------------------------------------
Grand Total  400.0 (no discount)

Conclusion for month 12
Total quantity sold:  27
Total sales:  630.0

1.Append new item 
2.search for an item
3.Add quantity 
4.Change rate of an item 
5.Delete an item 
6.Daily sales report
7.Monthly sales report
8.Yearly sales report
9.Item-wise sales report
10.Items available,items whose quantity is less than 20 and items whose stock is over
0.Exit
Input choice-[0-10]:8
YEARLY SALES REPORT

Year (yyyy): 2022

Date 23/08/2022            Cash Memo Number 12341
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P005   RULER            10     5         50     
2     P003   CARBON PAPER     50     10        500    
3     P001   PEN              40     3         120    
----------------------------------------------------
Grand Total  670 (no discount)

Date 23/08/2022            Cash Memo Number 12342
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P002   PENCIL           5      5         25     
2     P004   ERASER           2      10        20     
----------------------------------------------------
Grand Total  45 (no discount)

Date 23/08/2022            Cash Memo Number 12343
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P002   PENCIL           5      10        50     
2     P001   PEN              40     5         200    
3     P003   CARBON PAPER     50     12        600    
4     P005   RULER            10     16        160    
----------------------------------------------------
Grand Total  1010 After Discount 909

Date 23/08/2022            Cash Memo Number 12344
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P002   PENCIL           5      4         20     
2     P003   CARBON PAPER     50     23        1150   
----------------------------------------------------
Grand Total  1170 After Discount 1053

Date 23/08/2022            Cash Memo Number 12345
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P001   PEN              40     8         320    
2     P004   ERASER           2      10        20     
3     P002   PENCIL           5      4         20     
----------------------------------------------------
Grand Total  360 (no discount)

Date 28/08/2022            Cash Memo Number 12346
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P001   PEN              40     12        480    
2     P005   RULER            10     5         50     
3     P003   CARBON PAPER     50     29        1450   
----------------------------------------------------
Grand Total  1980 After Discount 1782

Date 28/08/2022            Cash Memo Number 12347
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P002   PENCIL           10     30        300    
2     P005   RULER            15     13        195    
3     P003   CARBON PAPER     20     27        540    
4     P001   PEN              40     16        640    
----------------------------------------------------
Grand Total  1675 After Discount 1507.5

Date 28/08/2022            Cash Memo Number 12348
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P001   PEN              40.0   4         160.0  
2     P001   PEN              40.0   6         240.0  
3     P003   CARBON PAPER     20.0   10        200.0  
4     P005   RULER            15.0   20        300.0  
----------------------------------------------------
Grand Total  900.0 (no discount)

Date 28/08/2022            Cash Memo Number 12349
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P006   NOTEBOOK         75.0   14        1050.0 
2     P004   ERASER           5.0    3         15.0   
----------------------------------------------------
Grand Total  1065.0 After Discount 958.5

Date 28/08/2022            Cash Memo Number 12350
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P006   NOTEBOOK         75.0   18        1350.0 
2     P002   PENCIL           10.0   10        100.0  
3     P004   ERASER           5.0    7         35.0   
----------------------------------------------------
Grand Total  1485.0 After Discount 1336.5

Date 28/08/2022            Cash Memo Number 12351
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P003   CARBON PAPER     20.0   249       4980.0 
2     P001   PEN              40.0   31        1240.0 
3     P002   PENCIL           10.0   12        120.0  
4     P004   ERASER           5.0    5         25.0   
5     P005   RULER            15.0   9         135.0  
6     P006   NOTEBOOK         75.0   14        1050.0 
----------------------------------------------------
Grand Total  7550.0 After Discount 5285.0

Date 29/08/2022            Cash Memo Number 12352
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P006   NOTEBOOK         75.0   12        900.0  
2     P003   CARBON PAPER     20.0   6         120.0  
3     P002   PENCIL           10.0   16        160.0  
4     P001   PEN              40.0   8         320.0  
----------------------------------------------------
Grand Total  1500.0 After Discount 1350.0

Date 29/08/2022            Cash Memo Number 12353
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P006   NOTEBOOK         75.0   5         375.0  
----------------------------------------------------
Grand Total  375.0 (no discount)

Date 29/08/2022            Cash Memo Number 12354
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P002   PENCIL           10.0   4         40.0   
2     P005   RULER            15.0   3         45.0   
----------------------------------------------------
Grand Total  85.0 (no discount)

Date 29/08/2022            Cash Memo Number 12355
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P001   PEN              40.0   2         80.0   
2     P002   PENCIL           10.0   4         40.0   
3     P003   CARBON PAPER     20.0   6         120.0  
4     P004   ERASER           5.0    8         40.0   
5     P005   RULER            15.0   10        150.0  
6     P006   NOTEBOOK         75.0   12        900.0  
----------------------------------------------------
Grand Total  1330.0 After Discount 1197.0

Date 29/08/2022            Cash Memo Number 12356
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P002   PENCIL           10.0   6         60.0   
2     P004   ERASER           5.0    2         10.0   
----------------------------------------------------
Grand Total  70.0 (no discount)

Date 31/08/2022            Cash Memo Number 12357
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P003   CARBON PAPER     20.0   10        200.0  
2     P001   PEN              40.0   12        480.0  
3     P004   ERASER           5.0    7         35.0   
4     P006   NOTEBOOK         75.0   2         150.0  
----------------------------------------------------
Grand Total  865.0 (no discount)

Date 31/08/2022            Cash Memo Number 12358
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P002   PENCIL           10.0   4         40.0   
2     P005   RULER            15.0   5         75.0   
----------------------------------------------------
Grand Total  115.0 (no discount)

Date 31/08/2022            Cash Memo Number 12359
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P001   PEN              40.0   2         80.0   
2     P002   PENCIL           10.0   2         20.0   
3     P003   CARBON PAPER     20.0   1         20.0   
4     P004   ERASER           5.0    2         10.0   
5     P005   RULER            15.0   1         15.0   
----------------------------------------------------
Grand Total  145.0 (no discount)

Date 31/08/2022            Cash Memo Number 12360
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P006   NOTEBOOK         75.0   2         150.0  
----------------------------------------------------
Grand Total  150.0 (no discount)

Date 02/09/2022            Cash Memo Number 12361
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P002   PENCIL           10.0   4         40.0   
2     P006   NOTEBOOK         75.0   5         375.0  
3     P001   PEN              40.0   2         80.0   
----------------------------------------------------
Grand Total  495.0 (no discount)

Date 02/09/2022            Cash Memo Number 12362
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P003   CARBON PAPER     20.0   5         100.0  
2     P005   RULER            15.0   1         15.0   
----------------------------------------------------
Grand Total  115.0 (no discount)

Date 02/09/2022            Cash Memo Number 12363
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P001   PEN              40.0   2         80.0   
2     P004   ERASER           5.0    3         15.0   
3     P003   CARBON PAPER     20.0   6         120.0  
4     P005   RULER            15.0   3         45.0   
----------------------------------------------------
Grand Total  260.0 (no discount)

Date 02/09/2022            Cash Memo Number 12364
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P005   RULER            15.0   5         75.0   
2     P004   ERASER           5.0    4         20.0   
3     P003   CARBON PAPER     20.0   3         60.0   
4     P002   PENCIL           10.0   2         20.0   
----------------------------------------------------
Grand Total  175.0 (no discount)

Date 02/09/2022            Cash Memo Number 12365
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P001   PEN              40.0   5         200.0  
2     P006   NOTEBOOK         75.0   4         300.0  
----------------------------------------------------
Grand Total  500.0 (no discount)

Date 03/09/2022            Cash Memo Number 12366
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P001   PEN              40.0   6         240.0  
2     P002   PENCIL           10.0   5         50.0   
3     P003   CARBON PAPER     20.0   4         80.0   
4     P004   ERASER           5.0    3         15.0   
5     P005   RULER            15.0   2         30.0   
6     P006   NOTEBOOK         75.0   1         75.0   
----------------------------------------------------
Grand Total  490.0 (no discount)

Date 03/09/2022            Cash Memo Number 12367
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P006   NOTEBOOK         75.0   10        750.0  
2     P002   PENCIL           10.0   10        100.0  
3     P005   RULER            15.0   10        150.0  
4     P001   PEN              40.0   10        400.0  
----------------------------------------------------
Grand Total  1400.0 After Discount 1260.0

Date 03/09/2022            Cash Memo Number 12368
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P002   PENCIL           10.0   5         50.0   
2     P003   CARBON PAPER     20.0   5         100.0  
----------------------------------------------------
Grand Total  150.0 (no discount)

Date 03/09/2022            Cash Memo Number 12369
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P006   NOTEBOOK         75.0   4         300.0  
----------------------------------------------------
Grand Total  300.0 (no discount)

Date 03/09/2022            Cash Memo Number 12370
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P001   PEN              40.0   5         200.0  
2     P002   PENCIL           10.0   4         40.0   
3     P003   CARBON PAPER     20.0   3         60.0   
4     P004   ERASER           5.0    2         10.0   
5     P005   RULER            15.0   6         90.0   
----------------------------------------------------
Grand Total  400.0 (no discount)

Date 10/12/2022            Cash Memo Number 12371
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P003   CARBON PAPER     20.0   5         100.0  
2     P002   PENCIL           10.0   10        100.0  
3     P005   RULER            15.0   2         30.0   
----------------------------------------------------
Grand Total  230.0 (no discount)

Date 10/12/2022            Cash Memo Number 12372
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P001   PEN              40.0   10        400.0  
----------------------------------------------------
Grand Total  400.0 (no discount)

Conclusion for year 2022
Total quantity sold: 999
Total sales: 23933.5

1.Append new item 
2.search for an item
3.Add quantity 
4.Change rate of an item 
5.Delete an item 
6.Daily sales report
7.Monthly sales report
8.Yearly sales report
9.Item-wise sales report
10.Items available,items whose quantity is less than 20 and items whose stock is over
0.Exit
Input choice-[0-10]:9
ITEM=WISE SALES REPORT

ICode  Item Particular  Rate  Total Quantity   Total Amount 
----------------------------------------------------------
P001   PEN              40     149            5960.0      
P002   PENCIL           5      151            1395.0      
P003   CARBON PAPER     50     414            10500.0     
P004   ERASER           2      66             270.0       
P005   RULER            10     116            1610.0      
P006   NOTEBOOK         75.0   103            7725.0      
----------------------------------------------------------

Conclusion
Total quantity:  999
Total amount:  27460.0

1.Append new item 
2.search for an item
3.Add quantity 
4.Change rate of an item 
5.Delete an item 
6.Daily sales report
7.Monthly sales report
8.Yearly sales report
9.Item-wise sales report
10.Items available,items whose quantity is less than 20 and items whose stock is over
0.Exit
Input choice-[0-10]:10

Available items: 
PEN
PENCIL
CARBON PAPER
ERASER
RULER
NOTEBOOK

Items whose stock is less than 20: 
None

Not available items: 
None


1.Append new item 
2.search for an item
3.Add quantity 
4.Change rate of an item 
5.Delete an item 
6.Daily sales report
7.Monthly sales report
8.Yearly sales report
9.Item-wise sales report
10.Items available,items whose quantity is less than 20 and items whose stock is over
0.Exit
Input choice-[0-10]:0
Thank you

(press space and enter to exit) 
Are you a supplier(s) or buyer(b)? B
Do you want to continue purchasing(y/n)? Y

How many items do you want to purchase? 2

SPECIAL DISCOUNT
10% off on shopping over 1000 
20% off on shooping over 3000

ICode  Item Particular  Rate  Quantity 
---------------------------------------
P001   PEN              40.0   400      
P002   PENCIL           10.0   400      
P003   CARBON PAPER     20.0   400      
P004   ERASER           5.0    400      
P005   RULER            15.0   400      
P006   NOTEBOOK         75.0   400      
---------------------------------------


Please enter the item code of the product: P006
Please enter the quantity of the product: 20

(Total till now: 1500.0 )

ICode  Item Particular  Rate  Quantity 
---------------------------------------
P001   PEN              40.0   400      
P002   PENCIL           10.0   400      
P003   CARBON PAPER     20.0   400      
P004   ERASER           5.0    400      
P005   RULER            15.0   400      
P006   NOTEBOOK         75.0   380      
---------------------------------------


Please enter the item code of the product: P001
Please enter the quantity of the product: 5

(Total till now: 1700.0 )
After discount: 1530.0

Date:  10/12/2022           Cash Memo Number:  12373
----------------------------------------------------
Sno  ICode  Item Particular  Rate  Quantity  Amount 
1     P006   NOTEBOOK         75.0   20        1500.0 
2     P001   PEN              40.0   5         200.0  
----------------------------------------------------
Grand Total 1700.0 After Discount 1530.0
----------------------------------------------------
Thank you shopping

(press space and enter to exit) 
Are you a supplier(s) or buyer(b)?  

'''
