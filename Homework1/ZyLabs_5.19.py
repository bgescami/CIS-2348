# Brandon Escamilla PSID: 1823960
#(1) Output a menu of automotive services and the corresponding cost of each service.

dict = {'Oil change':35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 0 }

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")

serv1 = input("Select first service:\n")
serv2 = input("Select second service:\n\n")

total = dict[serv1] + dict[serv2]
print("Davy's auto shop invoice\n")

if serv1 == "-":
    print("Service 1: No service")
else:
    print("Service 1: " + serv1 + ", ${:.0f}".format(dict[serv1]))

if serv2 == "-":
    print("Service 2: No service\n")
else:
    print("Service 2: " + serv2 + ", ${:.0f}\n".format(dict[serv2]))

print("Total:", '${:.0f}'.format(total))



