import string
#### PART 1 helper functions ####
# divides the items in the rucksack into two separate compartments
def divide_items(item: str)-> tuple:
    return item[:len(item) // 2], item[len(item) // 2:]

# find mutual items in compartment
def get_same_item(item: str) -> str:
    first_half, second_half = divide_items(item)

    return ''.join(set(first_half).intersection(second_half))


#### PART 2 helper functions ####
# divide elves into groups of three 
def divide_to_groups(list_of_elves: list) -> list:  
    groups = list()
    for i in range(0, len(list_of_elves), 3):
        groups.append(list_of_elves[i:i + 3])

    return groups

# get score of item
def score(char: str) -> int:
    return string.ascii_letters.index(char) + 1

# get mutual item in group of elves
def find_mutual_in_group(group: list)-> str:
    return ''.join(set(group[0]).intersection(group[1]).intersection(group[2]))

def solution():
    with open('input.txt', 'r') as f:
        input = f.read().split('\n')

    
    priority_sum_part_1 = 0
    for item in input:
        mutual_item = get_same_item(item)
        priority_sum_part_1 += score(mutual_item)

    priority_sum_part_2 = 0
    for group in divide_to_groups(input):
        mutual_item_in_group = find_mutual_in_group(group)
        priority_sum_part_2 += score(mutual_item_in_group)

    print(f"Part 1 solution: {priority_sum_part_1}")
    print(f"Part 2 solution: {priority_sum_part_2}")


solution()

