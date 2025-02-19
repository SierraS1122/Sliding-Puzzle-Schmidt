#Geez I haven't had to code in ages

goal_state = ['1','2','3','8','_','4','7','6','5']
found_solution = False

def representation(lst):
    pass
    #print(lst[0],lst[1],lst[2])
    #print(lst[3],lst[4],lst[5])
    #print(lst[6],lst[7],lst[8])

file = open("input.txt","r")
input_str = file.read()
##print(input_str)
file.close()

##print(type(input_str))

input_lst = input_str.split(',')
##print(input_lst)
##print(type(input_lst))

cur_lst = input_lst
cur_action = []

state_queue = []
state_queue += [cur_lst]

action_queue = [[]]
action_queue += cur_action
states_visited = []

states_visited += [cur_lst]

#print("Starting Puzzle")
representation(cur_lst)

def generate_next_states(cur_lst, state_queue, cur_action, action_queue, states_visited, found_solution):
    #Top Left Empty Moves
    
    if cur_lst[0] == "_":
        
        if found_solution == False:
        #Option 1 (Number Right)
            opt1_lst = cur_lst.copy()
            opt1_lst[0] = cur_lst[1]
            opt1_lst[1] = cur_lst[0]
            #print('')
            move = opt1_lst[0]+'L'
            #print("Move:", move) 
            representation(opt1_lst)

            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
                
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)

        if found_solution == False:
        #Option 2 (Number Below)
            opt2_lst = cur_lst.copy()
            opt2_lst[0] = cur_lst[3]
            opt2_lst[3] = cur_lst[0]
            #print('')
            move = opt2_lst[0]+'U'
            #print("Move:", move)
            representation(opt2_lst)
            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
        



    #Top Middle Empty Moves
    if cur_lst[1] == "_":

        if found_solution == False:  
        #Option 1 (Number Left)
            opt1_lst = cur_lst.copy()
            opt1_lst[1] = cur_lst[0]
            opt1_lst[0] = cur_lst[1]
            #print('')
            move = opt1_lst[1]+'R'
            #print("Move:", move)
            representation(opt1_lst)

            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
        
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)

        #Option 2 (Number Right)
        if found_solution == False:  
            opt2_lst = cur_lst.copy()
            opt2_lst[1] = cur_lst[2]
            opt2_lst[2] = cur_lst[1]
            #print('')
            move = opt2_lst[1]+'L'
            #print("Move:", move)
            representation(opt2_lst)

            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                
        #Option 3 (Number Below)
        if found_solution == False:  
            opt3_lst = cur_lst.copy()
            opt3_lst[1] = cur_lst[4]
            opt3_lst[4] = cur_lst[1]
            #print('')
            move = opt3_lst[1]+'U'
            #print("Move:", move)
            representation(opt3_lst)
            if opt3_lst == goal_state:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            

            if opt3_lst not in states_visited:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                
                
    #Top Right Empty Moves
    if cur_lst[2] == "_":
        
        if found_solution == False:
        #Option 1 (Number Left)
            opt1_lst = cur_lst.copy()
            opt1_lst[2] = cur_lst[1]
            opt1_lst[1] = cur_lst[2]
            #print('')
            move = opt1_lst[2]+'R'
            #print("Move:", move)
            representation(opt1_lst)
            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)

        if found_solution == False:
        #Option 2 (Number Below)
            opt2_lst = cur_lst.copy()
            opt2_lst[2] = cur_lst[5]
            opt2_lst[5] = cur_lst[2]
            #print('')
            move = opt2_lst[2]+'U'
            #print("Move:", move)
            representation(opt2_lst)
            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
    

    #Middle Left Empty Moves
    if cur_lst[3] == "_":
            
        if found_solution == False:
        #Option 1 (Number Up)
            opt1_lst = cur_lst.copy()
            opt1_lst[3] = cur_lst[0]
            opt1_lst[0] = cur_lst[3]
            #print('')
            move = opt1_lst[3]+'D'
            #print("Move:", move)
            representation(opt1_lst)
            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)

        if found_solution == False:
        #Option 2 (Number Right)
            opt2_lst = cur_lst.copy()
            opt2_lst[3] = cur_lst[4]
            opt2_lst[4] = cur_lst[3]
            #print('')
            move = opt2_lst[3]+'L'
            #print("Move:", move)
            representation(opt2_lst)
            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                
        #Option 3 (Number Below)

        if found_solution==False:

            opt3_lst = cur_lst.copy()
            opt3_lst[3] = cur_lst[6]
            opt3_lst[6] = cur_lst[3]
            #print('')
            move = opt3_lst[3]+'U'
            #print("Move:", move)
            representation(opt3_lst)

            if opt3_lst == goal_state:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt3_lst not in states_visited:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)

    #Middle Middle Empty Moves
    if cur_lst[4] == "_":
            
        if found_solution == False:
        #Option 1 (Number Up)
            opt1_lst = cur_lst.copy()
            opt1_lst[4] = cur_lst[1]
            opt1_lst[1] = cur_lst[4]
            #print('')
            move = opt1_lst[4]+'D'
            #print("Move:",move)
            representation(opt1_lst)
            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)

        if found_solution == False:
        #Option 2 (Number Right)
            opt2_lst = cur_lst.copy()
            opt2_lst[4] = cur_lst[5]
            opt2_lst[5] = cur_lst[4]
            #print('')
            move =  opt2_lst[4]+'L'
            #print("Move:", move)
            representation(opt2_lst)
            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)

        if found_solution == False:       
        #Option 3 (Number Below)
            opt3_lst = cur_lst.copy()
            opt3_lst[4] = cur_lst[7]
            opt3_lst[7] = cur_lst[4]
            #print('')
            move = opt3_lst[4]+'U'
            #print("Move:", move)
            representation(opt3_lst)
            if opt3_lst == goal_state:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt3_lst not in states_visited:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)

        if found_solution==False:
        #Option 4 (Number Left)
            opt4_lst = cur_lst.copy()
            opt4_lst[4] = cur_lst[3]
            opt4_lst[3] = cur_lst[4]
            #print('')
            move = opt4_lst[4]+'R'
            #print("Move:", move)
            representation(opt4_lst)
            if opt4_lst == goal_state:
                state_queue += [opt4_lst]
                states_visited += [opt4_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt4_lst not in states_visited:
                state_queue += [opt4_lst]
                states_visited += [opt4_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)

    #Middle Right Empty Moves
    if cur_lst[5] == "_":
            
        if found_solution==False:
        #Option 1 (Number Up)
            opt1_lst = cur_lst.copy()
            opt1_lst[5] = cur_lst[2]
            opt1_lst[2] = cur_lst[5]
            #print('')
            move = opt1_lst[5]+'D'
            #print("Move:", move)
            representation(opt1_lst)
            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)

        if found_solution==False:
        #Option 2 (Number Left)
            opt2_lst = cur_lst.copy()
            opt2_lst[5] = cur_lst[4]
            opt2_lst[4] = cur_lst[5]
            #print('')
            move = opt2_lst[5]+'R'
            #print("Move:", move)
            representation(opt2_lst)
            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)

        if found_solution==False:        
        #Option 3 (Number Below)
            opt3_lst = cur_lst.copy()
            opt3_lst[5] = cur_lst[8]
            opt3_lst[8] = cur_lst[5]
            #print('')
            move = opt3_lst[5]+'U'
            #print("Move:", move)
            representation(opt3_lst)
            if opt3_lst == goal_state:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt3_lst not in states_visited:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)

    #Bottom Left Empty Moves
    if cur_lst[6] == "_":
            
        if found_solution==False:
        #Option 1 (Number Up)
            opt1_lst = cur_lst.copy()
            opt1_lst[6] = cur_lst[3]
            opt1_lst[3] = cur_lst[6]
            #print('')
            move = opt1_lst[6]+'D'
            #print("Move:", move)
            representation(opt1_lst)
            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)

        if found_solution==False:
        #Option 2 (Number Right)
            opt2_lst = cur_lst.copy()
            opt2_lst[6] = cur_lst[7]
            opt2_lst[7] = cur_lst[6]
            #print('')
            move = opt2_lst[6]+'L'
            #print("Move:", move)
            representation(opt2_lst)
            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                

    #Bottom Middle Empty Moves
    if cur_lst[7] == "_":
            
        if found_solution==False:
        #Option 1 (Number Up)
            opt1_lst = cur_lst.copy()
            opt1_lst[7] = cur_lst[4]
            opt1_lst[4] = cur_lst[7]
            #print('')
            move = opt1_lst[7]+'D'
            #print("Move:", move)
            representation(opt1_lst)
            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)

        if found_solution==False:
        #Option 2 (Number Right)
            opt2_lst = cur_lst.copy()
            opt2_lst[7] = cur_lst[8]
            opt2_lst[8] = cur_lst[7]
            #print('')
            move = opt2_lst[7]+'L'
            #print("Move:", move)
            representation(opt2_lst)
            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)

        if found_solution==False:
        #Option 3 (Number Left)
            opt3_lst = cur_lst.copy()
            opt3_lst[7] = cur_lst[6]
            opt3_lst[6] = cur_lst[7]
            #print('')
            move =  opt3_lst[7]+'R'
            #print("Move:", move)
            representation(opt3_lst)
            if opt3_lst == goal_state:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt3_lst not in states_visited:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                
    #Bottom Right Empty Moves
    if cur_lst[8] == "_":
            
        if found_solution==False:
        #Option 1 (Number Up)
            opt1_lst = cur_lst.copy()
            opt1_lst[8] = cur_lst[5]
            opt1_lst[5] = cur_lst[8]
            #print('')
            move = opt1_lst[8]+'D'
            #print("Move:", move)
            representation(opt1_lst)
            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)

        if found_solution==False:
        #Option 2 (Number Left)
            opt2_lst = cur_lst.copy()
            opt2_lst[8] = cur_lst[7]
            opt2_lst[7] = cur_lst[8]
            #print('')
            move = opt2_lst[8]+'R'
            #print("Move:", move)
            representation(opt2_lst)
            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("SOLUTION FOUND")
                found_solution = True
                return(found_solution)
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)

while (generate_next_states(cur_lst, state_queue, cur_action, action_queue, states_visited, found_solution)) != True:
    if cur_lst != goal_state:
        #print(found_solution)
        cur_lst = state_queue[1]
        cur_action = action_queue[1]
        del(action_queue[0])
        del(state_queue[0])
        #print("State Queue after", state_queue)
        #print("Action Queue after", action_queue)
    #print('States Visited', states_visited)

#print(action_queue[-1])
solution_BFS = ','.join(action_queue[-1])
print("The solution of Q.2")
print (solution_BFS)