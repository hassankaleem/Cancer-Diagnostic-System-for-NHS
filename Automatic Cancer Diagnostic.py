import csv
import math
from collections import Counter
import random
# 1 Function
# Takes string argument
# Returns list of list with numeric values in it
def load_from_csv(filename):
    with open(filename+".csv", newline='') as file:
        my_2dlist = []
        my_2dlist = list(csv.reader(file))
        for val in range(len(my_2dlist)):
            for str in range(len(my_2dlist[val])):
                my_2dlist[val][str]=int(my_2dlist[val][str])
        return my_2dlist



# 2 Function
# Takes two parameters, both of them lists
# Returns the Euclidean distance between the two lists , return type is float
def get_distance(list_a,list_b):
    square = 0
    for index in range(len(list_a)):
        square += (list_a[index]-list_b[index])**2
    return math.sqrt(square)



# 3 Function
# Take two parameters, matrix and column no
# Column no start with 0 index value equal to first column of excel sheet
def get_avg(matrix,column_no):
    avg = 0
    sum = 0
    for val in range(len(matrix)):
        sum += matrix[val][column_no]
    avg = sum/len(matrix)
    return avg
# Function 4
# Take two parameters on list of list and the column no
# returns the standard deviation of the elements in the column number passed as parameter
def get_standard_deviation(matrix,column_no):
    square = 0
    avg = get_avg(matrix, column_no)
    for val in range(len(matrix)):
        square += ((matrix[val][column_no] - avg) ** 2)
    square = square / (len(matrix) - 1)
    return math.sqrt(square)

# print(get_standard_deviation([[1,2,3],[4,5,6],[7,8,9]],1))
# Function 5
# Take one parameter, a matrix (list of lists)
# Return a matrix containing the standardised version of the matrix passed as a parameter
def get_standardised_matrix(par_list):
    avg = 0
    std = 0
    for val in range(len(par_list[0])):
        avg = get_avg(par_list,val)
        std = get_standard_deviation(par_list,val)
        for data in range(len(par_list)):
            par_list[data][val] = (par_list[data][val] - avg) / (std)
    return par_list
# Function 6
# Takes 4 arguments
# Calculate distance between any given pl_1(list) and pl_2 (list-of-list) and save it in distance var
# Return the list with possible value of k nearest labels
def get_k_nearest_labels(pl_1,pl_2,pl_3,p_k):
    distance = []
    learn_lable = []
    for val in range(len(pl_2)):
        distance.append(get_distance(pl_1,pl_2[val]))
    # distance.sort()
    # [0,2,0,4] [0,1,2,3] >>> [0,2,1,3] >> [0,0,2,4]
    # print("Distance", distance)
    # l1 = [1, 3, 1, 4, 5]
    # print(l1)
    # for x in sorted(distance):
    #     print(x)
    l2 = [distance.index(x) for x in sorted(distance)]

    # print('l2',l2)
    for va in range(p_k):
        learn_lable.append(pl_3[l2[va]])

    #     # print(min(distance),distance.index(min(distance)),pl_3[distance.index(min(distance))],pl_3)
        # learn_lable.append(pl_3[distance.index(min(distance))])
        # pl_3.pop(distance.index(min(distance)))
        # distance.pop(distance.index(min(distance)))


    # print(learn_lable)
    return learn_lable
# print(get_k_nearest_labels([1,2,3,4],[[1,2,3,4],[1,2,3,5],[1,2,3,4]],[0,1,0],3))


# Function 7
# Takes one argument as list
# Returns the mode of the passed list
def get_mode(par_list):
    mode_list = []*len(par_list)
    for val in range(len(par_list)):
        mode_list.append(par_list[val][0])
    n = len(mode_list)
    data = Counter(mode_list)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    get_mode = mode
    return random.choice(get_mode)

# Function 8
# Takes four arguments two standardised lists of lists and learning_Data_labels and K
# Returns the data file labels list of list.
def classify(sd_1,sd_2,llabel_3,k_4):
    labels=[[]]*len(sd_1)
    for val in range(len(sd_1)):
        print(get_k_nearest_labels(sd_1[val], sd_2, llabel_3, k_4))
        labels[val] = [get_mode(get_k_nearest_labels(sd_1[val],sd_2,llabel_3,k_4))]
    return labels
# Function 9
# Takes two parameters both list of list
# Returns accuracy of predicted data labels and actual data labels
def get_accuracy(pl_1,pl_2):
    count=0
    for val in range(len(pl_1)):
        if pl_1[val] == pl_2[val]:
            count+=1
    return (count/len(pl_1))
# Function 10
# Hard-coded values for the strings containing the filenames of data, correct_data_labels, learning_data and learning_data_labels
# Generates the accuracy of model for different values of k
def run_test():
    fn_1 = get_standardised_matrix(load_from_csv("Data"))
    fn_2 = load_from_csv("Correct_Data_Labels")
    fn_3 = get_standardised_matrix(load_from_csv("Learning_Data"))
    fn_4 = load_from_csv("Learning_Data_Labels")
    knn = 3
    for val in range(knn,16,1):
        accuracy = format(get_accuracy(classify(fn_1,fn_3,fn_4,val),fn_2),'.1%')
        print("k=",val,"Accuracy=",accuracy)
run_test()