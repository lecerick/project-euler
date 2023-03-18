import itertools

element_orders=      [list(perm) for perm in itertools.permutations(range(5),5)]
coefficient_combos=  [list(perm) for perm in itertools.combinations_with_replacement(range(5),15)]

def polynomial(x: int, y: int, coeffs: list):
    return (coeffs[0]  + coeffs[1]*x + coeffs[2]*y + coeffs[3]*(x^2) + coeffs[4]*(y^2) + coeffs[5]*(x^3) + coeffs[6]*(y^3) + coeffs[7]*(x^4) + coeffs[8]*(y^4) + coeffs[9]*(x^5) + coeffs[10]*(y^5)  + coeffs[11]*(x^6) + coeffs[12]*(y^6) + coeffs[13]*(x^7) + coeffs[14]*(y^7)) % 5
def print_polynomial(coeffs: list):
    print('{} + {}x + {}y + {}x^2 + {}y^2 + {}x^3 + {}y^3 + {}x^4 + {}y^4 + {}x^5 + {}y^5 + {}x^6 + {}y^6 + {}x^7 + {}y^7'.format(*coeffs))

def convertTuple(tup):
    return '('+','.join([str(x) for x in tup])+')'
def solver(a,b,c,d,e):
    star = {
        (a,a): a,
        (a,b): d,
        (a,d): c,
        (a,e): d,
        (b,a): c,
        (b,b): d,
        (b,c): d,
        (b,d): a,
        (b,e): c,
        (c,b): e,
        (c,c): d,
        (c,d): b,
        (c,e): d,
        (d,a): a,
        (d,d): b,
        (d,e): c,
        (e,a): b,
        (e,b): b,
        (e,c): c,
        (e,e): a 
    }
    polys = {}
    for coeff in coefficient_combos:
        if all([polynomial(combo[0],combo[1],coeff)==star[combo] for combo in star]):
            print("solution = ")
            print_polynomial(coeff)
            return True
    return False

for vars in element_orders:
    Solution_found = solver(*vars)
if Solution_found == False:
    print("Sorry no luck")