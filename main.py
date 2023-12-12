variable_a = input("masukan value variable a : ")
print(variable_a)
variable_b = input("masukan value variable b : ")
print(variable_b)
variable_operator = input("masukan operator : ")


if variable_operator == "+":
    # ketika variable a dan b ditambah akan muncul hasil tambah 
    try:
        variable_c = int(variable_a) + int(variable_b)
        print(variable_c)
    except Exception as error:
        print("variabel a dan b harus berupa angka",error)
elif variable_operator == "-":
    try:
        variable_c = int(variable_a) - int(variable_b)
        print(variable_c)
    except Exception as error:
        print("variabel a dan b harus berupa angka",error)
    variable_c = int(variable_a) - int(variable_b)
    print(variable_c)
elif variable_operator == "*":
    try:
        variable_c = int(variable_a) * int(variable_b)
        print(variable_c)
    except Exception as error:
        print("variabel a dan b harus berupa angka",error)
    variable_c = int(variable_a) * int(variable_b)
    print(variable_c)
elif variable_operator == "/":
    try: 
        variable_c = int(variable_a) / int(variable_b)
        print(variable_c)
    except Exception as error:
        print("variabel a dan b harus berupa angka",error)
    variable_c = int(variable_a) / int(variable_b)
    print(variable_c)
elif variable_operator == "%":
    try:
        variable_c = int(variable_a) % int(variable_b)
        print(variable_c)
    except Exception as error:
        print("variabel a dan b harus berupa angka",error)
    variable_c = int(variable_a) % int(variable_b)
    print(variable_c)
else : 
    print("operator tidak diketahui")

print("Hello SEPTIANA HENDRAWATI!")