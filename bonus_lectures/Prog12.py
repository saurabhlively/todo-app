member = input("Please enter new member: ")

file = open("../files/members.txt", "r")
existing_mem = file.readlines()
file.close()

existing_mem.append(member + "\n")

file = open("../files/members.txt", 'w')
file.writelines(existing_mem)
file.close()