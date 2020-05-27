from vector import Vector

#isok

v1 = Vector(3)
print(str(v1))
v2 = Vector(3)
print(str(v2))
v3 = v1 + v2
print(v3, "=", v1, "+", v2)
v4 = v2 * v3
print(v4, "=", v2, "*", v3)
v5 = v4 - v3
print(v5, "=", v4, "-", v3)
v7 = Vector((4, 8))
v8 = v4 / 2
print(v8, "=", v4, "/", "2")

#error

v1 = Vector(12)
v2 = Vector(5)

v3 = v1 / 0

v3 = v1 + v2
