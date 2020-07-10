
#solve MTV's Are You The One based on previous responses

#setup

lr1 = list(["Francesca","Victoria","Mikala","Kaylen","Emma","Julia","Camille","Alyssa","Nicole","Tori"]) # guess order, round 1
ir1 = 3 #how many were correct?
lr2 = list(["Camille","Julia","Mikala","Kaylen","Nicole","Alyssa","Emma","Francesca","Tori","Victoria"])  # guess order, round 2
ir2 = 3 #how many were correct?
lr3 = list(["Camille","Nicole","Mikala","Kaylen","Victoria","Francesca","Emma","Alyssa","Tori","Julia"])
ir3 = 4 
lr4 = list(["Camille","Emma","Mikala","Kaylen","Victoria","Tori","Nicole","Alyssa","Julia","Francesca"])
ir4 = 4
lr5 = list(["Camille","Emma","Mikala","Francesca","Tori","Julia","Victoria","Alyssa","Nicole","Kaylen"])
ir5 = 4
lr6 = list(["Camille","Victoria","Mikala","Francesca","Emma","Tori","Kaylen","Alyssa","Julia","Nicole"])
ir6 = 4
lr7 = list(["Francesca","Nicole","Mikala","Emma","Kaylen","Tori","Victoria","Alyssa","Julia","Camille"])
ir7 = 4

loL = list([lr1, lr2, lr3, lr4, lr5, lr6, lr7]) #add all the rounds together in a list (of lists)
loIR = list([ir1, ir2, ir3, ir4, ir5, ir6, ir7]) #and all the correct guesses

n = len(lr1)
a = list(lr1)
ix = 0

#Function

def permute(a, l, r):
    if l == r:
        checker = True
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
