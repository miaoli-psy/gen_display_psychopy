import random
import ast


def get_position_list(df, col_name):
    '''
    df: dataframe that that contains col of positions
    col_name: str
    '''
    # get list like str
    list_like_str = df[col_name].tolist()
    # return list of positions
    return [ast.literal_eval(i) for i in list_like_str]


def select_random_half(posilist):
    n = int(len(posilist) / 2)
    return random.sample(posilist, n)


def get_diff_between_2_lists(list1, list2):
    li_dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
    return li_dif