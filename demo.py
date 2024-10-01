def demo_func(propA, propB, *context):
    print(propA)
    print(propB)
    print(type(context))

# the "context" by the docs is a List()

demo_func("A", "B", 1, 2, 3)