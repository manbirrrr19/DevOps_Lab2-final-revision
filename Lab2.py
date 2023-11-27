import statistics
print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_menu():
    print("display main_menu")

def get_user_input(num):
    nums = num.split(",")
    numlist = [float(i) for i in nums]
    print(numlist)
    return numlist

def calc_average(numlist):
    size = len(numlist)
    total = 0
    for i in range(size):
        total = total + numlist[i]
    avg = round(total/size, 2)
    print("The average is ", avg)
    return avg

def find_min_max(numlist):
    minimum = min(numlist)
    maximum = max(numlist)
    print("The minimum is ", minimum, " and the maximum is ", maximum)
    return minimum, maximum
def sort_temperature(numlist):
    numlist.sort()
    sorted_list = numlist
    print("The list in ascending order is ", sorted_list)
    return sorted_list
def calc_median_temperature(numlist):
    median = statistics.median(numlist)
    print("The median number is ", median)
    return median

if __name__ == "__main__":
    num = input("Enter a list of temperatures e.g. 1,2,3: ")
    numlist = get_user_input(num)
    calc_average(numlist)
    find_min_max(numlist)
    sort_temperature(numlist)
    calc_median_temperature(numlist)

