#import string module to use string.punctuation method'
import string
#creating five list to append the values and count the values.
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
#creating the file in reading mode
with open("Crime.csv",'r') as fin:
#for loop is used for traverse the words
  for line in fin:
#strip method to remove whitespaces
    word= line.strip(string.punctuation):  
#spilt method is used to split the line in to words
    word=line.split()
    word=word.lower()
#lower method to converting uppercase to lowercase letter
#by using if and elif conditional expressions it verify the conditions if its true it will append the values
    if "assault" in word and "1430" in word:
      list1.append(word[-1])
      list1.append(word[-2])
    elif "robbery" in word and "1610" in word:
      list2.append(word[-1])
      list2.append(word[-2])
    elif "theft from vehicle" in word and "2142" in word:
      list3.append(word[-1])
      list3.append(word[-2])
    elif "theft of vehicle" in word and "2135" in word: 
      list4.append(word[-1])
      list4.append(word[-2])
    elif "break and enter" in word and "2120" in word:
      list5.append(word[-1])
      list5.append(word[-2]) 
#defining function to remove the repeted words
def fun(listx):
  mylist=[]
#adding words to empty list
  for i in listx:
    if i not in mylist:  
     mylist.append(i)
  return mylist
#display the list and count method to count values
print("crime_type"," ","crime_id"," "," ","crime_count")
print(fun(list1),"\t","\t",list1.count(1430))
print(fun(list2),"\t","\t",list2.count(1610))
print(fun(list3),"\t",list3.count(2142))
print(fun(list4),"\t",list4.count(2135))
print(fun(list5),"\t",list5.count(2120))

