def C2F(C):
    F=(9./5)*C+32
    return F

def F2C(F):
    C=(5./9)*(F-32)
    return C

def C2K(C):
    K=C=273
    return K

def K2C(K):
    C=K-273.15
    return C

def F2K(F):
    K=F2C(F)+273.15
    return K

def K2F(K):
    F=C2F(K-273.15)
    return F


Kval = input(('Enter the Value of K='))
K = float(Kval)
F = K2F(K)
C = K2C(K)
print('Absolute Zero = %gK, %gC, %gF'%(K,C,F))

Cval = input('Enter the Value of C =')
C = float(Cval)
F = C2F(C)
K = C2K(C)
print('Freezing Point of Water = %gK, %gc, %gF'%(K,C,F))

Fval = input('Enter the Values of F =')
F = float(Fval)
K = F2K(F)
C = F2C(F)
print('Freezing point of Brine = %gK, %gC, %gF'%(K,C,F))
