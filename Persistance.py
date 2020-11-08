
import timeit

def multi_number(num, steps):
    """
    :param num: number to be multiplied
    :return: the steps number
    """

    if steps == 0:
        print("Start:", num)
    else:
        print(num)

    digits = [int(i) for i in str(num)]
    result = 1
    for j in digits:
        result *= j

    if len(str(num))> 1:
        steps += 1
        steps = multi_number(result, steps)
        return steps

    else:
        print("Step: ", steps)
        return steps



def check_num(num):
    """
    Check if number is containg 0,5 or other number
    and the Order
    check if the order if the digit is increasing
    :param num:
    :return: True or False
    """
    str_num = str(num)

    if "0" in str_num:
        return False
    if "5" in str_num:
        return False
    if str_num != ''.join(sorted(str_num)):
        return False

    return True

start = timeit.default_timer()
x = 277777788888800
below_11 = True

while below_11:

    #time.sleep(1)
    counter = 0
    if check_num(x) == True:
        counter = multi_number(x, counter)
        print("Done")
        if counter > 9:
            with open("nb_step_above_10.txt", 'a') as file:
                record = str(x) + " nb of Step: " + str(counter) + "\n"
                file.write(record)
            if counter > 11:
                below_11 = False
    else:
        #print("Reject number:", x)
        pass

    if (x % 10000000) == 0:
        with open("nb_step_above_10.txt", 'a') as file:
            record = "Last number check: " + str(x) + "\n"
            print(record)
            file.write(record)
        # Test Time
        below_11 = False
    x += 1

stop = timeit.default_timer()

print('Time: ', stop - start)