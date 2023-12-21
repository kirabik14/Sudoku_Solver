#Soduko Solver by Backtracking

#defining the required lists
grid= [[], [], [], [], [], [], [], [], []]

#subgrid formation
def form_subgrid():
    global grid, subgrid
    subgrid= [[grid[0][0], grid[0][1], grid[0][2], grid[1][0], grid[1][1], grid[1][2], grid[2][0], grid[2][1], grid[2][2]],
               [grid[0][3], grid[0][4], grid[0][5], grid[1][3], grid[1][4], grid[1][5], grid[2][3], grid[2][4], grid[2][5],],
               [grid[0][6], grid[0][7], grid[0][8], grid[1][6], grid[1][7], grid[1][8], grid[2][6], grid[2][7], grid[2][8]],
               [grid[3][0], grid[3][1], grid[3][2], grid[4][0], grid[4][1], grid[4][2], grid[5][0], grid[5][1], grid[5][2]],
               [grid[3][3], grid[3][4], grid[3][5], grid[4][3], grid[4][4], grid[4][5], grid[5][3], grid[5][4], grid[5][5]],
               [grid[3][6], grid[3][7], grid[3][8], grid[4][6], grid[4][7], grid[4][8], grid[5][6], grid[5][7], grid[5][8]],
               [grid[6][0], grid[6][1], grid[6][2], grid[7][0], grid[7][1], grid[7][2], grid[8][0], grid[8][1], grid[8][2]],
               [grid[6][3], grid[6][4], grid[6][5], grid[7][3], grid[7][4], grid[7][5], grid[8][3], grid[8][4], grid[8][5],],
               [grid[6][6], grid[6][7], grid[6][8], grid[7][6], grid[7][7], grid[7][8], grid[8][6], grid[8][7], grid[8][8]]]

#finding which subgrid the element lies in
def find_subgrid(row, column):
    global grid, subgrid
    form_subgrid()
    '''for i in range(9):
        print(subgrid[i])'''
    #row choice -> subgrid
    if row in (0,1,2):
        subgrid_choices= (0,1,2)
    elif row in (3,4,5):
        subgrid_choices= (3,4,5)
    elif row in (6,7,8):
        subgrid_choices= (6,7,8)
    #column choice -> subgrid
    if column in (0,1,2):
        return subgrid_choices[0]
    if column in (3,4,5):
        return subgrid_choices[1]
    if column in (6,7,8):
        return subgrid_choices[2]

#checking valid entries
def check_valid(row, column):
    global grid, subgrid
    entries= [1,2,3,4,5,6,7,8,9]
    #checking row elements
    for i in range(9):
        if grid[row][i] in entries:
            entries.remove(grid[row][i])
    #checking column elements
    for i in range(9):
        if grid[i][column] in entries:
            entries.remove(grid[i][column])
    #checking subgrid elements
    index= find_subgrid(row, column)
    #print(index)
    for i in range(9):
        if subgrid[index][i] in entries:
            entries.remove(subgrid[index][i])
    return entries

#iterating and putting values in cells
def put_value(r, c):
    global grid, subgrid
    if r== 9:                       #finished the last row -> Program over!!
        #print("row9 True")
        return True
    elif c== 9:                     #finished the last column cell -> we proceed to next row
        #print(r, "th row ->", grid[r])
        return put_value(r+1, 0)
    elif grid[r][c]!= 0:             #If the cell is filled already -> move over to next cell
        return put_value(r, c+1)
    else:                                   #If the cell is empty (having 0)
        #print(check_valid(r,c))
        for number in check_valid(r, c):    #we iterate through the valid numbers for the cell
            grid[r][c]= number             #putting a number
            if put_value(r, c+1):           #and checking futher for success
                return True                  
            grid[r][c]= 0                   #as we failed, we undo our "by-mistake" fill
        return False                        #and backtrack....
      
#input of unsolved sudoku
print("Enter the row entries as a 9 digit number, leave 0 for blank spaces")
for i in range(9):
    print(i+1, end=" ")
    grid[i] = list(input("row entries: "))
    for j in range(9):
        grid[i][j]= int(grid[i][j])

#solving
put_value(0,0)

#printing of solved sudoku
for i in range(9):
    print(grid[i])

