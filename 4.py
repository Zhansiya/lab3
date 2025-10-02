#void print_hello() {
#     cout << "Hello world";
# }
# def print_hello():
#     print("hello world")
#
# print_hello()

#def a_pluse_b(a, b):
#    return a + b

#print(a_pluse_b(3, 5))
#print(a_pluse_b(int(input()), int(input())))

#def power_of_two(*, n):
#    return 2 ** n

#print(power_of_two(n = int(input())))

#def get_list(*, first = "Aybek", second = "Azamat"):
#   print(first, second)

#get_list(first = "Aisulu")

def get_list(*args):
    print(args)
    print(f"First student name is {args[2]}")

get_list("Azamat", 12, "Aisulu", "Arman")