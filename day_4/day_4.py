def solution():
    with open('input.txt', 'r') as f:
        input = f.read().split('\n')

    assignments_overlap = 0
    pair_overlap = 0
    # go through assignments in input
    for assignment in input:
        # split the assignments into two, so 1 per elf and give each elf a starting and ending point (so their sections)
        assignment_1, assignment_2 = assignment.split(',')
        elf_1_start, elf_1_end = [int(r) for r in assignment_1.split('-')]
        elf_2_start, elf_2_end = [int(r) for r in assignment_2.split('-')]

        # check whether either one of them fully contain the other by comparing starting and ending values
        if (elf_1_start <= elf_2_start and elf_1_end >= elf_2_end) or (elf_2_start <= elf_1_start and elf_2_end >= elf_1_end):
            assignments_overlap += 1
        
        # create a list of starting and ending points
        range_1 = list(range(elf_1_start, elf_1_end + 1))
        range_2 = list(range(elf_2_start, elf_2_end + 1))

        # check if sections of the 1st elf are in the sections of the 2nd elf (so mutual overlap anywhere in assignments)
        overlap = [i for i in range_1 if i in range_2]

        # if there were any, there was some
        if len(overlap) > 0:
            pair_overlap += 1

    print(f"Part 1 solution: {assignments_overlap}")
    print(f"Part 2 solution: {pair_overlap}")

solution()