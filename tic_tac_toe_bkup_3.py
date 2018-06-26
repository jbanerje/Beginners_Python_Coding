#tic tac toe

#compare conning combination with player entry
def comp(list1, list2):
    #print(list1, list2)
    if  (( list1[0] == list2[0]) & ( list1[1] == list2[1]) & ( list1[2] == list2[2])):
        #print('true')
        return 'true'
    else:
        #print('false')
        return 'false'
    
#Check winning condition:

def chk_winning_cond(player_num,comb):
    win_comb_1 = [1,2,3]
    win_comb_2 = [4,5,6]
    win_comb_3 = [7,8,9]
    win_comb_4 = [1,4,7]
    win_comb_5 = [2,5,8]
    win_comb_6 = [3,6,9]
    win_comb_7 = [1,5,9]
    win_comb_8 = [3,5,7]
    
    add_pos = 0
    count_pos = 0
    game_status = 'game_on'
    track_comb = track_comb_2 = track_comb_5 = track_comb_7 = track_comb_8 =  'false'
    comb_bkp = []
    comb_bkp_1 = []
    temp_comb_1 =[]
    temp_comb_2 =[]
    temp_comb_3 =[]
    temp_comb_4 =[]
    sum_temp_comb_1 = sum_temp_comb_2 = sum_temp_comb_3 = sum_temp_comb_4 = 0
    
        
    for pos_ttt in comb:
        add_pos = add_pos + pos_ttt
        count_pos = count_pos + 1

    comb.sort() #Sorting the list

    #Condition for horizontal -> 1,2,3 - > Total 6
    if (count_pos == 3):
        if (add_pos == 6):
            track_comb = comp(comb, win_comb_1) #function call for winning combination
           
        elif (add_pos == 12):
            track_comb = comp(comb, win_comb_4) #function call for winning combination

        elif (add_pos == 18):
            track_comb = comp(comb, win_comb_6) #function call for winning combination

        elif (add_pos == 24):
            track_comb = comp(comb, win_comb_3) #function call for winning combination

        else:
            if (add_pos == 15):
                track_comb_2 = comp(comb, win_comb_2) #function call for winning combination
                track_comb_5 = comp(comb, win_comb_5) #function call for winning combination
                track_comb_7 = comp(comb, win_comb_7) #function call for winning combination
                track_comb_8 = comp(comb, win_comb_8) #function call for winning combination
            else :
                game_status = "Game_on"

        if ((track_comb == 'true') or (track_comb_2 == 'true') or (track_comb_5 == 'true') or (track_comb_7 == 'true') or (track_comb_8 == 'true')):
            game_status = "Win"
        else:
            game_status = "Game_on"
            
    elif (count_pos == 4):
            
            temp_comb_1 = comb[0:3]  #Combination 1 
            temp_comb_2 = comb[1:4]  #Combination 2

            comb_bkp.append(comb[0])
            comb_bkp.append(comb[2])
            comb_bkp.append(comb[3])

            comb_bkp_1.append(comb[0])
            comb_bkp_1.append(comb[1])
            comb_bkp_1.append(comb[3])
               
            temp_comb_3 = comb_bkp    #Combination 3
            temp_comb_4 = comb_bkp_1  #Combination 4

            #print("In Count 4-temp_comb :", comb, temp_comb_1 ,temp_comb_2, temp_comb_3, temp_comb_4)
            
            for pos_temp_comb_1 in temp_comb_1:
                sum_temp_comb_1 = sum_temp_comb_1 + pos_temp_comb_1
                
            for pos_temp_comb_2 in temp_comb_2:
                sum_temp_comb_2 = sum_temp_comb_2 + pos_temp_comb_2
                
            for pos_temp_comb_3 in temp_comb_3:
                sum_temp_comb_3 = sum_temp_comb_3 + pos_temp_comb_3
                
            for pos_temp_comb_4 in temp_comb_4:
                sum_temp_comb_4 = sum_temp_comb_4 + pos_temp_comb_4
                
            #print("sum_temp_comb :", sum_temp_comb_1, sum_temp_comb_2 ,sum_temp_comb_3, sum_temp_comb_4)
            
            if ( (sum_temp_comb_1 == 6) or (sum_temp_comb_2 == 6) or (sum_temp_comb_3 == 6) or (sum_temp_comb_4 == 6)):

                #print("sum_temp_comb == 6")
                
                track_comb_1 = comp(temp_comb_1, win_comb_1) #function call for winning combination
                track_comb_2 = comp(temp_comb_2, win_comb_1) #function call for winning combination
                track_comb_3 = comp(temp_comb_3, win_comb_1) #function call for winning combination
                track_comb_4 = comp(temp_comb_4, win_comb_1) #function call for winning combination

                if ((track_comb_1 == 'true') or (track_comb_2 == 'true') or (track_comb_3 == 'true') or (track_comb_4 == 'true')):
                    game_status = "Win"
                else:
                    game_status = "Game_on"

                #print("game_status:" , game_status)

            if ( (sum_temp_comb_1 == 12) or (sum_temp_comb_2 == 12) or (sum_temp_comb_3 == 12) or (sum_temp_comb_4 == 12)):

                #print("sum_temp_comb == 12")

                track_comb_1 = comp(temp_comb_1, win_comb_4) #function call for winning combination
                track_comb_2 = comp(temp_comb_2, win_comb_4) #function call for winning combination
                track_comb_3 = comp(temp_comb_3, win_comb_4) #function call for winning combination
                track_comb_4 = comp(temp_comb_4, win_comb_4) #function call for winning combination

                if ((track_comb_1 == 'true') or (track_comb_2 == 'true') or (track_comb_3 == 'true') or (track_comb_4 == 'true')):
                    game_status = "Win"
                else:
                    game_status = "Game_on"

                #print("game_status:" , game_status)
                    
            if ( (sum_temp_comb_1 == 18) or (sum_temp_comb_2 == 18) or (sum_temp_comb_3 == 18) or (sum_temp_comb_4 == 18)):

                #print("sum_temp_comb == 18")
                
                track_comb_1 = comp(temp_comb_1, win_comb_6) #function call for winning combination
                track_comb_2 = comp(temp_comb_2, win_comb_6) #function call for winning combination
                track_comb_3 = comp(temp_comb_3, win_comb_6) #function call for winning combination
                track_comb_4 = comp(temp_comb_4, win_comb_6) #function call for winning combination

                if ((track_comb_1 == 'true') or (track_comb_2 == 'true') or (track_comb_3 == 'true') or (track_comb_4 == 'true')):
                    game_status = "Win"
                else:
                    game_status = "Game_on"

                #print("game_status:" , game_status)
                
            if ( (sum_temp_comb_1 == 24) or (sum_temp_comb_2 == 24) or (sum_temp_comb_3 == 24) or (sum_temp_comb_4 == 24)):

                #print("sum_temp_comb == 24")
                
                track_comb_1 = comp(temp_comb_1, win_comb_3) #function call for winning combination
                track_comb_2 = comp(temp_comb_2, win_comb_3) #function call for winning combination
                track_comb_3 = comp(temp_comb_3, win_comb_3) #function call for winning combination
                track_comb_4 = comp(temp_comb_4, win_comb_3) #function call for winning combination

                if ((track_comb_1 == 'true') or (track_comb_2 == 'true') or (track_comb_3 == 'true') or (track_comb_4 == 'true')):
                    game_status = "Win"
                else:
                    game_status = "Game_on"

                #print("game_status:" , game_status)

            if ( (sum_temp_comb_1 == 15) or (sum_temp_comb_2 == 15) or (sum_temp_comb_3 == 15) or (sum_temp_comb_4 == 15)):

                #print("sum_temp_comb == 15")
                
                track_comb_1a = comp(temp_comb_1, win_comb_2) #function call for winning combination
                track_comb_1b = comp(temp_comb_1, win_comb_5) #function call for winning combination
                track_comb_1c = comp(temp_comb_1, win_comb_7) #function call for winning combination
                track_comb_1d = comp(temp_comb_1, win_comb_8) #function call for winning combination

                track_comb_2a = comp(temp_comb_2, win_comb_2) #function call for winning combination
                track_comb_2b = comp(temp_comb_2, win_comb_5) #function call for winning combination
                track_comb_2c = comp(temp_comb_2, win_comb_7) #function call for winning combination
                track_comb_2d = comp(temp_comb_2, win_comb_8) #function call for winning combination

                track_comb_3a = comp(temp_comb_3, win_comb_2) #function call for winning combination
                track_comb_3b = comp(temp_comb_3, win_comb_5) #function call for winning combination
                track_comb_3c = comp(temp_comb_3, win_comb_7) #function call for winning combination
                track_comb_3d = comp(temp_comb_3, win_comb_8) #function call for winning combination

                track_comb_4a = comp(temp_comb_4, win_comb_2) #function call for winning combination
                track_comb_4b = comp(temp_comb_4, win_comb_5) #function call for winning combination
                track_comb_4c = comp(temp_comb_4, win_comb_7) #function call for winning combination
                track_comb_4d = comp(temp_comb_4, win_comb_8) #function call for winning combination

                print ("track_comb_3c:", track_comb_3c)
                
                if ((track_comb_1a == 'true') or (track_comb_1b == 'true') or (track_comb_1c == 'true') or (track_comb_1d == 'true')):
                    game_status = "Win"

                if ((track_comb_2a == 'true') or (track_comb_2b == 'true') or (track_comb_2c == 'true') or (track_comb_2d == 'true')):
                    game_status = "Win"

                if ((track_comb_3a == 'true') or (track_comb_3b == 'true') or (track_comb_3c == 'true') or (track_comb_3d == 'true')):
                    game_status = "Win"

                if ((track_comb_4a == 'true') or (track_comb_4b == 'true') or (track_comb_4c == 'true') or (track_comb_4d == 'true')):
                    game_status = "Win"


                #print("game_status:" , game_status)
                   
    else:
        game_status = "Game_on"
        
    return(game_status) # returns value to player_pos(player_num,player_pos)

# This fucntion will do sanity check of the position

def player_pos_chk(player_pos):
    
    if (player_pos <= 3):
        if ((row1_player[player_pos - 1] == 'P1') or (row1_player[player_pos - 1] == 'P2')):
            chk_flag = 'fail'
        else:
            chk_flag = 'pass'
            
    elif ((player_pos > 3) & (player_pos <= 6)):
        if ((row2_player[player_pos - 4] == 'P1') or (row2_player[player_pos - 4] == 'P2')):
            chk_flag = 'fail'
        else:
            chk_flag = 'pass'
         
    else:
        #print("In range 7 to 9",row3_number[player_pos - 7])
        if ((row3_player[player_pos - 7] == 'P1') or (row3_player[player_pos - 7] == 'P2')):
            chk_flag = 'fail'
        else:
            chk_flag = 'pass'

    return chk_flag; #Return pass/fail to main . chk_result = player_pos_chk(player_1_pos)

# This function will place the player's turn in the corresponding cell
def player_pos(player_num,player_pos) :

    
    if (player_pos <= 3):
        
        row1_player[player_pos - 1] = player_num
        if (player_num == 'P1'):
            comb_P1.append(player_pos)
        else:
            comb_P2.append(player_pos)
        
    
    elif ((player_pos > 3) & (player_pos <= 6)):
        
        row2_player[player_pos - 4] = player_num
        if (player_num == 'P1'):
            comb_P1.append(player_pos)
        else:
            comb_P2.append(player_pos)
            
    else:
        
        row3_player[player_pos - 7] = player_num
        if (player_num == 'P1'):
            comb_P1.append(player_pos)
        else:
            comb_P2.append(player_pos)
            
    if (player_num =='P1'):
        player_1_flag = 'y'
    else:
        player_1_flag = 'n'

    if (player_num == 'P1'):     
        win_flag = chk_winning_cond(player_num,comb_P1) # Function Check winning condition: returns "Win" or "Game On"
    else:
        win_flag = chk_winning_cond(player_num,comb_P2) # Function Check winning condition: returns "Win" or "Game On"
 
    print("",row1_player,"\n",row2_player,"\n",row3_player)
    
    return(win_flag);

#*************Main Starts Here *************************************#
comb_P1=[]
comb_P2=[]

row1_player=['1','2','3']
row2_player=['4','5','6']
row3_player=['7','8','9']

play_count=1
chk_result = 'pass'
player_1_flag = 'n'
player_2_flag = 'n'


# This is the basic gaming structure
print("***-----------Tic Tac Toe table---------------------------***")
print(" [1,2,3]\n","[4,5,6]\n","[7,8,9]")
print("***-------------------End---------------------------------***")

#Total 9 opportunities will be present for 2 players
while (play_count <= 9):
    #print("play_count:",play_count)

    player_1_pos = int(input("Player_1: Enter your position:")) 
    chk_result = player_pos_chk(player_1_pos) # This fucntion will do sanity check of the position
    #print("chk_result:",chk_result)
        
    if (chk_result == 'pass') :
        win_flag = player_pos('P1',player_1_pos) # This function will place the player's turn in the corresponding cell
        
        if (win_flag == 'Win'):
            print("P1 Wins!!")
            print('Player_1:',comb_P1)
            print('Player_2:',comb_P2)
            break
        play_count = play_count + 1
    else:
        print('Position Already Accupied!')
  
    if (play_count <= 9):
        #print("play_count:",play_count)
        player_2_pos = int(input("Player_2: Enter your position:"))
        chk_result = player_pos_chk(player_2_pos) # This fucntion will do sanity check of the position

        #print("chk_result:",chk_result)

        if (chk_result == 'pass') :
            win_flag = player_pos('P2',player_2_pos) # This function will place the player's turn in the corresponding cell
            if (win_flag == 'Win'):
                print("P2 Wins!!")
                print('Player_1:',comb_P1)
                print('Player_2:',comb_P2)
                break
            play_count = play_count + 1
        else:
            print('Position Already Occupied!') 
    else:
        print('Game Ends!')
        print('Player_1:',comb_P1)
        print('Player_2:',comb_P2)







    
