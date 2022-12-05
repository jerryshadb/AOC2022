def solution():
    with open('input.txt', 'r') as f:
        input = f.read().split('\n')

    assignments_overlap = 0
    pair_overlap = 0
    for assignment in input:
        assignment_1, assignment_2 = assignment.split(',')
        elf_1_start, elf_1_end = [int(r) for r in assignment_1.split('-')]
        elf_2_start, elf_2_end = [int(r) for r in assignment_2.split('-')]

        if (elf_1_start <= elf_2_start and elf_1_end >= elf_2_end) or (elf_2_start <= elf_1_start and elf_2_end >= elf_1_end):
            assignments_overlap += 1
        
        range_1 = list(range(elf_1_start, elf_1_end + 1))
        range_2 = list(range(elf_2_start, elf_2_end + 1))
        
        overlap = [i for i in range_1 if i in range_2]

        if len(overlap) > 0:
            pair_overlap += 1

    print(f"Part 1 solution: {assignments_overlap}")
    print(f"Part 2 solution: {pair_overlap}")

solution()