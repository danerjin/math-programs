import copy

eq = input()
def f(x):
    return eval(eq)
def computeGCD(x, y):
    while(y):
        x, y = y, x % y
    return abs(x)
def simplify_fraction(p,q):
    return (round(p/computeGCD(p,q)),round(q/computeGCD(p,q)))
def factors(x):
    fac=[]
    for i in range(1,round(x**0.5+1)):
        if x%i == 0:
            fac+=[i]
    fac2 = copy.copy(fac)
    for thing in fac2:
        fac+=[round(x/thing)]
    return fac
constant_term = f(0)
first = ''
for i in eq:
    if i == 'x' or i == "*":
        if first == "":
            first = '1'
        break
    else:
        first+=i
first = int(first)
p = factors(abs(constant_term))
q = factors(abs(first))
roots = []
for pv in p:
    for qv in q:
        if abs(f(pv/qv)) <= 0.001 and str(pv/qv) not in roots and f"{simplify_fraction(pv,qv)[0]}/{simplify_fraction(pv,qv)[1]}" not in roots:
            if pv/qv % 1 == 0:
                roots+=[str(round(pv/qv))]
            else:
                roots+=[f"{simplify_fraction(pv,qv)[0]}/{simplify_fraction(pv,qv)[1]}"]
        elif abs(f(-pv/qv)) <= 0.001 and str(-pv/qv) not in roots and f"{-simplify_fraction(pv,qv)[0]}/{simplify_fraction(pv,qv)[1]}" not in roots:
            if -pv/qv % 1 == 0:
                roots+=[str(round(-pv/qv))]
            else:
                roots+=[f"{-simplify_fraction(pv,qv)[0]}/{simplify_fraction(pv,qv)[1]}"]
roots2=[]
for root in roots:
    if root not in roots2:
        print(root)
        roots2+=[root]
