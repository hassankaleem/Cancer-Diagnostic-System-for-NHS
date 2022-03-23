import csv
import math
import statistics as stat
from collections import Counter
import random
# 1 function
# Takes string argument
# Returns list of list with numeric values in it
def load_from_csv(filename):
    with open(filename+".csv", newline='') as file:
        my_2dlist = []
        my_2dlist = list(csv.reader(file))
        for val in range(len(my_2dlist)):
            for str in range(len(my_2dlist[val])):
                my_2dlist[val][str]=int(my_2dlist[val][str])
        # print(my_2dlist)
        # print(type(my_2dlist[0][0]))
        return my_2dlist
# print(load_from_csv("Data"))

# 2 function
# Takes two parameters, both of them lists
# Returns the Euclidean distance between the two lists , return type is float
def get_distance(list_a,list_b):
    square = 0
    for index in range(len(list_a)):
        square += (list_a[index]-list_b[index])**2
    return math.sqrt(square)

# print(get_distance([1,2,3],[1,2,3]))
# 3 Function
# Take two parameters, matrix and column no
# Column no start with 0 index value equal to first column of excel sheet
def get_avg(matrix,column_no):
    avg = 0
    sum = 0
    for val in range(len(matrix)):
        sum += matrix[val][column_no]
    avg = sum/len(matrix)
    # print(avg)
    return avg
# print(get_avg([[1,2,3],[4,5,6],[7,8,9]],0))
def get_standard_deviation(matrix,column_no):
    square=0
    avg = get_avg(matrix,column_no)
    for val in range(len(matrix)):
        square += ((matrix[val][column_no]-avg)**2)
    square = square / (len(matrix)-1)
    return math.sqrt(square)
# print(get_standard_deviation([[1,2,3],
#                               [4,5,6],
#                               [7,8,9]],0))

# Take one parameter, a matrix (list of lists)
# Return a matrix containing the standardised version of the matrix passed as a parameter
def get_standardised_matrix(par_list):
    # var_list = [[]*len(par_list)]*len(par_list)
    avg = 0
    std = 0
    for val in range(len(par_list[0])):
        avg = get_avg(par_list,val)
        std = get_standard_deviation(par_list,val)
        # // call agv and get sat
        for data in range(len(par_list)):
            # print(par_list[data][val], val, data, get_avg(par_list, val), par_list, var_list)
            par_list[data][val] = (par_list[data][val] - avg) / (std)
            # var_list.append([(par_list[data][val] - get_avg(par_list, val)) / (get_standard_deviation(par_list, val))])
    # print(par_list)
    return par_list
# get_standardised_matrix(load_from_csv("Learning_Data"))
    # print(get_standard_deviation(par_list,val))
    #
    # for i in range(len(par_list)):
    #     for j in range(len(par_list[i])):
    #         print(par_list[i][j])

        # print(val)
# get_standardised_matrix([[1,2,3],[4,5,6],[7,8,9]])

# print(len(get_standardised_matrix(load_from_csv("Learning_Data"))))

# Function should have four parameters
# 1 for-loop calculate distance between pl_1(list) and pl_2 (list-of-list) and save it in distance var
# pl_3 is learning data lable , p_k take value of k
def get_k_nearest_labels(pl_1,pl_2,pl_3,p_k):
    distance = []
    learn_lable = []
    for val in range(len(pl_2)):
        distance.append(get_distance(pl_1,pl_2[val]))
    for va in range(p_k):
        learn_lable.append(pl_3[distance.index(min(distance))])
        distance.pop(distance.index(min(distance)))
    # print(learn_lable)
    return learn_lable
#         # print(learn_lable)
#         # empyty = load_from_csv("Learning_Data_Labels")
#     # print(distance)
# #     # print(distance)
# print(get_k_nearest_labels([0.21246335637467315, 0.28274411053763127, 0.9164989661098344, 1.098373130225817, 0.35576325467852093, 1.8453610721159155, 0.19794362630407297, 0.05440216697768479, -0.33898067042109864],
#                      get_standardised_matrix(load_from_csv("Learning_Data")),load_from_csv("Learning_Data_Labels"),3))


print(load_from_csv("Learning_Data_Labels"))
print(load_from_csv("Learning_Data_Labels")[201])
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

    # print(random.choice(get_mode))
# #     # print(get_mode)
# #     # print(mode_list)

# print(get_mode([[0],[1],[0],[0],[1],[1],[1],[0],[0]]))

def classify(sd_1,sd_2,llabel_3,k_4):
    labels=[[]]*len(sd_1)
    # print(sd_1,sd_2,llabel_3,k_4)
    for val in range(len(sd_1)):
        # print(get_k_nearest_labels(sd_1[val],sd_2,llabel_3,k_4))
        # print(get_mode(get_k_nearest_labels(sd_1[val],sd_2,llabel_3,k_4)))
        labels[val] = [get_mode(get_k_nearest_labels(sd_1[val],sd_2,llabel_3,k_4))]
        # print(get_mode(get_k_nearest_labels(sd_1[val],sd_2,llabel_3,k_4)))
    # print("Labels for Data File",labels)
    # print(load_from_csv("Correct_Data_Labels"))
    return labels
# classify(get_standardised_matrix(load_from_csv("Data")),get_standardised_matrix(load_from_csv("Learning_Data")),load_from_csv("Learning_Data_Labels"),4)
# # # # Takes two parameters both list of list
# # # # Return accuracy of predicted data labels and actual data labels
def get_accuracy(pl_1,pl_2):
    print(pl_1)
    print(pl_2)
    count=0
    for val in range(len(pl_1)):
        if pl_1[val] == pl_2[val]:
            count+=1
    accuracy=count/len(pl_1)
    # print(format(accuracy,'.0%'))
    return format(accuracy,'.0%')
# get_accuracy([1,1,1,1,1,1],[1,1,1,1,0,0])

# # get_accuracy(classify(get_standardised_matrix(load_from_csv("Data")),get_standardised_matrix(load_from_csv("Learning_Data")),load_from_csv("Learning_Data_Labels"),4),load_from_csv("Correct_Data_Labels"))
# # # #
# # # # # Hard-coded values for the strings containing the filenames of data, correct_data_labels, learning_data and learning_data_labels
# # # # # Generates the accuracy of model for different valuse of k
def run_test():
    fn_1 = get_standardised_matrix(load_from_csv("Data"))
    fn_2 = load_from_csv("Correct_Data_Labels")
    fn_3 = get_standardised_matrix(load_from_csv("Learning_Data"))
    fn_4 = load_from_csv("Learning_Data_Labels")
    knn  = 3
    for val in range(knn,15,1):
        print("k=",val,"Accuracy=",get_accuracy(classify(fn_1,fn_3,fn_4,val),fn_2))
run_test()