def solution():
    with open('input.txt', 'r') as f:
        input = f.read()
    pt1 = part_1(input, 4)
    pt2 = part_1(input, 14)
    print(f"Part 1 solution: {pt1}")

    # part 2 was so similar to part 1 so i decided to just use the part 1 solution.
    # only difference was that the requirement for the set's length was 14 instead of 4.
    print(f"Part 2 solution: {pt2}")


def part_1(data: str, partition: int) -> int:
    # check if first _partition_ letters of string is what we're looking for 
    current_window = data[:partition]
    if(len(set(current_window)) == partition):
        return partition
    
    # else go through input string by starting from the _partition_th index and 
    # going through the first 3 letters + the next one, thus effectively iterating through the whole string 
    # as specified in description.
    # if the current window's length as a set is same as described partition i.e. all letters are different, we've reached the start of our signal
    for i, char in enumerate(data[partition:], partition):
        current_window = current_window[1:] + char
        if(len(set(current_window)) == partition):
            return i + 1




solution()