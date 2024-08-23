def clean(value):
    for character in value:
        if character == " ":
            value = value.replace(character, "")
    return value

try:
    class_amount = int(clean(input('How many classes do you have? ')))
    ap_amount = int(clean(input("How many AP courses do you have? ")))
except ValueError:
    print("Your class amount/AP's should be an integer, not a float, string, etc.\n")
    exit()

if class_amount > 8 or ap_amount > 8:
    print("Your class amount/AP's should be below eight.\n")
    exit()

GPA = 0
print('\nPlease enter the classes as strings: Ex(A+, A, A-): ')
print("You don't need to indicate if the course is AP or not, it will be automatically factored in.\n")
for value in range(class_amount):
    grade = clean(input('Class {integer}: '.format(integer = value+1)).lower())
    if grade == 'a+':
        grade = 4.33
    elif grade == 'a':
        grade = 4
    elif grade == 'a-':
        grade = 3.67
    elif grade == 'b+':
        grade = 3.33
    elif grade == 'b':
        grade = 3
    elif grade == 'b-':
        grade = 2.67
    elif grade == 'c+':
        grade = 2.33
    elif grade == 'c':
        grade = 2
    elif grade == 'c-':
        grade = 1.67
    elif grade == 'd+':
        grade = 1.33
    elif grade == 'd':
        grade = 1
    elif grade == 'd-':
        grade = .67
    elif grade == 'f':
        grade = 0
    else:
        print('\nInvalid input. Please retry using stringed format. Ex(A+, A, A-).')
        exit()
    GPA+=grade

if ap_amount != 0:
    value = .333
    GPA+=(value*ap_amount)

GPA = round(GPA/class_amount, 2)
print('Your GPA is: {GPA} '.format(GPA=GPA))
print('Thanks for running our program.\n')
