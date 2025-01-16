# Loop within another loop
# Outer loop, inner loop

# range()
# used to generate sequence of numbers
# start, stop, step
# START: optional; default start is 0, unless specified
# STOP: required; number specifying postion to stop (exclusive)
# STEP: optional;  default skip is 1, number specifying the amount to skip


# # Prints 0 - 2
# for x in range(3):
#     print(x)

# # Prints 1 - 3
# for x in range(1, 4):
#     print(x)


# # By default print will "print" on a new line each iteration
# # You can change this using end="" 
# for a in range(3):
#     for b in range(4):
#         print(b, end=" ") # prints on the same line separated by a single space
#     print("") 



# step can also be used to generate a sequence that counts down
# in this case, you will need to reverse the start and stop values, and specify a negative step 
for x in range(10, -4, -2):
    print(x)





