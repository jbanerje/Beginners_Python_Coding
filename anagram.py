def anagram(word1 , word2):

    return_text = ""
    anagram_flag = "Y"
    count_letter = 0
    
    len_word1 = len(word1)
    len_word2 = len(word2)

    word1_list = list(word1)
    word2_list = list(word2)

    if (len_word1 != len_word2 ):
        anagram_flag = "N"
    else:
        for letter in word1_list:
            if ( letter in word2_list):
                word_index = word2_list.index(letter)
                word2_list.pop(word_index)
                count_letter = count_letter + 1
            else:
                anagram_flag = "N"
                break
            
    if ( len(word2_list) == 0 ) &  ( anagram_flag == "Y" ) :
        return_text = "Anagram"
    else:
        return_text = "Non-Anagram"
            
    return return_text ;
    
word1 = input("Word1:")
word2 = input ("Word2 :")
result = anagram(word1 , word2)
print(result)
