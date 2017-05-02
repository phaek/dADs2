# -*- coding: utf-8 -*-

def findSilhuet(A):
    if len(A) == 0: #Hvis A er tom så returnér [], for så har vi ingen bygninger
        return "Listen er tom"
        
    def kombiner(venstreDelproblem, hoejreDelproblem):
        byg1_hoejde = 0
        byg2_hoejde = 0
        delproblemRetVal = []
        i = 0
        j = 0
        while i < len(venstreDelproblem) and j < len(hoejreDelproblem):
            byg1_startX = venstreDelproblem[i][0]
            byg2_startX = hoejreDelproblem[j][0]

            if byg1_startX <= byg2_startX: #Hvis byg1 <= byg2 er bygningernes startX sorteret og alt er godt
                currBygning = venstreDelproblem[i]
                byg1_hoejde = venstreDelproblem[i][1]
                i += 1
            if byg1_startX >= byg2_startX: #Hvis bygning2 starter FØR bygning1, så håndterer vi stadig venstre bygning først
                currBygning = hoejreDelproblem[j]
                byg2_hoejde = hoejreDelproblem[j][1]
                j += 1
                
            currBygning[1] = max(byg1_hoejde, byg2_hoejde) #Nuværende maxhøjde sættes til max(b1.h, b2.h)
            
            if delproblemRetVal and delproblemRetVal[-1][1] == currBygning[1]:
                continue
            delproblemRetVal.append(currBygning)

        #Tid til at samle delproblemernes returværdier
        if i < len(venstreDelproblem):
            delproblemRetVal += venstreDelproblem[i:]
        else:
            delproblemRetVal += hoejreDelproblem[j:]
            
        return delproblemRetVal

        #Forvandler delproblemets liste om til punkter
    A = [[[startX, h], [byg2_startX, 0]] for startX, h, byg2_startX in A]

    while len(A) > 1:
        A = [kombiner(A[2*i], A[2*i+1]) for i in range(len(A)/2)] + ([A[-1]] if len(A) % 2 else []) 
            
    return A[0]
        
