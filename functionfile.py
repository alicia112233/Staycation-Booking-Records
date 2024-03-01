list = [{'Customer Name': 'Angela', 'Package Name': 'Conrad Centennial Singapore', 'Cost': 390, 'NoOfPax': 5},
        {'Customer Name': 'Elizabeth', 'Package Name': 'Hilton Singapore Orchard', 'Cost': 270, 'NoOfPax': 3},
        {'Customer Name': 'Claire', 'Package Name': 'Hotel G Singapore', 'Cost': 280, 'NoOfPax': 7},
        {'Customer Name': 'Gwen', 'Package Name': 'YOTEL Singapore Orchard Road', 'Cost': 250, 'NoOfPax': 4},
        {'Customer Name': 'Benny', 'Package Name': 'The St. Regis Singapore', 'Cost': 150, 'NoOfPax': 6},
        {'Customer Name': 'Faith', 'Package Name': 'Capella Singapore', 'Cost': 450, 'NoOfPax': 12},
        {'Customer Name': 'Danny', 'Package Name': 'Fullerton Bay Hotel Singapore', 'Cost': 320, 'NoOfPax': 15}]


# bubble sort
def bubbleSort(theSeq):
    n = len(theSeq)
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
        # Bubble the largest item to the end
        for j in range(i):
            if theSeq[j]['Customer Name'] > theSeq[j + 1]['Customer Name']:
                # Swap the j and j+1 items
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp


# Sort a sequence in ascending order using the selection sort algorithm
def Selection(theSeq):
    n = len(theSeq)
    for i in range(n - 1):
        # Assume the ith element is the smallest.
        smallNdx = i
        # Determine if any other element contains a smaller value.
        for j in range(i+1, n):
            if theSeq[j]['Package Name'] < theSeq[smallNdx]['Package Name']:
                smallNdx = j
                # Swap the ith value and smallNdx value only if the smallest
                # value is not already in its proper position.
                if smallNdx != i:
                    tmp = theSeq[i]
                    theSeq[i] = theSeq[smallNdx]
                    theSeq[smallNdx] = tmp


# Sorts a sequence in ascending order using the insertion sort algorithm
def insertionSort(theSeq):
    n = len(theSeq)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned
        value = theSeq[i]
        # Find the position where value fits in the
        # ordered part of the list.
        pos = i
        while pos > 0 and value['Cost'] < theSeq[pos - 1]['Cost']:
            # Shift the items to the right during the search
            theSeq[pos] = theSeq[pos-1]
            pos -= 1
            # Put the saved value into the open slot.
            theSeq[pos] = value


# linear search
def linsearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        # If the target is in the theValues element, return True, and proceeds to update option.
        if theValues[i]['Customer Name'].upper() == target:
            while True:
                update = input('Do you want to update this person? (Y/N) ')
                if update.upper() == 'Y':
                    what = input('what do you want to update? (pn: package name, c: cost, pax: no of pax) ')
                    if what.upper() == 'PN':
                        newpackname = input("What other package do you want to change to? ")
                        theValues[i]['Package Name'] = newpackname
                        print("Package Name successfully changed!")
                    elif what.upper() == 'C':
                        try:
                            newcost = int(input("Cost to be changed to: "))
                            theValues[i]['Cost'] = newcost
                            print("Cost per pax successfully changed!")
                        except ValueError:
                            print('Enter numbers only!')
                    elif what.upper() == 'PAX':
                        try:
                            newpax = int(input("Number of pax to be changed to: "))
                            theValues[i]['NoOfPax'] = newpax
                            print("Number of pax successfully changed!")
                        except ValueError:
                            print('Enter numbers only!')
                    else:
                        print('Enter only pn, c or pax!')

                elif update.upper() == 'N':
                    print("Ok bye! If you have updated earlier, it's updated!")
                    return  # Exit the function after printing the message
                else:
                    print('Please choose Y/N !')
    print('Not found, try again!')  # If not found, print this.


# binary search
def binarySearch(theValues, target):
    n = len(theValues)
    # Start with the entire sequence of elements
    low = 0
    high = len(theValues) - 1
    for i in range(n):
        # Repeatedly subdivide the sequence in half until the target is found
        if low <= high:
            # Find the midpoint of the sequence
            mid = (high + low) // 2
            # Does the midpoint contain the target?
            # If yes, return midpoint (i.e. index of the list)
            if theValues[mid]['Package Name'].upper() == target:
                update = input('Do you want to update this Package Name? (Y/N) ')
                if update.upper() == 'Y':
                    what = input('what do you want to update? (cn: customer name, c: cost, pax: no of pax) ')
                    if what.upper() == 'CN':
                        newcustname = input("Customer name to be changed to: ")
                        theValues[i]['Customer Name'] = newcustname
                        print("Customer Name successfully changed!")
                    elif what.upper() == 'C':
                        try:
                            newcost = int(input("Cost to be changed to: "))
                            theValues[i]['Cost'] = newcost
                            print("Cost per pax successfully changed!")
                        except ValueError:
                            print('Enter numbers only!')
                    elif what.upper() == 'PAX':
                        try:
                            newpax = int(input("Number of pax to be changed to: "))
                            theValues[i]['NoOfPax'] = newpax
                            print("Number of pax successfully changed!")
                        except ValueError:
                            print('Enter numbers only!')
                    else:
                        print('Enter only cn, c or pax!')

                elif update.upper() == 'N':
                    print("Ok bye! If you have updated earlier, it's updated!")
                    return  # Exit the function after printing the message
                else:
                    print('Please choose Y/N !')

            # Or is the target before the midpoint?
            elif target < theValues[mid]['Package Name']:
                high = mid - 1
            # Or is the target after the midpoint?
            else:
                low = mid + 1
    # If the sequence cannot be subdivided further, target is not in the list of values
    print("Not found, try again!")


# MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2
        # Dividing the array elements
        left = arr[:mid]
        # into 2 halves
        right = arr[mid:]
        # Sorting the first half
        mergeSort(left)
        # Sorting the second half
        mergeSort(right)

        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i]['NoOfPax'] < right[j]['NoOfPax']:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k]['NoOfPax'] = left[i]['NoOfPax']
            i += 1
            k += 1

        while j < len(right):
            arr[k]['NoOfPax'] = right[j]['NoOfPax']
            j += 1
            k += 1


# Code to print the list
def printList(list):
    for i in list:
        cust = i['Customer Name']
        packname = i['Package Name']
        cost = i['Cost']
        pax = i['NoOfPax']
        print('Customer:', cust, ', Package Name:', packname, ', Cost per pax:', cost, ', No. Of Pax:', pax)
