#Write your function here
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

def max_num(nums):
    max = nums[0]
    for number in nums:
        if (number > max):
            max = number
    return max
print(max_num([50, -10, 0, 75, 20]))

##looks through two list and sees if it has any matching indexs
## if any Indexs match they're added to a new list
def same_values(lst1,lst2):
    new_lst = []
    for index in range(len(lst1)):
        if lst1[index] == lst2[index]:
            new_lst.append(index)
    return new_lst
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


## Compares list to see if the first matches the second backwards
def reversed_list(lst1,lst2):
    for index in range(len(lst1)):
        if lst1[index] != lst2[len(lst2) - 1 - index]:
            return False
    return True
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))