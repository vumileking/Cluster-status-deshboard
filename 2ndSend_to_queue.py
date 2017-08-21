#!/home/vumile/python2.7/bin/python
from __future__ import division
import subprocess
import boto3
from subprocess import call 
#pbsnodes command, allowing us to get data
node_info=subprocess.Popen("pbsnodes", stdout=subprocess.PIPE)
recieve_node_info=node_info.stdout.read()
counter=0
array_node_no=" "
array_state=" "
status=" "
w, h =27,3
#array for 2D list
Matrix=[[0 for x in range(w)] for y in range(h)]
No_of_proc=0
processes=" "
process_number=0
Jobs=" "
totalmem=" "
availiblemem=" "
physicalmem=" "
state_type=" "
state_color=" "
node_number2=" "
node_number=" "
Matrix3=[]
#opens file that will store the results
out_put_file= open('Output2.html','w')
#since this is the second table in our html grid file the below syntex is in html format
Matrix[0][0]="<div=\"suball2\"><br/><center><h3>cream</h3></center><table style=\"width:50%\" align=\"center\" border=\"1px\"><tr><th>Node No</th>"
Matrix[1][0]="</tr><tr><th>State</th>"
Matrix[2][0]="</tr><tr><th>Load</th>"
counter2=0
take_frm_counter=0
first_index=0
#Checking memory size of the core
node_info=subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
recieve_dfh_info=node_info.stdout.read()
l=0
b=0
dataD_used=0.0
#seaching df -h line by line
for n in range(0, len(recieve_dfh_info)):
  if recieve_dfh_info[n]=='n' and recieve_dfh_info[n+1]=='/' and recieve_dfh_info[n+2]=='d' and recieve_dfh_info[n+3]=='a' and recieve_dfh_info[n+4]=='t' and recieve_dfh_info[n+5]=='a' and recieve_dfh_info[n+6]=='D':
    dataD_used=recieve_dfh_info[n+20:n+23]
    dataD_avil=recieve_dfh_info[n+32:n+35]
    print dataD_used
    print dataD_avil
    percentD=(float(dataD_used)/(float(dataD_avil)+float(dataD_used)))*100
#Collecting Data C and spaces 
  if recieve_dfh_info[n]=='n' and recieve_dfh_info[n+1]=='/' and recieve_dfh_info[n+2]=='d' and recieve_dfh_info[n+3]=='a' and recieve_dfh_info[n+4]=='t' and recieve_dfh_info[n+5]=='a' and recieve_dfh_info[n+6]=='C':
    dataC_used=recieve_dfh_info[n+20:n+23]
    dataC_avil=recieve_dfh_info[n+32:n+35]
    percentC=(float(dataC_used)/(float(dataC_avil)+float(dataC_used)))*100
# Collecting Data B 
  if recieve_dfh_info[n]=='n' and recieve_dfh_info[n+1]=='/' and recieve_dfh_info[n+2]=='d' and recieve_dfh_info[n+3]=='a' and recieve_dfh_info[n+4]=='t' and recieve_dfh_info[n+5]=='a' and recieve_dfh_info[n+6]=="B":
    dataB_used=recieve_dfh_info[n+20:n+23]
    dataB_avil=recieve_dfh_info[n+32:n+35]
    percentB=(float(dataB_used)/(float(dataB_avil)+float(dataB_used)))*100
# Collecting Data A and home
  if recieve_dfh_info[n]=='n' and recieve_dfh_info[n+1]=='/' and recieve_dfh_info[n+2]=='d' and recieve_dfh_info[n+3]=='a' and recieve_dfh_info[n+4]=='t' and recieve_dfh_info[n+5]=='a' and recieve_dfh_info[n+6]=='A':
    dataA_used=recieve_dfh_info[n+20:n+23]
    dataA_avil=recieve_dfh_info[n+32:n+35]
    percentA=(float(dataA_used)/(float(dataA_avil)+float(dataA_used)))*100
#checks every word stored in recieve_node_info line by line
for a in recieve_node_info:
#if statement for referencing the end of the line in each sentence contained by recieve_node_info
 if a=='\n':
  first_index=take_frm_counter
  #passing the reference of take_frm_counter to first_index, were first_index is the beginning of
  #every sentence in recieve_node_info
  line=recieve_node_info[first_index+1:counter2+1]
  take_frm_counter=counter2
  #find the number of processors for each node
  if "np = " in line:
   processes=line
   for zt in range (0, len(processes)):
    if processes[zt]=='n' and processes[zt+1]=='p' and processes[zt+4]==" ":
     xt=processes.index('\n')
     process_number=processes[zt+4:xt]
    #print process_number
  take_frm_counter=counter2
  line=recieve_node_info[first_index:counter2+1]
  #checking the number of jobs that run in the cluster
  if "jobs" in line:
   Job=line
   for j in range(0, len(Job)):
    if Job[j]=='j' and Job[j+1]=='o' and Job[j+2]=='b' and Job[j+6]==' ':
     k=0;
     No_of_proc+=1
     while k<len(Job):
      #count jobs by commas that differentiate them
      if Job[k]==',':
       No_of_proc+=1
      k+=1
   #print No_of_proc
  #This condition checks the state of each node then converts the results to their respective color 
  if "state" in line:
   array_state=line
   for f in range (0, len(array_state)):
    if array_state[f]=='s' and array_state[f+2]=='a' and array_state[f+6]=='=':
     x=array_state.index('\n')
     state_type=array_state[f+8:len(array_state)]
     #print state_type
     if "down" in  array_state:
      state_color="#ff0000"
     else:
      if "offline" in array_state:
       state_color="#FFC0CB"
      else:
       if "free" in array_state:
        state_color="#ffffff"
       else:
        if "job-exclusive" in array_state:
         state_color="#DAA520"
  #this contion gives the node number
  if "core.wits.ac.za-0\n" in line:
   array_node_no=line
   for k in range(0,len(array_node_no)):
     if array_node_no[k]=='n' and array_node_no[k+3]=='.' and array_node_no[k+9]=='w':
      node_number2=array_node_no[k+1:k+3]
      #print node_number2
  #this	statementcurrently has no function in the current programme
  #but its job is to read the availible, used and total memory that is in each cluster
  if "status" in line:
   status=line
   for i in range(0, len(status)):
    if status[i]=='n' and status[i+3]=='.':
     node_number=status[i+1:i+3]
     #print node_number
    else:
      if status[i]=='p' and status[i+1]=='h'and status[i+6]=='m':
       x=status.index('k')
       physicalmem = status[i+8:x]
       #print physicalmem
      else:
        if status[i]=='a' and status[i+4]=='l' and status[i+8]=='=':
          x=i+8
          while status[x]!='k':
           x+=1
          availiblemem=status[i+9:x]
          #print availiblemem
        else:
          if status[i]=='t' and status[i+2]=='t' and status[i+3]=='m' and status[i+6]=='=':
            x=i+7
            while status[x]!='k':
             x+=1
            totalmem=status[i+7:x]
            #print totalmem
  #this condition calcylates in percentage the nodes used in each claster.
  if process_number!=0.0:
   percent_mem=float((No_of_proc)/float(process_number))*100
  #stores in array if nodes used are less than 80%
  if node_number!=" " and totalmem!=" " and state_type!=" " and float(percent_mem)<80.00 and No_of_proc>=0 and process_number!=" ":
    #print"1: "+node_number2
    Matrix[0][int(node_number2)]="<td>"+node_number2+"</td>"
    Matrix[1][int(node_number2)]="<td bgcolor="+state_color+"></td>"
    Matrix[2][int(node_number2)]="<td bgcolor=\"#008000\"></td>"
    node_number2=" "
    totalmem=" "
    state_type=" "
    availiblemem=" "
    physicalmem=" "
    No_of_proc=0
    state_color=" "
 else:
   #stores in array if nodes used are greater or equal to 80%
   if node_number!=" " and totalmem!=" " and state_type!=" " and float(percent_mem)>=80.00 and No_of_proc>=0 and process_number!=" ":
    counter+=1
    #print "2:"+node_number2
    Matrix[0][int(node_number2)]="<td>"+node_number2+"</td>"
    Matrix[1][int(node_number2)]="<td bgcolor="+state_color+"></td>"
    Matrix[2][int(node_number2)]="<td bgcolor=\"#0000FF\"></td>"
    node_number2=" "
    totalmem=" "
    state_type=" "
    availiblemem=" "
    physicalmem=" "
    No_of_proc=0
    state_color=" "
   else:
    #condition happens when its down and and there are still jobs running in the claster
    if state_type ==" down" and No_of_proc>=0:
     #print "3:"+node_number2
     counter+=1
     Matrix[0][int(node_number2)]="<td>"+node_number2+"</td>"
     Matrix[1][int(node_number2)]="<td bgcolor="+state_color+"></td>"
     Matrix[2][int(node_number2)]="<td bgcolor=\"#000000\"></td>"
     node_number2=" "
     state_type=" "
     No_of_proc=0
     state_color=" "
 counter2+=1
#assigns the 2D array to 1D array to prepere for refinary
Matrix2=''.join(map(str,Matrix[0:3]))
c=0
#array is bieng refined, taking out all unwanted data
while c<len(Matrix2):
 if Matrix2[c]=="0" and Matrix2[c+1]==',' and Matrix2[c+2]==" ":
  c+=3
 else:
  if Matrix2[c]=="'" or Matrix2[c]=="," or Matrix2[c]=="]":
   c+=1
  else:
   if (Matrix2[c]=="[" and Matrix2[c+1]=="'"):
    c+=2
   else:
    Matrix3.append(Matrix2[c])
    c+=1
#printing to output2.html in an html format.
out_put_file.write(''.join(map(str,Matrix3)))
out_put_file.write("</tr></table>")
out_put_file.write("\n<p></p>\n<p></p>\n<p></p>\n<p></p>\n<p></p>")
out_put_file.write("<center><table style=\"width:20%\" align=\"left\" border=\"1px\"><tr><th>Directories</th><th>Used Mem(TB)</th><th>Availible Mem(TB)</th><th>Used Mem(%)</th></tr>")
out_put_file.write("<tr><td>/dataA<br/>/home</td><td>"+dataA_used+"</td><td>"+dataA_avil+"</td><td>"+str(percentA)+"</td></tr>")
out_put_file.write("<tr><td>/dataB</td><td>"+dataB_used+"</td><td>"+dataB_avil+"</td><td>"+str(percentB)+"</td></tr>")
out_put_file.write("<tr><td>/dataC<br/>/spaces</td><td>"+dataC_used+"</td><td>"+dataC_avil+"</td><td>"+str(percentC)+"</td></tr>")
out_put_file.write("<tr><td>/dataD</td><td>"+dataD_used+"</td><td>"+dataD_avil+"</td><td>"+str(percentD)+"</td></tr>")
out_put_file.write("</table></center></div><br/>")
out_put_file.write("<table style=\"width:20%\" align=\"left\" border=\"1px\"><tr><th>Keys</th></tr>")
out_put_file.write("<tr><td>Down</td><td bgcolor=\"#ff0000\"</td>  </tr>")
out_put_file.write("<tr><td>Offline</td><td bgcolor=\"#FFC0CB\"</td>  </tr>")
out_put_file.write("<tr><td>Free</td><td bgcolor=\"#ffffff\"</td> </tr>")
out_put_file.write("<tr><td>Job-exclusive</td><td bgcolor=\"#DAA520\"></td style=\"width:10%\">  </tr>")
out_put_file.write("<tr><td>Light loaded</td><td bgcolor=\"#008000\"></td style=\"width:10%\">  </tr>")
out_put_file.write("<tr><td>Heavy loaded</td><td bgcolor=\"#0000FF\"></td style=\"width:10%\">  </tr>")
out_put_file.write("<tr><td>Unknown</td><td bgcolor=\"#000000\"</td style=\"width:10%\">  </tr>")
out_put_file.write("</table></div></div><p></p><p></p><p></p><center>Last update:<p id=\"time\"></p><script>var x = document.lastModified; document.getElementById(\"time\").innerHTML =x;</script></center></body></html>")
out_put_file.close()
