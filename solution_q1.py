#Geez I haven't had to code in ages

import math

goal_state = ['_','1','2','3','4','5','6','7','8']
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

def dfs(cur_lst, state_queue, cur_action, action_queue, states_visited, found_solution):
    while (generate_next_states(cur_lst, state_queue, cur_action, action_queue, states_visited, found_solution)) != True:
    #print(found_solution)

    #print(cur_action)
        state_queue.remove(cur_lst)
        action_queue.remove(cur_action)
        cur_lst = state_queue[-1]
        cur_action = action_queue[-1]
        if len(states_visited) > 382000:
            print("No sol")
            break
        #print(cur_lst)
        #print("State Queue after", state_queue)
        #print("Action Queue after", action_queue)
        #print('States Visited', states_visited)

        #print(action_queue[-1])
    solution_BFS = ','.join(action_queue[-1])
    print("The solution of Q.1")
    print (solution_BFS)
    print(state_queue[-1])


    with open('solution.txt', 'w') as f:
        f.write(solution_BFS)
        print("Solution has been written to solution.txt")
        print(solution_BFS)



def bfs(cur_lst, state_queue, cur_action, action_queue, states_visited, found_solution):
    while (generate_next_states(cur_lst, state_queue, cur_action, action_queue, states_visited, found_solution)) != True:
        #print(found_solution)
        state_queue.remove(cur_lst)
        action_queue.remove(cur_action)
        cur_lst = state_queue[0]
        cur_action = action_queue[0]
        #print("State Queue after", state_queue)
        #print("Action Queue after", action_queue)
        #print('States Visited', states_visited)
        #print('BFS')

    #print(action_queue[-1])
    solution_BFS = ','.join(action_queue[-1])
    print("The solution of Q.2")
    print (solution_BFS)



dfs(cur_lst, state_queue, cur_action, action_queue, states_visited, found_solution)

goal_state = ['_','1','2','3','4','5','6','7','8']
found_solution = False

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

bfs(cur_lst, state_queue, cur_action, action_queue, states_visited, found_solution)

import math

goal_state = ['_','1','2','3','4','5','6','7','8']
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


def ucs_cost(lst, goal_state):
    #Since all moves = 1, the cost regardless of current state to the next move = 1
    cost = 1
    return cost


def A_star_man_cost(lst, goal_state):
    cost = 0

    element = lst[0]
    if lst[0]!='_':
        if goal_state[1] == element or goal_state[3] == element:
            cost +=1
        if goal_state[2] == element or goal_state[4] == element or goal_state[6] == element:
            cost+=2
        if goal_state[7] == element or goal_state[5]== element:
            cost+=3
        if goal_state[8] == element:
            cost+=4

    element = lst[1]
    if lst[1]!='_':
        if goal_state[6] == element or goal_state[8]== element:
            cost +=3
        if goal_state[2] == element or goal_state[4] == element or goal_state[0] == element:
            cost+=1
        if goal_state[7] == element or goal_state[5] == element or goal_state[3]== element:
            cost+=2

    element = lst[2]
    if lst[2]!='_':
        if goal_state[1] == element or goal_state[5]==element:
            cost +=1
        if goal_state[0] == element or goal_state[4] == element or goal_state[8] == element:
            cost+=2
        if goal_state[7] == element or goal_state[3] == element:
            cost+=3
        if goal_state[6] == element:
            cost+=4

    element = lst[3]
    if lst[3]!='_':
        if goal_state[2] == element or goal_state[8]== element:
            cost +=3
        if goal_state[0] == element or goal_state[4] == element or goal_state[6] == element:
            cost+=1
        if goal_state[7] == element or goal_state[5] == element or goal_state[1]== element:
            cost+=2
    
    element = lst[4]
    if lst[4]!='_':
        if goal_state[0] == element or goal_state[2] == element or goal_state[6] == element or goal_state[8] == element:
            cost+=2
        if goal_state[7] == element or goal_state[5] == element or goal_state[1] == element or goal_state[3] == element:
            cost+=1

    element = lst[5]
    if lst[5]!='_':
        if goal_state[0] == element or goal_state[6]== element:
            cost +=3
        if goal_state[2] == element or goal_state[4] == element or goal_state[8] == element:
            cost+=1
        if goal_state[7] == element or goal_state[3] == element or goal_state[1]== element:
            cost+=2

    element = lst[6]
    if lst[6]!='_':
        if goal_state[3] == element or goal_state[7]==element:
            cost +=1
        if goal_state[0] == element or goal_state[4] == element or goal_state[8] == element:
            cost+=2
        if goal_state[5] == element or goal_state[1]== element:
            cost+=3
        if goal_state[2]== element:
            cost+=4

    element = lst[7]
    if lst[7]!='_':
        if goal_state[0] == element or goal_state[2] == element:
            cost +=3
        if goal_state[6] == element or goal_state[4] == element or goal_state[8] == element:
            cost+=1
        if goal_state[5] == element or goal_state[3] == element or goal_state[1]== element:
            cost+=2

    element = lst[8]
    if lst[8]!='_':
        if goal_state[5] == element or goal_state[7]==element:
            cost +=1
        if goal_state[2] == element or goal_state[4] == element or goal_state[6] == element:
            cost+=2
        if goal_state[3] == element or goal_state[1] == element:
            cost+=3
        if goal_state[0]== element:
            cost+=4

    return (cost)
    

        

def A_star_straight_cost(lst, goal_state):
    cost = 0

    element = lst[0]
    if lst[0]!='_':
        if goal_state[1] == element or goal_state[3]==element:
            cost +=1
        if goal_state[2] == element or goal_state[6] == element:
            cost+=2
        if goal_state[4]== element:
            cost+=math.sqrt(2)
        if goal_state[7] == element or goal_state[5]== element:
            cost+=math.sqrt(5)
        if goal_state[8]== element:
            cost+=math.sqrt(8)

    element = lst[1]
    if lst[1]!='_':
        if goal_state[6] == element or goal_state[8]== element:
            cost +math.sqrt(5)
        if goal_state[2] == element or goal_state[4] == element or goal_state[0] == element:
            cost+=1
        if goal_state[5] == element or goal_state[3]== element:
            cost+=math.sqrt(2)
        if goal_state[7] == element:
            cost+=2

    element = lst[2]
    if lst[2]!='_':
        if goal_state[1] == element or goal_state[5]==element:
            cost +=1
        if goal_state[0] == element or goal_state[8] == element:
            cost+=2
        if goal_state[4]== element:
            cost+=math.sqrt(2)
        if goal_state[7] == element or goal_state[3]== element:
            cost+=math.sqrt(5)
        if goal_state[6] == element:
            cost+=math.sqrt(8)

    element = lst[3]
    if lst[3]!='_':
        if goal_state[2] == element or goal_state[8]== element:
            cost +math.sqrt(5)
        if goal_state[6] == element or goal_state[4] == element or goal_state[0] == element:
            cost+=1
        if goal_state[1] == element or goal_state[7]== element:
            cost+=math.sqrt(2)
        if goal_state[5] == element:
            cost+=2
    
    element = lst[4]
    if lst[4]!='_':
        if goal_state[0] == element or goal_state[2] == element or goal_state[8] == element or goal_state[6] == element:
            cost+=math.sqrt(2)
        if goal_state[7] == element or goal_state[5] == element or goal_state[1] == element or goal_state[3] == element:
            cost+=1

    element = lst[5]
    if lst[5]!='_':
        if goal_state[6] == element or goal_state[0]== element:
            cost +math.sqrt(5)
        if goal_state[2] == element or goal_state[4] == element or goal_state[8] == element:
            cost+=1
        if goal_state[1] == element or goal_state[7]== element:
            cost+=math.sqrt(2)
        if goal_state[3] == element:
            cost+=2

    element = lst[6]
    if lst[6]!='_':
        if goal_state[3] == element or goal_state[7]==element:
            cost +=1
        if goal_state[0] == element or goal_state[8] == element:
            cost+=2
        if goal_state[4] == element:
            cost+=math.sqrt(2)
        if goal_state[1] == element or goal_state[5]== element:
            cost+=math.sqrt(5)
        if goal_state[2] == element:
            cost+=math.sqrt(8)

    element = lst[7]
    if lst[7]!='_':
        if goal_state[0] == element or goal_state[2]== element:
            cost +math.sqrt(5)
        if goal_state[6] == element or goal_state[4] == element or goal_state[8] == element:
            cost+=1
        if goal_state[3] == element or goal_state[5]== element:
            cost+=math.sqrt(2)
        if goal_state[1] == element :
            cost+=2

    element = lst[8]
    if lst[8]!='_':
        if goal_state[5] == element or goal_state[7]==element:
            cost +=1
        if goal_state[6] == element or goal_state[2] == element:
            cost+=2
        if goal_state[4]== element:
            cost+=math.sqrt(2)
        if goal_state[1] == element or goal_state[3] == element:
            cost+=math.sqrt(5)
        if goal_state[0] == element:
            cost+=math.sqrt(8)

    return (cost)

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


def generate_next_states2(cur_lst, state_queue, cur_action, action_queue, cur_cost, cost_queue, states_visited):
    #Top Left Empty Moves
     
    if cur_lst[0] == "_":
        
        
        #Option 1 (Number Right)
            opt1_lst = cur_lst.copy()
            opt1_lst[0] = cur_lst[1]
            opt1_lst[1] = cur_lst[0]
            #print('')
            move = opt1_lst[0]+'L'
            #print("Move:", move) 
            representation(opt1_lst)
            ucs_cost_val = ucs_cost(opt1_lst,goal_state)
            A_star_man_cost_val = A_star_man_cost(opt1_lst, goal_state)
            A_star_straight_cost_val = A_star_straight_cost(opt1_lst,goal_state)

            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
                
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)

        
        #Option 2 (Number Below)
            opt2_lst = cur_lst.copy()
            opt2_lst[0] = cur_lst[3]
            opt2_lst[3] = cur_lst[0]
            #print('')
            move = opt2_lst[0]+'U'
            #print("Move:", move)
            representation(opt2_lst)
            ucs_cost_val = ucs_cost(opt2_lst,goal_state)
            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
        



    #Top Middle Empty Moves
    if cur_lst[1] == "_":

          
        #Option 1 (Number Left)
            opt1_lst = cur_lst.copy()
            opt1_lst[1] = cur_lst[0]
            opt1_lst[0] = cur_lst[1]
            #print('')
            move = opt1_lst[1]+'R'
            #print("Move:", move)
            representation(opt1_lst)
            ucs_cost_val = ucs_cost(opt1_lst,goal_state)

            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
        
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)

        #Option 2 (Number Right)
          
            opt2_lst = cur_lst.copy()
            opt2_lst[1] = cur_lst[2]
            opt2_lst[2] = cur_lst[1]
            #print('')
            move = opt2_lst[1]+'L'
            #print("Move:", move)
            representation(opt2_lst)
            ucs_cost_val = ucs_cost(opt2_lst,goal_state)

            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
                
        #Option 3 (Number Below)
          
            opt3_lst = cur_lst.copy()
            opt3_lst[1] = cur_lst[4]
            opt3_lst[4] = cur_lst[1]
            #print('')
            move = opt3_lst[1]+'U'
            #print("Move:", move)
            representation(opt3_lst)
            ucs_cost_val = ucs_cost(opt3_lst,goal_state)

            if opt3_lst == goal_state:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            

            if opt3_lst not in states_visited:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
                
                
    #Top Right Empty Moves
    if cur_lst[2] == "_":
        
        
        #Option 1 (Number Left)
            opt1_lst = cur_lst.copy()
            opt1_lst[2] = cur_lst[1]
            opt1_lst[1] = cur_lst[2]
            #print('')
            move = opt1_lst[2]+'R'
            #print("Move:", move)
            representation(opt1_lst)
            ucs_cost_val = ucs_cost(opt1_lst,goal_state)

            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)

        
        #Option 2 (Number Below)
            opt2_lst = cur_lst.copy()
            opt2_lst[2] = cur_lst[5]
            opt2_lst[5] = cur_lst[2]
            #print('')
            move = opt2_lst[2]+'U'
            #print("Move:", move)
            representation(opt2_lst)
            ucs_cost_val = ucs_cost(opt2_lst,goal_state)

            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
    

    #Middle Left Empty Moves
    if cur_lst[3] == "_":
            
        
        #Option 1 (Number Up)
            opt1_lst = cur_lst.copy()
            opt1_lst[3] = cur_lst[0]
            opt1_lst[0] = cur_lst[3]
            #print('')
            move = opt1_lst[3]+'D'
            #print("Move:", move)
            representation(opt1_lst)
            ucs_cost_val = ucs_cost(opt1_lst,goal_state)

            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)

        
        #Option 2 (Number Right)
            opt2_lst = cur_lst.copy()
            opt2_lst[3] = cur_lst[4]
            opt2_lst[4] = cur_lst[3]
            #print('')
            move = opt2_lst[3]+'L'
            #print("Move:", move)
            representation(opt2_lst)
            ucs_cost_val = ucs_cost(opt2_lst,goal_state)

            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
                
        #Option 3 (Number Below)

            opt3_lst = cur_lst.copy()
            opt3_lst[3] = cur_lst[6]
            opt3_lst[6] = cur_lst[3]
            #print('')
            move = opt3_lst[3]+'U'
            #print("Move:", move)
            representation(opt3_lst)
            ucs_cost_val = ucs_cost(opt3_lst,goal_state)

            if opt3_lst == goal_state:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt3_lst not in states_visited:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)

    #Middle Middle Empty Moves
    if cur_lst[4] == "_":
            
        
        #Option 1 (Number Up)
            opt1_lst = cur_lst.copy()
            opt1_lst[4] = cur_lst[1]
            opt1_lst[1] = cur_lst[4]
            #print('')
            move = opt1_lst[4]+'D'
            #print("Move:",move)
            representation(opt1_lst)
            ucs_cost_val = ucs_cost(opt1_lst,goal_state)

            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)

        
        #Option 2 (Number Right)
            opt2_lst = cur_lst.copy()
            opt2_lst[4] = cur_lst[5]
            opt2_lst[5] = cur_lst[4]
            #print('')
            move =  opt2_lst[4]+'L'
            #print("Move:", move)
            representation(opt2_lst)
            ucs_cost_val = ucs_cost(opt2_lst,goal_state)

            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)

               
        #Option 3 (Number Below)
            opt3_lst = cur_lst.copy()
            opt3_lst[4] = cur_lst[7]
            opt3_lst[7] = cur_lst[4]
            #print('')
            move = opt3_lst[4]+'U'
            #print("Move:", move)
            representation(opt3_lst)
            ucs_cost_val = ucs_cost(opt3_lst,goal_state)

            if opt3_lst == goal_state:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt3_lst not in states_visited:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)

        
        #Option 4 (Number Left)
            opt4_lst = cur_lst.copy()
            opt4_lst[4] = cur_lst[3]
            opt4_lst[3] = cur_lst[4]
            #print('')
            move = opt4_lst[4]+'R'
            #print("Move:", move)
            representation(opt4_lst)
            ucs_cost_val = ucs_cost(opt4_lst,goal_state)

            if opt4_lst == goal_state:
                state_queue += [opt4_lst]
                states_visited += [opt4_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt4_lst not in states_visited:
                state_queue += [opt4_lst]
                states_visited += [opt4_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)

    #Middle Right Empty Moves
    if cur_lst[5] == "_":
            
        
        #Option 1 (Number Up)
            opt1_lst = cur_lst.copy()
            opt1_lst[5] = cur_lst[2]
            opt1_lst[2] = cur_lst[5]
            #print('')
            move = opt1_lst[5]+'D'
            #print("Move:", move)
            representation(opt1_lst)
            ucs_cost_val = ucs_cost(opt1_lst,goal_state)

            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)

        
        #Option 2 (Number Left)
            opt2_lst = cur_lst.copy()
            opt2_lst[5] = cur_lst[4]
            opt2_lst[4] = cur_lst[5]
            #print('')
            move = opt2_lst[5]+'R'
            #print("Move:", move)
            representation(opt2_lst)
            ucs_cost_val = ucs_cost(opt2_lst,goal_state)

            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)

                
        #Option 3 (Number Below)
            opt3_lst = cur_lst.copy()
            opt3_lst[5] = cur_lst[8]
            opt3_lst[8] = cur_lst[5]
            #print('')
            move = opt3_lst[5]+'U'
            #print("Move:", move)
            representation(opt3_lst)
            ucs_cost_val = ucs_cost(opt3_lst,goal_state)

            if opt3_lst == goal_state:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt3_lst not in states_visited:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)

    #Bottom Left Empty Moves
    if cur_lst[6] == "_":
            
        
        #Option 1 (Number Up)
            opt1_lst = cur_lst.copy()
            opt1_lst[6] = cur_lst[3]
            opt1_lst[3] = cur_lst[6]
            #print('')
            move = opt1_lst[6]+'D'
            #print("Move:", move)
            representation(opt1_lst)
            ucs_cost_val = ucs_cost(opt1_lst,goal_state)

            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)

        
        #Option 2 (Number Right)
            opt2_lst = cur_lst.copy()
            opt2_lst[6] = cur_lst[7]
            opt2_lst[7] = cur_lst[6]
            #print('')
            move = opt2_lst[6]+'L'
            #print("Move:", move)
            representation(opt2_lst)
            ucs_cost_val = ucs_cost(opt2_lst,goal_state)

            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
                

    #Bottom Middle Empty Moves
    if cur_lst[7] == "_":
            
        
        #Option 1 (Number Up)
            opt1_lst = cur_lst.copy()
            opt1_lst[7] = cur_lst[4]
            opt1_lst[4] = cur_lst[7]
            #print('')
            move = opt1_lst[7]+'D'
            #print("Move:", move)
            representation(opt1_lst)
            ucs_cost_val = ucs_cost(opt1_lst,goal_state)

            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)

        
        #Option 2 (Number Right)
            opt2_lst = cur_lst.copy()
            opt2_lst[7] = cur_lst[8]
            opt2_lst[8] = cur_lst[7]
            #print('')
            move = opt2_lst[7]+'L'
            #print("Move:", move)
            representation(opt2_lst)
            ucs_cost_val = ucs_cost(opt2_lst,goal_state)

            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)

        
        #Option 3 (Number Left)
            opt3_lst = cur_lst.copy()
            opt3_lst[7] = cur_lst[6]
            opt3_lst[6] = cur_lst[7]
            #print('')
            move =  opt3_lst[7]+'R'
            #print("Move:", move)
            representation(opt3_lst)
            ucs_cost_val = ucs_cost(opt3_lst,goal_state)

            if opt3_lst == goal_state:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt3_lst not in states_visited:
                state_queue += [opt3_lst]
                states_visited += [opt3_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
                
    #Bottom Right Empty Moves
    if cur_lst[8] == "_":
            
        
        #Option 1 (Number Up)
            opt1_lst = cur_lst.copy()
            opt1_lst[8] = cur_lst[5]
            opt1_lst[5] = cur_lst[8]
            #print('')
            move = opt1_lst[8]+'D'
            #print("Move:", move)
            representation(opt1_lst)
            ucs_cost_val = ucs_cost(opt1_lst,goal_state)

            if opt1_lst == goal_state:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
            
            if opt1_lst not in states_visited:
                state_queue += [opt1_lst]
                states_visited += [opt1_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)

        
        #Option 2 (Number Left)
            opt2_lst = cur_lst.copy()
            opt2_lst[8] = cur_lst[7]
            opt2_lst[7] = cur_lst[8]
            #print('')
            move = opt2_lst[8]+'R'
            #print("Move:", move)
            representation(opt2_lst)
            ucs_cost_val = ucs_cost(opt2_lst,goal_state)

            if opt2_lst == goal_state:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)
                
            
            if opt2_lst not in states_visited:
                state_queue += [opt2_lst]
                states_visited += [opt2_lst]
                #print("current action", cur_action)
                new_action = cur_action + [move]
                #print("New action", new_action)
                action_queue += [new_action]
                #print (action_queue)
                #print("current cost", cur_cost)
                new_cost = cur_cost + ucs_cost_val
                #print("New cost", new_cost)
                cost_queue += [new_cost]
                #print(cost_queue)

goal_state = ['_','1','2','3','4','5','6','7','8']
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
cur_cost = 0

state_queue = []
state_queue += [cur_lst]

action_queue = [[]]
action_queue += cur_action

cost_queue = []
cost_queue += [cur_cost]

states_visited = []
states_visited += [cur_lst]

#print("Starting Puzzle")
representation(cur_lst)     


def ucs(cur_lst, state_queue, cur_action, action_queue, cur_cost, cost_queue, states_visited):

    while len(state_queue) > 0:  

        if cur_lst == goal_state:
            solution_UCS = ','.join(cur_action)
            print("The solution of Q.3")
            print(solution_UCS)
            return
            
   
        generate_next_states2(cur_lst, state_queue, cur_action, action_queue, cur_cost, cost_queue, states_visited)
        #print(cost_queue)

        state_queue.remove(cur_lst)
        action_queue.remove(cur_action)
        cost_queue.remove(cur_cost)

        minimum = cost_queue[0]
        min_index = 0
        for i in range(1, len(cost_queue)):
            if cost_queue[i] < minimum:
                minimum = cost_queue[i]
                min_index = i
   
        cur_lst = state_queue[min_index]
        cur_action = action_queue[min_index]
        cur_cost = cost_queue[min_index] 


ucs(cur_lst, state_queue, cur_action, action_queue, cur_cost, cost_queue, states_visited)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

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

def a_star_manhattan(cur_lst, state_queue, cur_action, action_queue, cur_cost, cost_queue, states_visited):
    while len(state_queue) > 0:  
        if cur_lst == goal_state:
            solution_astar_manhattan = ','.join(cur_action)
            print("The solution of Q.4")
            print(solution_astar_manhattan)
            return
            
        generate_next_states2(cur_lst, state_queue, cur_action, action_queue, cur_cost, cost_queue, states_visited)

        state_queue.remove(cur_lst)
        action_queue.remove(cur_action)

        #f(n) = g(n) + h(n): Expected Cost from State
        #g(n): Path Cost
        # h(n): Manhattan distance heuristic
        minimum = float('inf')
        min_index = 0
        for i in range(len(state_queue)):

            #Since each action taken before costs 1, number of actions taken before = g
            g_n = len(action_queue[i])

            h_n = A_star_man_cost(state_queue[i], goal_state)  
            #print(h_n)
            f_n = g_n + h_n
            if f_n < minimum:
                minimum = f_n
                min_index = i
   
        cur_lst = state_queue[min_index]
        cur_action = action_queue[min_index]
   
        cur_lst = state_queue[min_index]
        cur_action = action_queue[min_index]

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

def a_star_straight_line(cur_lst, state_queue, cur_action, action_queue, cur_cost, cost_queue, states_visited):
    while len(state_queue) > 0:  
        if cur_lst == goal_state:
            solution_astar_straight = ','.join(cur_action)
            print("The solution of Q.5")
            print(solution_astar_straight)
            return
            
        generate_next_states2(cur_lst, state_queue, cur_action, action_queue, cur_cost, cost_queue, states_visited)

        state_queue.remove(cur_lst)
        action_queue.remove(cur_action)

        #f(n) = g(n) + h(n): Expected Cost from State
        #g(n): Path Cost
        # h(n): Straight line distance heuristic
        minimum = float('inf')
        min_index = 0

        for i in range(len(state_queue)):
            #Since each action taken before costs 1, number of actions taken before = f
            g_n = len(action_queue[i])
            h_n = A_star_straight_cost(state_queue[i], goal_state)  
            #print(h_n)
            f_n = g_n + h_n
            if f_n < minimum:
                minimum = f_n
                min_index = i
   
        cur_lst = state_queue[min_index]
        cur_action = action_queue[min_index]


goal_state = ['_','1','2','3','4','5','6','7','8']
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

a_star_manhattan(cur_lst, state_queue, cur_action, action_queue, cur_cost, cost_queue, states_visited)


goal_state = ['_','1','2','3','4','5','6','7','8']
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

a_star_straight_line(cur_lst, state_queue, cur_action, action_queue, cur_cost, cost_queue, states_visited)