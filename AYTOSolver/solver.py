
#solve MTV's Are You The One based on previous responses

#setup

lexn = list(["Melanie","Britni","Kiki","Kiki","Kiki","Kiki"])
lexp = list([0,2,2,4,5,9])

lr1 = list(["Stacey","Kiki","Hannah","Chelsey","Melanie","Britni","Amanda","Cheyenne","Rashida","Kayla"]) # guess order, round 1
ir1 = 2 #how many were correct?
lr2 = list(["Chelsey","Kiki","Hannah","Kayla","Melanie","Stacey","Amanda","Cheyenne","Rashida","Britni"])  # guess order, round 2
ir2 = 0 #how many were correct?
lr3 = list(["Stacey","Amanda","Kiki","Chelsey","Rashida","Britni","Kayla","Melanie","Cheyenne","Hannah"])
ir3 = 3 
lr4 = list(["Amanda","Stacey","Kiki","Chelsey","Hannah","Rashida","Kayla","Britni","Melanie","Cheyenne"])
ir4 = 2
lr5 = list(["Stacey","Hannah","Kiki","Chelsey","Cheyenne","Melanie","Britni","Rashida","Amanda","Kayla"])
ir5 = 2
lr6 = list(["Stacey","Cheyenne","Amanda","Chelsey","Rashida","Britni","Melanie","Kiki","Hannah","Kayla"])
ir6 = 3
lr7 = list(["Rashida","Kayla","Melanie","Chelsey","Britni","Amanda","Stacey","Kiki","Cheyenne","Hannah"])
ir7 = 3
lr8 = list(["Stacey","Kiki","Amanda","Chelsey","Rashida","Britni","Melanie","Kayla","Cheyenne","Hannah"])
ir8 = 3
lr9 = list(["Stacey","Cheyenne","Rashida","Chelsey","Britni","Kayla","Kiki","Amanda","Melanie","Hannah"])
ir9 = 2

loL = list([lr1, lr2, lr3, lr4, lr5, lr6, lr7, lr8, lr9]) #add all the rounds together in a list (of lists)
loIR = list([ir1, ir2, ir3, ir4, ir5, ir6, ir7, ir8, ir9]) #and all the correct guesses

n = len(lr1)
a = list(lr1)
ix = 0

#Function

def permute(a, l, r):
    if l == r:
        checker = True
        for x in range(len(lexn)):
            if checker == True:#wrong this bit iis wrong
                if a[lexp[x]] == lexn[x]:
                    checker = False#wrong this bit iis wrong
        for x in range(len(loL)):
            if checker == True:    
                ix = 0
                ir = loIR[x]
                lr = loL[x]
                for i in range(len(a)):
                    if a[i] == lr[i]: ix = ix + 1
                if ix != ir:
                    checker = False
        if checker == True: print(a)
    else: 
        for i in range(l, r + 1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l + 1, r) 
            a[l], a[i] = a[i], a[l] 
permute(a, 0, n-1)
  
#Coded by Joerg Wood
