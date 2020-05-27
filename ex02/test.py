from vector import Vector

# isok

v1 = Vector(3)
print(str(v1))
v2 = Vector(3)
print(str(v2))
v3 = v1 + v2
print(v3, "=", v1, "+", v2)
v4 = v2 * v3
print(v4, "=", v2, "*", v3)
v4 = Vector(3)
v5 = v4 - v3
print(v5, "=", v4, "-", v3)
v7 = Vector((4, 8))
v8 = v4 / 2
print(v8, "=", v4, "/", "2")

v10 = Vector(5)
v11 = Vector(5)
v12 = v10 * v11
print(v12, "=", v11, "*", v12)

# error

v1 = Vector(12)
v2 = Vector(5)

try:
    v3 = v1 / 0
except Exception as e:
    print(e)

try:
    v12 = v1 + v2
except Exception as e:
    print(e)

try:
    v1 * v2
except Exception as e:
    print(e)
