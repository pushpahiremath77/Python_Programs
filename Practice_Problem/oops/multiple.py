class A:
    var_a = "Pushpa"

class B:
    var_b = "Hiremath"

class C(A,B):
    var_c = "Welcome"

c1 = C()

print(c1.var_c)
print(c1.var_a)
print(c1.var_b)
