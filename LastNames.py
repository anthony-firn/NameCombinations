# import itertools package
import itertools
from itertools import product
FORTNER = 'fortner'
FINGER = 'finger'

def combine_sub_list(list_1, list_2):
    combined_sub = []
    for item_1 in list_1:
        for front_sub_1 in list_1[item_1][0]:
            for item_2 in list_2:
                for front_sub_2 in list_2[item_2][0]:
                    combined_sub.append(front_sub_1 + front_sub_2)
    return combined_sub

def combine_alt_sub_list(list_1, list_2):
    combined_alt_sub = []
    for item_1 in list_1:
        for front_sub_1 in list_1[item_1][0]:
            for item_2 in list_2:
                for front_sub_2 in list_2[item_2][0]:
                    for back_sub_1 in list_1[item_1][1]:
                        combined_alt_sub.append(
                            front_sub_1 + front_sub_2 + back_sub_1
                        )
    return combined_alt_sub

def get_uniq_comb(list_1, list_2):
    # create empty list to store the combinations
    unique_combinations = []

    fortner_front_sub = combine_alt_sub_list(list_1, list_2)
    finger_front_sub = combine_alt_sub_list(list_2, list_1)
    # print(fortner_front_sub, finger_front_sub)
    unique_combinations = fortner_front_sub + finger_front_sub

    return unique_combinations



def get_sub(str):
    res = [str[i: j] for i in range(len(str))
        for j in range(i + 1, len(str) + 1)]
    return res

def name_index_list(i, name, sub_names):
    return [
        [
            sub_names[i]
        ],
        sub_names[
            (len(name)*(i+1) - int((i*(i+1))/2)):
            (len(name)*(i+2) - int(((i+1)*(i+2))/2))
        ]
    ]

def get_name_dic(name, sub_names):
    dic_names = {}
    k = [0]*len(name)
    for i in range(len(name)):
        dic_names[i] = name_index_list(i, name, sub_names)
        if i > 0:
            dic_names[i][0].append(sub_names[len(name)*1 + (i-1)])
            for j in range(i-1):
                if j >= i-2:
                    k[j] = -int(((i-1)*(i+0))/2)
                else:
                    k[j] += 1

                dic_names[i][0].append(sub_names[len(name)*(j+2) + k[j]])

    return dic_names

# # generate fortner sub strings
# res_FORTNER = [FORTNER[i: j] for i in range(len(FORTNER))
#           for j in range(i + 1, len(FORTNER) + 1)]
#
# # generate fortner sub strings
# res_FINGER = [test_str[i: j] for i in range(len(FORTNER))
#           for j in range(i + 1, len(FORTNER) + 1)]

sub_FORTNER = get_sub(FORTNER)
sub_FINGER = get_sub(FINGER)
dic_FORTNER = get_name_dic(FORTNER, sub_FORTNER)
dic_FINGER = get_name_dic(FINGER, sub_FINGER)

print("sub strings:")
print(sub_FORTNER)
print(sub_FINGER)


# python program to demonstrate
# unique combination of two lists
# using zip() and product() of itertools



# initialize lists
# sub_FORTNER = ["bz","c","d"]
# sub_FINGER = ["a", "b"]

# # create empty list to store the combinations
# unique_combinations = []
#
# # Extract Combination Mapping in two lists
# # using zip() + product()
# unique_combinations = list(list(zip(sub_FORTNER, element))
#                            for element in product(sub_FINGER, repeat = len(sub_FORTNER)))
unique_combinations = get_uniq_comb(dic_FORTNER, dic_FINGER)

# printing unique_combination list
# print("strings combined")
# print(unique_combinations)

file=open('unique_comb.txt','w')
for items in str(unique_combinations):
    file.writelines([items])

file.close()
