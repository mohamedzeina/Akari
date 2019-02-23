import constraint
import numpy as np

class Block():
    def __init__(self, name, r, c, count):
        self.name = name
        self.r = r
        self.c = c
        self.value = count
        
class Empty():
    def __init__(self, name, r, c, partition):
        self.name = name
        self.r = r
        self.c = c
        self.part = partition
       
class EmptyCell():
    def __init__(self, name, r, c, partition1, partition2):
        self.name = name
        self.r = r
        self.c = c
        self.r_part = partition1
        self.c_part = partition2
            
      

  
def checkLeft(i, j, mat):
    if(mat[i][j - 1] == 'E'):
        return True
    else:
        return False
    
def checkRight(i, j, mat):
    if(mat[i][j + 1] == 'E'):
        return True
    else:
        return False
    
def checkUp(i, j, mat):
    if(mat[i - 1][j] == 'E'):
        return True
    else:
        return False  

    
def checkDown(i, j, mat):
    if(mat[i + 1][j] == 'E'):
        return True
    else:
        return False  


def checkLeft2(i, j, mat):
    temp = []
    
    while (j - 1 >= -1 and mat[i][j] == 'E'):
        i_d = str(i) + str(j)
        temp.append(i_d)
        j -= 1
    return temp
    
def checkRight2(i, j, mat):
    temp = []
    
    while (j + 1 <= cols and mat[i][j] == 'E'):
        i_d = str(i) + str(j)
        temp.append(i_d)
        j += 1
    return temp
    
def checkUp2(i, j, mat):
    temp = []

    while (i - 1 >= -1 and mat[i][j] == 'E' ):
           i_d = str(i) + str(j)
           temp.append(i_d)
           i -= 1
    return temp  

    
def checkDown2(i, j, mat):
    temp = []
    while (i + 1 <= rows and mat[i][j] == 'E' ):
        i_d = str(i) + str(j)
        temp.append(i_d)
        i += 1
    return temp
        


     

    
        
       
def getBlocks(Matrix):
    Type_Cell = None
    Row = 0
    Col = 0
    Value = 0
    Blocks = []
    Block_temp = None
    Final_Blocks = []
    
    
    for i in range(rows):
        for j in range(cols):
            if(Matrix[i][j] != 'E'):
                Row = i
                Col = j
                Value = int(Matrix[i][j])
                Type_Cell = 'Block'
                Block_temp = Block(Type_Cell, Row, Col, Value)
                Blocks.append(Block_temp)
               
                
    Final_Blocks = change_to_array2(Blocks)           
    return Final_Blocks

def find(i, j, templist):
    for x in range(len(templist)):
        if(templist[x].r == i and templist[x].c == j):
            return templist[x].part
            
    
def change_to_array1(list_temp):
    typ = None 
    row = None
    col = None
    rpart = None
    cpart = None
    coord = None
    temp = []
    final_list = []
    for i in list_temp:
        typ = i.name 
        row = i.r
        col = i.c 
        rpart = i.r_part
        cpart = i.c_part
        coord = str(row) + str(col)
        temp = [typ, row, col, rpart, cpart, coord]
        final_list.append(temp)
    return final_list
        
def change_to_array2(list_temp):
    typ = None 
    row = None
    col = None
    val = None
    coord = None
    temp = []
    final_list = []
    for i in list_temp:
        typ = i.name 
        row = i.r
        col = i.c
        val = i.value
        coord = str(row) + str(col)
        temp = [typ, row, col, val, coord]
        final_list.append(temp)
    return final_list
                       
                
    
def getVars(Matrix):
    Row = 0 
    Col = 0 
    R_Part = 1
    Empty_temp = None
    C_Part = 1
    R_List = []
    Type_Cell = None
    R_Part_Temp = 0
    Final_List = []
    Final_List2 = []
   
    
    
    
    for i in range(rows):
        for j in range(cols):
            Row = i 
            Col = j 
            
            if((j + 1 < cols) and (Matrix[i][j] != 'E') and (j!= 0) and (Matrix[i][j + 1] == 'E')):
                R_Part += 1
            elif(Matrix[i][j] == 'E'):
                Type_Cell = 'Empty'
                Empty_temp = Empty(Type_Cell, Row, Col, R_Part)
                R_List.append(Empty_temp)
        R_Part = 1

    for j in range(cols):
        for i in range(rows):
            Row = i 
            Col = j 
            
            if((i + 1 < rows) and (Matrix[i][j] != 'E') and (i!= 0) and (Matrix[i + 1][j] == 'E')):
                C_Part += 1
            elif(Matrix[i][j] == 'E'):
                Type_Cell = 'Empty'
                R_Part_Temp = find(Row, Col, R_List) 
                Empty_temp = EmptyCell(Type_Cell, Row, Col, R_Part_Temp, C_Part)
                Final_List.append(Empty_temp)
        C_Part = 1
        
    Final_List2 = change_to_array1(Final_List)
    return Final_List2
                

                
                
               
    




rows = 7 
cols = 7
list_temp = []

row_temp = None
col_temp = None

row_temp2 = None
col_temp2 = None



temp_coord = None


matrix = [  ['E','E','E','E','E','E','E'],
            ['E','E','E','-1','1','E','E'],
            ['E','0','E','E','E','E','E'],
            ['E','1','E','E','E','-1','E'],
            ['E','E','E','E','E','2','E'],
            ['E','E','3','-1','E','E','E'],
            ['E','E','E','E','E','E','E'],
         ]


  
  



Block_List = getBlocks(matrix)
list1 = getVars(matrix)
problem = constraint.Problem()



for i in list1:
   problem.addVariable(i[5], [0,1])
   list_temp.append(i[5])
   
for i in range(len(list1)):
    for j in range(len(list1)):
        if((list1[i] != list1[j]) and ((list1[i][3] == list1[j][3] and list1[i][1] == list1[j][1])  or (list1[i][4] == list1[j][4] and list1[i][2] == list1[j][2]))):
             problem.addConstraint(lambda x, z: x + z <= 1, 
                                    (list_temp[i], list_temp[j]))


for i in Block_List:
    filter_neighbours = []
    if(i[3] != -1):
        
        row_temp = i[1]
        col_temp = i[2]
    
        if(row_temp == 0 and col_temp == 0):
            if(checkDown(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp + 1) + str(col_temp)
                filter_neighbours.append(temp_coord)
            if(checkRight(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp) + str(col_temp + 1)
                filter_neighbours.append(temp_coord)
            if(len(filter_neighbours) > 0):
                problem.addConstraint(constraint.ExactSumConstraint(i[3]), filter_neighbours)
        
        elif(row_temp == 0 and col_temp == cols - 1):
            if(checkDown(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp + 1) +  str(col_temp)
                filter_neighbours.append(temp_coord)
            if(checkLeft(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp) + str(col_temp - 1)
                filter_neighbours.append(temp_coord)
            if(len(filter_neighbours) > 0):
                problem.addConstraint(constraint.ExactSumConstraint(i[3]), filter_neighbours)
                
        elif(row_temp == rows - 1 and col_temp == 0):
            if(checkUp(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp - 1) +  str(col_temp)
                filter_neighbours.append(temp_coord)
            if(checkRight(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp) + str(col_temp + 1)
                filter_neighbours.append(temp_coord)
            if(len(filter_neighbours) > 0):
                problem.addConstraint(constraint.ExactSumConstraint(i[3]), filter_neighbours)
        
        elif(row_temp == rows - 1 and col_temp ==  cols - 1):
            if(checkUp(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp - 1) +  str(col_temp)
                filter_neighbours.append(temp_coord)
            if(checkLeft(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp) + str(col_temp - 1)
                filter_neighbours.append(temp_coord)
            if(len(filter_neighbours) > 0):
                problem.addConstraint(constraint.ExactSumConstraint(i[3]), filter_neighbours)
                
        elif(row_temp == 0):
            if(checkRight(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp) +  str(col_temp + 1)
                filter_neighbours.append(temp_coord)
            if(checkLeft(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp) + str(col_temp - 1)
                filter_neighbours.append(temp_coord)
            if(checkDown(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp + 1) + str(col_temp)
                filter_neighbours.append(temp_coord)
            if(len(filter_neighbours) > 0):
                problem.addConstraint(constraint.ExactSumConstraint(i[3]), filter_neighbours)
                
        elif(row_temp == rows - 1):
            if(checkRight(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp) +  str(col_temp + 1)
                filter_neighbours.append(temp_coord)
            if(checkLeft(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp) + str(col_temp - 1)
                filter_neighbours.append(temp_coord)
            if(checkUp(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp - 1) + str(col_temp)
                filter_neighbours.append(temp_coord)
            if(len(filter_neighbours) > 0):
                problem.addConstraint(constraint.ExactSumConstraint(i[3]), filter_neighbours)
                
        elif(col_temp == 0):
            if(checkRight(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp) +  str(col_temp + 1)
                filter_neighbours.append(temp_coord)
            if(checkDown(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp + 1) + str(col_temp)
                filter_neighbours.append(temp_coord)
            if(checkUp(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp - 1) + str(col_temp)
                filter_neighbours.append(temp_coord)
            if(len(filter_neighbours) > 0):
                problem.addConstraint(constraint.ExactSumConstraint(i[3]), filter_neighbours)
                
        elif(col_temp == cols - 1):
            if(checkLeft(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp) +  str(col_temp - 1)
                filter_neighbours.append(temp_coord)
            if(checkDown(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp + 1) + str(col_temp)
                filter_neighbours.append(temp_coord)
            if(checkUp(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp - 1) + str(col_temp)
                filter_neighbours.append(temp_coord)
            if(len(filter_neighbours) > 0):
                problem.addConstraint(constraint.ExactSumConstraint(i[3]), filter_neighbours)
        else:
            if(checkLeft(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp) +  str(col_temp - 1)
                filter_neighbours.append(temp_coord)
            if(checkDown(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp + 1) + str(col_temp)
                filter_neighbours.append(temp_coord)
            if(checkUp(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp - 1) + str(col_temp)
                filter_neighbours.append(temp_coord)
            if(checkRight(row_temp, col_temp, matrix)):
                temp_coord = str(row_temp) + str(col_temp + 1)
                filter_neighbours.append(temp_coord)
            if(len(filter_neighbours) > 0):
                problem.addConstraint(constraint.ExactSumConstraint(i[3]), filter_neighbours)
               
for i in list1:
    temp_up = []    
    temp_down = []
    temp_left = []
    temp_right = []
    row_temp2 = i[1]
    col_temp2 = i[2]
    light_list = []
    
    temp_up = checkUp2(row_temp2, col_temp2, matrix)
    temp_down = checkDown2(row_temp2, col_temp2, matrix)
    temp_right = checkRight2(row_temp2, col_temp2, matrix)
    temp_left = checkLeft2(row_temp2, col_temp2, matrix)
    
    if(len(temp_up) != 0):
        del temp_up[0]
    if(len(temp_down) != 0):
        del temp_down[0]
    if(len(temp_right) != 0):
        del temp_right[0]
    if(len(temp_left) != 0):
        del temp_left[0]
    light_list.append(i[5])
    
    if(len(temp_up) != 0):
        for x in temp_up:
            light_list.append(x)
    if(len(temp_down) != 0):
        for z in temp_down:
            light_list.append(z)
    if(len(temp_right) != 0):
        for s in temp_right:
            light_list.append(s)
    if(len(temp_left) != 0):
        for t in temp_left:
            light_list.append(t)
    
    
    problem.addConstraint(constraint.MinSumConstraint(1), light_list)
            
    
    
    
    
    
             
        
    
           
value = None
var = None  
array_tmp = []
array_var = [] 
string_var = None
r1 = None
c1 = None

           
s = problem.getSolution() 
c = list(s)
b = list(s.values())


for i in range(len(c)):
    var = c[i]
    value = b[i]
    array_tmp = [var, value]
    array_var.append(array_tmp)

for i in array_var:
    if(i[1] == 1):
        string_var = i[0]
        r1 = int(string_var[0])
        c1 = int(string_var[1])
        matrix[r1][c1] = 'L'
        
f = np.matrix(matrix)
print(f)  