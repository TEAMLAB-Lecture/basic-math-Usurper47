#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


def get_greatest(number_list:list) -> int:
  return max(number_list)


def get_smallest(number_list:list) -> int:
  return min(number_list)


def get_mean(number_list:list) -> int:
  return sum(number_list) / len(number_list)

def get_median(number_list:list) -> int:
  number_list = sorted(number_list)
  len_ = len(number_list) 
  mid = len_ // 2  
  if len_ % 2 == 0 :
    return sum(number_list[mid - 1 : mid + 1]) / 2
  else: 
    return number_list[mid]
