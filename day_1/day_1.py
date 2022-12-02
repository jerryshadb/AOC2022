def solution():
    with open("input.txt", 'r') as f:
        input = f.read().split('\n\n')

    # Calculate total calories per elf and sort them to a descending order
    total_cals_per_elf = sorted([(sum(int(inventory) for inventory in elf.split("\n"))) for elf in input], reverse = True)

    # Get top three elves based on calories
    top_three_elves = total_cals_per_elf[0:3]

    print(f"Part 1 solution: {total_cals_per_elf[0]}")
    print(f"Part 2 solution: {sum(top_three_elves)}")

solution()