#Functon to calcuate hcf
def calculate_hcf(x,y)
#Selecting small number 
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x%i == 0) and (y%i == 0)):
            HCF=1
    return HCF

#Taking input from user
n1=int(input("Enter the first number")) 
n1=int(input("Enter the second number"))    

print("HCF of",n1,"And",n2,"Is",calculate_hcf(n1,n2))