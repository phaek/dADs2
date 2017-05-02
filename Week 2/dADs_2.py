def partyList(T):
    n = len(T)-1
    guestList = []

    for i in range(0, n+1):
        #print "[ ] Current node: " + str(n-i+1) + " and its parent's value:", T[T[n-i][2]-1][0]
        if T[n-i][0] < 1:
            #print "[!] Skipping node " + str(n-i+1) + " (Reason: < 1)"
            continue 
        if T[n-i][0] > 0 and not any(j in T[n-i][1] for j in guestList):
            #print "[+] Adding " + str(n-i+1) + " to the guest list (Reason: > 0 && has no children in guestList)"
            guestList += [n-i+1]
        
        cSum = 0
        for l in range(0, len(T[n-i][1])):
            if T[T[n-i][1][l]-1][0] > 0:
                cSum += T[T[n-i][1][l]-1][0]
        #print "[ ] Calculated sum(children) of node " + str(n-i+1) + ": " + str(cSum)
        if T[n-i][0] > cSum and n-i+1 not in guestList and T[n-i][0] > T[T[n-i][2]-1][0]:
            #print "[+] Adding " + str(n-i+1) + " to the guest list (Reason: Node's value > sum(children)"
            guestList += [n-i+1]
            #print "[-] Removing children of previous node from guest list (Reason: parent+children not allowed)"
            guestList = [j for j in guestList if j not in [T[n-i][1]]]
            for l in range(0, len(T[n-i][1])):
                if T[n-i][1][l] in guestList:
                    guestList.remove(T[n-i][1][l])


        
    print "Guest list:", guestList
    print "Conviviality:", convivialitySum(guestList, T),"\n"
