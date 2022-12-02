def solution():
    with open('input.txt', 'r') as f:
        input = f.read().split('\n')
    part_1 = 0
    part_2 = 0
    # loop through games in input.txt
    for game in input:
        # tuple of played choices by elf and I
        elf, me = game.split()
        # dict of my choices and their corresponding points
        part_1 += {'X': 1, 'Y': 2, 'Z': 3}[me]

        # possible outcomes of games
        part_1 += {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
                ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
                ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
                }[(elf, me)]

        # loss, draw, win
        part_2 += {'X': 0, 'Y': 3, 'Z': 6}[me]

        # my hand shape in correspondance to the desired outcome: 
        # Elf plays 'A', rock, and I need to lose so I pick scissors thus giving me 3 points for my choice
        part_2 += {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
                ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
                ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1,
                }[(elf, me)]

    print(f"Total score for part 1: {part_1}")
    print(f"Total score for part 2: {part_2}")


solution()