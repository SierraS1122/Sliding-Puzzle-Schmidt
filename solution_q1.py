
#Geez I haven't had to code in ages


def representation(lst):
    print(lst[0],lst[1],lst[2])
    print(lst[3],lst[4],lst[5])
    print(lst[6],lst[7],lst[8])

file = open("input.txt",r"r")
input_str = file.read()
#print(input_str)
file.close()

#print(type(input_str))

input_lst = input_str.split(',')
#print(input_lst)
#print(type(input_lst))

cur_lst = input_lst

print("Starting Puzzle")
representation(cur_lst)

#Top Left Empty Moves
if cur_lst[0] == "_":
    
    #Option 1 (Number Right)
        opt1_lst = cur_lst.copy()
        opt1_lst[0] = cur_lst[1]
        opt1_lst[1] = cur_lst[0]
        print('')
        print("Move:", opt1_lst[0],'L', sep='')
        representation(opt1_lst)

    #Option 2 (Number Below)
        opt2_lst = cur_lst.copy()
        opt2_lst[0] = cur_lst[3]
        opt2_lst[3] = cur_lst[0]
        print('')
        print("Move:", opt2_lst[0],'U', sep='')
        representation(opt2_lst)
        
    



#Top Middle Empty Moves
if cur_lst[1] == "_":
    #Option 1 (Number Left)
        opt1_lst = cur_lst.copy()
        opt1_lst[1] = cur_lst[0]
        opt1_lst[0] = cur_lst[1]
        print('')
        print("Move:", opt1_lst[1],'R', sep='')
        representation(opt1_lst)

    #Option 2 (Number Right)
        opt2_lst = cur_lst.copy()
        opt2_lst[1] = cur_lst[2]
        opt2_lst[2] = cur_lst[1]
        print('')
        print("Move:", opt2_lst[1],'L', sep='')
        representation(opt2_lst)
              
    #Option 3 (Number Below)
        opt3_lst = cur_lst.copy()
        opt3_lst[1] = cur_lst[4]
        opt3_lst[4] = cur_lst[1]
        print('')
        print("Move:", opt3_lst[1],'U', sep='')
        representation(opt3_lst)
              
#Top Right Empty Moves
if cur_lst[2] == "_":
    
    #Option 1 (Number Left)
        opt1_lst = cur_lst.copy()
        opt1_lst[2] = cur_lst[1]
        opt1_lst[1] = cur_lst[2]
        print('')
        print("Move:", opt1_lst[2],'R', sep='')
        representation(opt1_lst)

    #Option 2 (Number Below)
        opt2_lst = cur_lst.copy()
        opt2_lst[2] = cur_lst[5]
        opt2_lst[5] = cur_lst[2]
        print('')
        print("Move:", opt2_lst[2],'U', sep='')
        representation(opt2_lst)
   

#Middle Left Empty Moves
if cur_lst[3] == "_":
    #Option 1 (Number Up)
        opt1_lst = cur_lst.copy()
        opt1_lst[3] = cur_lst[0]
        opt1_lst[0] = cur_lst[3]
        print('')
        print("Move:", opt1_lst[3],'D', sep='')
        representation(opt1_lst)

    #Option 2 (Number Right)
        opt2_lst = cur_lst.copy()
        opt2_lst[3] = cur_lst[4]
        opt2_lst[4] = cur_lst[3]
        print('')
        print("Move:", opt2_lst[3],'L', sep='')
        representation(opt2_lst)
              
    #Option 3 (Number Below)
        opt3_lst = cur_lst.copy()
        opt3_lst[3] = cur_lst[6]
        opt3_lst[6] = cur_lst[3]
        print('')
        print("Move:", opt3_lst[3],'U', sep='')
        representation(opt3_lst)



#Middle Middle Empty Moves
if cur_lst[4] == "_":
    #Option 1 (Number Up)
        opt1_lst = cur_lst.copy()
        opt1_lst[4] = cur_lst[1]
        opt1_lst[1] = cur_lst[4]
        print('')
        print("Move:", opt1_lst[4],'D', sep='')
        representation(opt1_lst)

    #Option 2 (Number Right)
        opt2_lst = cur_lst.copy()
        opt2_lst[4] = cur_lst[5]
        opt2_lst[5] = cur_lst[4]
        print('')
        print("Move:", opt2_lst[4],'L', sep='')
        representation(opt2_lst)
              
    #Option 3 (Number Below)
        opt3_lst = cur_lst.copy()
        opt3_lst[4] = cur_lst[7]
        opt3_lst[7] = cur_lst[4]
        print('')
        print("Move:", opt3_lst[4],'U', sep='')
        representation(opt3_lst)

    #Option 4 (Number Left)
        opt4_lst = cur_lst.copy()
        opt4_lst[4] = cur_lst[3]
        opt4_lst[3] = cur_lst[4]
        print('')
        print("Move:", opt4_lst[4],'R', sep='')
        representation(opt4_lst)

#Middle Right Empty Moves
if cur_lst[5] == "_":
    #Option 1 (Number Up)
        opt1_lst = cur_lst.copy()
        opt1_lst[5] = cur_lst[2]
        opt1_lst[2] = cur_lst[5]
        print('')
        print("Move:", opt1_lst[5],'D', sep='')
        representation(opt1_lst)

    #Option 2 (Number Left)
        opt2_lst = cur_lst.copy()
        opt2_lst[5] = cur_lst[4]
        opt2_lst[4] = cur_lst[5]
        print('')
        print("Move:", opt2_lst[5],'R', sep='')
        representation(opt2_lst)
              
    #Option 3 (Number Below)
        opt3_lst = cur_lst.copy()
        opt3_lst[5] = cur_lst[8]
        opt3_lst[8] = cur_lst[5]
        print('')
        print("Move:", opt3_lst[5],'U', sep='')
        representation(opt3_lst)

#Bottom Left Empty Moves
if cur_lst[6] == "_":
    #Option 1 (Number Up)
        opt1_lst = cur_lst.copy()
        opt1_lst[6] = cur_lst[3]
        opt1_lst[3] = cur_lst[6]
        print('')
        print("Move:", opt1_lst[6],'D', sep='')
        representation(opt1_lst)

    #Option 2 (Number Right)
        opt2_lst = cur_lst.copy()
        opt2_lst[6] = cur_lst[7]
        opt2_lst[7] = cur_lst[6]
        print('')
        print("Move:", opt2_lst[6],'L', sep='')
        representation(opt2_lst)
              

#Bottom Middle Empty Moves
if cur_lst[7] == "_":
    #Option 1 (Number Up)
        opt1_lst = cur_lst.copy()
        opt1_lst[7] = cur_lst[4]
        opt1_lst[4] = cur_lst[7]
        print('')
        print("Move:", opt1_lst[7],'D', sep='')
        representation(opt1_lst)

    #Option 2 (Number Right)
        opt2_lst = cur_lst.copy()
        opt2_lst[7] = cur_lst[8]
        opt2_lst[8] = cur_lst[7]
        print('')
        print("Move:", opt2_lst[7],'L', sep='')
        representation(opt2_lst)

    #Option 3 (Number Left)
        opt3_lst = cur_lst.copy()
        opt3_lst[7] = cur_lst[6]
        opt3_lst[6] = cur_lst[7]
        print('')
        print("Move:", opt3_lst[7],'R', sep='')
        representation(opt3_lst)
              
#Bottom Right Empty Moves
if cur_lst[8] == "_":
    #Option 1 (Number Up)
        opt1_lst = cur_lst.copy()
        opt1_lst[8] = cur_lst[5]
        opt1_lst[5] = cur_lst[8]
        print('')
        print("Move:", opt1_lst[8],'D', sep='')
        representation(opt1_lst)

    #Option 2 (Number Left)
        opt2_lst = cur_lst.copy()
        opt2_lst[8] = cur_lst[7]
        opt2_lst[7] = cur_lst[8]
        print('')
        print("Move:", opt2_lst[8],'R', sep='')
        representation(opt2_lst)

