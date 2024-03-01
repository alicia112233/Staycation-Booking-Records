import functionfile as ff
print("Select from following choices to continue:")
print("1. Display all records")
print("2. Sort record by Customer Name using Bubble sort")
print("3. Sort record by Package Name using Selection sort")
print("4. Sort record by Package Cost using Insertion sort")
print("5. Search record by Customer Name using Linear Search and update record")
print("6. Search record by Package Name using Binary Search and update record")
print("7. List records range from $X to $Y. e.g $100-200")
print("8. Sort the number of pax using Merge sort (BF)")
print("0. Exit Application")
while True:
    try:
        choice = int(input("Enter choice:"))
        if choice == 1:
            for i in ff.list:
                cust = i['Customer Name']
                packname = i['Package Name']
                cost = i['Cost']
                pax = i['NoOfPax']
                print('Customer:', cust, ', Package Name:', packname, ', Cost per pax:', cost, ', No. Of Pax:', pax)

        elif choice == 2:
            ff.bubbleSort(ff.list)
            for i in ff.list:
                cust = i['Customer Name']
                packname = i['Package Name']
                cost = i['Cost']
                pax = i['NoOfPax']
                print('Customer:', cust, ', Package Name:', packname, ', Cost per pax:', cost, ', No. Of Pax:', pax)

        elif choice == 3:
            ff.Selection(ff.list)
            for i in ff.list:
                cust = i['Customer Name']
                packname = i['Package Name']
                cost = i['Cost']
                pax = i['NoOfPax']
                print('Customer:', cust, ', Package Name:', packname, ', Cost per pax:', cost, ', No. Of Pax:', pax)

        elif choice == 4:
            ff.insertionSort(ff.list)
            for i in ff.list:
                cust = i['Customer Name']
                packname = i['Package Name']
                cost = i['Cost']
                pax = i['NoOfPax']
                print('Customer:', cust, ', Package Name:', packname, ', Cost per pax:', cost, ', No. Of Pax:', pax)

        elif choice == 5:
            # Driver Code
            while True:
                who = input('Who do you want to search? ')
                ff.linsearch(ff.list, who.upper())
                break

        elif choice == 6:
            ff.Selection(ff.list)
            while True:
                x = input('What Package do you want to find: ')
                ff.binarySearch(ff.list, x.upper())
                break

        elif choice == 7:
            # min-max range
            def rangelist(list):
                records = []
                count = 0
                for x in list:
                    if x['Cost'] >= min and x['Cost'] <= max:
                        records.append(x)
                        count += 1

                print('The record/s is/are:')
                for record in records:
                    print('Customer Name:', record['Customer Name'], ', Package Name:', record['Package Name'], ', Cost:', record['Cost'], ', No Of Pax:', record['NoOfPax'])

                print('No. of record/s:', count)

            min = int(input('Enter minimum cost:'))
            max = int(input('Enter maximum cost:'))
            rangelist(ff.list)

        elif choice == 8:
            ff.mergeSort(ff.list)
            print("After sort: ")
            ff.printList(ff.list)

        elif choice == 0:
            break

        else:
            print('Enter 1, 2, 3, 4, 5, 6, 7, 8 or 0!')

    except ValueError:
        print('Enter Numbers Only!')
