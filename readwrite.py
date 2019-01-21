#read name.txt
with open('name.txt') as f:
    my_name = f.read()

print(my_name)
#greeting = "Heloo"
greeting = "Hello my name is" + my_name + "."

#writing a text file 
with open('hello.txt', 'w') as f:
    f.write(greeting)
    f.write('\n')