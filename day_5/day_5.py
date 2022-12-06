
def part_1():
    part_1_answer = ''
    with open('input.txt') as f:
        # create dict where to parse stacks into
        stacks = {'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
        for line in f.readlines()[0:8]:
            # manually read from input, possibly could've done with regex and for loop to dynamically create stacks in case there were more or less of them.
            stacks['1'].insert(0,line[1])
            stacks['2'].insert(0,line[5])
            stacks['3'].insert(0,line[9])
            stacks['4'].insert(0,line[13])
            stacks['5'].insert(0,line[17])
            stacks['6'].insert(0,line[21])
            stacks['7'].insert(0,line[25])
            stacks['8'].insert(0,line[29])
            stacks['9'].insert(0,line[33])
            # remove empty entries from stack 
            for i in stacks:
                while ' ' in stacks[i]:
                    stacks[i].remove(' ')  
    # get instructions 
    with open('input.txt') as f:
        #skip over the first 10 lines of the file and get instructions
        for line in f.readlines()[10:]:
            # trim instruction line to only get things we need such as from what to where and how many times
            # order is how many times, from, to
            line = line.replace('move ', '').replace('from ', '').replace('to ', '').replace(' ', ',').replace('\n', '').split(',')
            for i in range(0, int(line[0])):
                stacks[str(line[2])].append(stacks[str(line[1])].pop())
        # get last value in stack so the 'top container' and append it to answer     
        for i in stacks: 
            part_1_answer += stacks[i][-1]

        return part_1_answer

# almost same ideas as in part 1 but here, instead of moving crates one by one, we move them all at once
def part_2():
    answer = ''
    with open('input.txt') as f:
        stacks = {'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
        for line in f.readlines()[0:8]:
            stacks['1'].insert(0,line[1])
            stacks['2'].insert(0,line[5])
            stacks['3'].insert(0,line[9])
            stacks['4'].insert(0,line[13])
            stacks['5'].insert(0,line[17])
            stacks['6'].insert(0,line[21])
            stacks['7'].insert(0,line[25])
            stacks['8'].insert(0,line[29])
            stacks['9'].insert(0,line[33])
            for i in stacks:
                while ' ' in stacks[i]:
                    stacks[i].remove(' ')  
    # helper stack                
    stacks['crate_stack'] = []
    with open('input.txt','r') as f:
        for line in f.readlines()[10:]:   
            line = line.replace('move ', '').replace('from ', '').replace('to ', '').replace(' ', ',').replace('\n', '').split(',')
            # otherwise same as part 1 but now we just move all the crates at once
            for i in range(0, int(line[0])):
                stacks['crate_stack'].append(stacks[line[1]].pop())
            for i in range(0, int(line[0])):   
                stacks[line[2]].append(stacks['crate_stack'].pop())
        # remove stack from dict
        stacks.pop('crate_stack')  
        for i in stacks: 
            answer += stacks[i][-1]
    return answer


print(f'Part 1 solution: {part_1()}')
print(f'Part 2 solution: {part_2()}')