# open file:
# file = open("new_file.txt")
# read file:
# content = file.read()
# print(content)
# file.close()

# или открыть файл, считать и закрыть можно командой:
with open("new_file.txt") as file:
    content = file.read()
    print(content)

# записать новое содержимое в файл, но нужно в скобках указать режим, т к по умолчанию стоит чтение файла:
with open("new_file.txt", mode="w") as file:
    file.write("Hello. What is your name?")
# создать новый файл и добавить в него запись:
with open("second_file.txt", mode="w") as file_1:
    file_1.write("Call me Litviakova")