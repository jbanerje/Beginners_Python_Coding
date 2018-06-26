#----------------------------------------------#
# Author    :   Jagannath Banerjee
# Date      :   12/10/2017
# Content   :   Parsing the log file for tls
#----------------------------------------------#

# Variable Initialization

print("Hi Logan! , Python is working for you! :)")

list_ip_data=[]
list_search_conn=[]
pos=0
ssl_v2=ssl_v3 = tls_1_0 = tls_1_1 = tls_1_2 = "N"
#print("IP","~","PORT","~","SSL_V2","~","SSL_V3","~","TLS_1.0","~","TLS_1.1","~","TLS_1.2")
output_file_header = "S_No."+"~"+"IP"+"~"+"PORT"+"~"+"SSL_V2"+"~"+"SSL_V3"+"~"+"TLS_1.0"+"~"+"TLS_1.1"+"~"+"TLS_1.2"
write_count=1

#File Operation  
input_file = open("dave_ext.txt", "r")
output_file = open("tls_data_from_log.txt", "w")
output_file.write(output_file_header)

str_file = input_file.read()

#Split the file by ":"

data_list=str_file.split(":")

#Finding the starting point of the log - "Connection"
for srch_str in range(len(data_list)):
    if (data_list[srch_str].find("Connection")>=0):
        list_search_conn.append(srch_str)

# This will enable file to be read from last connection to end of file.  
list_search_conn.append(len(data_list))

#print(list_search_conn)

#Main Parsing
for pos in range(len(list_search_conn)-1):
    pos_start = list_search_conn[pos]
    pos_end = list_search_conn[pos+1]

    #print(pos_start,";",pos_end)

    for srch_str in range(pos_start,pos_end):

        if (data_list[srch_str].find("Connection")>=0):
            ip= data_list[srch_str + 2].split("\n") #ip & connection
            sec_1 = data_list[srch_str + 3].split("\n") #ip & connection

        for sec_layer in range(srch_str, pos_end):

            if (data_list[srch_str].find("SSLv2 ClientHello")>=0):
                ssl_v2_split = data_list[srch_str+1].split("\n")
                if (ssl_v2_split[0]==' yes'):
                    ssl_v2="Y"
            
            if (data_list[srch_str].find("  SSLv3")>=0):
                ssl_v3="Y"
            
            if (data_list[srch_str].find("TLSv1.0")>=0):
                tls_1_0="Y"
            
            if (data_list[srch_str].find("TLSv1.1")>=0):
                tls_1_1="Y"
            
            if (data_list[srch_str].find("TLSv1.2")>=0):
                tls_1_2="Y"

    
    #print(sec_1[0],"~",ip[0],"~",ssl_v2[0],"~",ssl_v3,"~",tls_1_0,"~",tls_1_1,"~",tls_1_2)
    tls_ip = str(sec_1[0]).lstrip(' ')
    tls_port = str(ip[0])
    ssl_v2_enb = str(ssl_v2[0])

    output_rec= str(write_count) + "~" + tls_ip + "~"+ tls_port + "~"+ssl_v2_enb +"~"+ssl_v3+"~"+tls_1_0+"~"+tls_1_1+"~"+tls_1_2
    #print(output_rec)
    output_file.write("\n")
    output_file.write(output_rec)
    write_count+=1
    
    ssl_v2=ssl_v3 = tls_1_0 = tls_1_1 = tls_1_2 = "N"    

print("*************** Statistics *****************")
print("Record Written -",write_count )
print("************ End of Program ****************")


# Close open file
input_file.close()
output_file.close()
