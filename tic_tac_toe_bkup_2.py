#tic tac toe

#Compare List 3.
def comp_list_3(list1, list2):
    if  (( list1[0]== list2[0]) & ( list1[1]== list2[1]) & ( list1[2]== list2[2])):
        return 'true'
    else:
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
        
    for pos_ttt in comb:
        add_pos = add_pos + pos_ttt
        count_pos = count_pos + 1

    comb.sort() #Sorting the list

    #Condition for horizontal -> 1,2,3 - > Total 6
    if (count_pos == 3):
        if (add_pos == 6):
            comp_3_result = comp_list_3(comb, win_comb_1)
            if ( comp_3_result = 'true'):
                game_status = "Win"
                print('win_comb_1')
            else:
                game_status = "Game_on"
        elif (add_pos == 24):
            comp_3_result = comp_list_3(comb, win_comb_3)
            if ( set(comb) & set(win_comb_3)):
                game_status = "Win"
                print('win_comb_3')
            else:
                game_status = "Game_on"
        elif (add_pos == 12):
            if ( set(comb) & set(win_comb_4)):
                game_status = "Win"
                print('win_comb_4')
            else:
                game_status = "Game_on"
        elif (add_pos == 18):
            if ( set(comb) & set(win_comb_6)):
                print(comb)
                game_status = "Win"
                print('win_comb_6')
            else:
                game_status = "Game_on"
        else:
            if (add_pos == 15):
                if ( set(comb) & set(win_comb_2)):
                    game_status = "Win"
                    print('win_comb_2')  
                elif ( set(comb) & set(win_comb_5)):
                    game_status = "Win"
                    print('win_comb_5')
                elif ( set(comb) & set(win_comb_7)):
                    game_status = "Win"
                    print('win_comb_7')
                elif ( set(comb) & set(win_comb_8)):
                    game_status = "Win"
                    print('win_comb_8')
                else:
                    game_status = "Game_on"
                    print('No Combination 1')
    else:
        game_status = "Game_on"
        print('No Combination 2')
    return(game_status)

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

    return chk_flag;

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
        win_flag = chk_winning_cond(player_num,comb_P1)
    else:
        win_flag = chk_winning_cond(player_num,comb_P2)
 
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
    chk_result = player_pos_chk(player_1_pos)
    #print("chk_result:",chk_result)
        
    if (chk_result == 'pass') :
        win_flag = player_pos('P1',player_1_pos)
        
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
        chk_result = player_pos_chk(player_2_pos)

        #print("chk_result:",chk_result)

        if (chk_result == 'pass') :
            win_flag = player_pos('P2',player_2_pos)
            if (win_flag == 'Win'):
                print("P2 Wins!!")
                print('Player_1:',comb_P1)
                print('Player_2:',comb_P2)
                break
            play_count = play_count + 1
        else:
            print('Position Already Accupied!') 
    else:
        print('Game Ends!')
        print('Player_1:',comb_P1)
        print('Player_2:',comb_P2)







    
