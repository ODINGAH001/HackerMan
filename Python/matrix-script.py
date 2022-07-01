#python3

import re 
row,column= map(int,input().split())
matrix = [list(input()) for _ in range(row)]

#[['T', 's', 'i'], ['h', '%', 'x'], ['i', ' ', '#'], ['s', 'M', ' '], ['$', 'a', ' '], ['#', 't', '%'], ['i', 'r', '!']]

string=''#
for c in range(column):#
    for r in range(row):#
        string=string+matrix[r][c]#

#OR
#string= "".join([matrix[r][col] for col in range(column) for r in range(row) ])

#This$#is% Matrix#  %!
print(re.sub(r'(?<=\w)(\W+)(?=\w)'," ",string))# This is Matrix#  %!
