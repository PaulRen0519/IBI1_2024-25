#Aim: to calculate and print the first ten values
#initiate the counter
counter = 1
#start loop
#while counter less than 11, keep adding from 1 to n
while counter <= 10:
    #initiate the triangle sequence
    sum = 0
    #calculate the triangle sequence
    for i in range(1, counter + 1):
        sum = sum + i
    #output the value
    print(sum)
    #counter plus 1
    counter += 1