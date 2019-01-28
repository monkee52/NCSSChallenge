numbers = input("Number: ")

def go():
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in numbers:
        nums[int(i)] += 1

    valid = True

    for i in range(0, min(len(numbers), 10)):
        if (int(numbers[i]) != nums[i]):
            valid = False
            break

    if (valid):
        print("%s is autobiographical" % numbers)
    else:
        print("%s is not autobiographical" % numbers)

if (len(numbers) > 10):
    print("%s is not autobiographical" % numbers)
else:
    go()
