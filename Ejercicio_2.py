
def fxn(stng):   
    A = stng[0] 
    
    for i in range(1, len(stng)): 
        if stng[i-1] == ' ': 
            
            
            A += stng[i] 
              
    A = A.upper() 
    return A
  
print("Escriba la oracion a sacar su acronimo")
B = input()
  
print(fxn(B)) 
