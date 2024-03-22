from Search_Algorithms import BFS, AStar_search, DLS
from time import time
from State import State

# Function to count the number of inversions
def inv_num(puzzle):
    inv = 0
    for i in range(len(puzzle)-1):
        for j in range(i+1 , len(puzzle)):
            if (( puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):
                inv += 1
    return inv

def solvable(puzzle): #check if initial state puzzle is solvable: number of inversions should be even.
    inv_counter = inv_num(puzzle)
    if (inv_counter % 2 ==0):
        return True
    return False

example_puzzles = [
    [[8, 1, 3], [4, 0, 2], [7, 6, 5]],  # Example 1 (8-puzzle)
    [[0, 1, 3], [7, 2, 5], [8, 4, 6]],  # Example 2 (8-puzzle)
    [[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 7, 11], [13, 14, 15, 12]], # Example 3 (15-puzzle)
    [[1, 2, 3], [4, 5, 6], [8, 7, 0]], # Example 4 (8-puzzle) (Not solvable)
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 15, 14, 0]] # Example 5 (15-puzzle) (Not solvable)
] 

for i, puzzle in enumerate(example_puzzles):
    print(f"Running algorithms for Example {i + 1} puzzle:")
    n = len(puzzle)  # Determine the size of the puzzle
    print("The given state is:", puzzle)

    if solvable(sum(puzzle, [])):
        print("Solvable, please wait. \n")
    
        time1 = time()
        BFS_solution, BFS_steps = BFS(sum(puzzle, []), n)
        BFS_time = time() - time1
        print('BFS Solution is ', BFS_solution[0])
        print('Number of explored nodes is ', BFS_steps)
        print('Number of steps:', BFS_solution[1])  # Print the number of steps taken
        print('Time to completion: ', BFS_time)
        time2 = time()
        DLS_solution, DLS_steps = DLS(sum(puzzle, []), n, 30) # Depth limit set hard coded, you can adjust it as needed
        DLS_time = time() - time2
        print('DLS Solution is ', DLS_solution[0])
        print('Number of explored nodes is ', DLS_steps)
        print('Number of steps:', DLS_solution[1] )  # Print the number of steps taken
        print('Time to completion: ', DLS_time)
        time3 = time()
        AStar_solution, AStar_steps = AStar_search(sum(puzzle, []), n)
        AStar_time = time() - time3
        print('A* Solution is ', AStar_solution[0])
        print('Number of explored nodes is ',AStar_steps )
        print('Number of steps:', AStar_solution[1])  # Print the number of steps taken
        print('Time to completion: ', AStar_time)
    else:
        print("Not solvable")

    print("\n")
