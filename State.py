class State:
    goal = []  # Will be dynamically set based on n

    greedy_evaluation = None
    AStar_evaluation = None
    heuristic = None

    def __init__(self, state, parent, direction, depth, cost, n):
        self.state = state
        self.parent = parent
        self.direction = direction
        self.depth = depth

        if parent:
            self.cost = parent.cost + cost
        else:
            self.cost = cost

        # Dynamically set the goal state based on n
        self.set_goal_state(n)

    def set_goal_state(self, n):
        self.goal = list(range(1, n*n)) + [0]

    def test(self): #check if the given state is goal
        if self.state == self.goal:
            return True
        return False
        
    #heuristic function based on Manhattan distance
    def Manhattan_Distance(self, n):
        self.heuristic = 0
        for i in range(1, n*n):
            current_position = self.state.index(i)
            goal_position = self.goal.index(i)
            # Calculate Manhattan distance
            distance = abs(current_position % n - goal_position % n) + abs(current_position // n - goal_position // n)
            self.heuristic += distance
        self.AStar_evaluation = self.heuristic + self.cost
        return (self.AStar_evaluation, self.heuristic)


    @staticmethod
    #this would remove illegal moves for a given state
    def available_moves(x,n): 
        moves = ['Left', 'Right', 'Up', 'Down']
        if x % n == 0:
            moves.remove('Left')
        if x % n == n-1:
            moves.remove('Right')
        if x - n < 0:
            moves.remove('Up')
        if x + n > n*n - 1:
            moves.remove('Down')

        return moves

    #produces children of a given state
    def expand(self , n): 
        x = self.state.index(0)
        moves = self.available_moves(x,n)
        
        children = []
        for direction in moves:
            temp = self.state.copy()
            if direction == 'Left':
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direction == 'Right':
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direction == 'Up':
                temp[x], temp[x - n] = temp[x - n], temp[x]
            elif direction == 'Down':
                temp[x], temp[x + n] = temp[x + n], temp[x]
        
            children.append(State(temp, self, direction, self.depth + 1, 1, n)) #depth should be changed as children are produced
        return children

    #gets the given state and returns it's direction + it's parent's direction until there is no parent
    def solution(self):
        solution = []
        solution.append(self.direction)
        path = self
        path_length = 0  # Initialize the path length counter
        while path.parent != None:
            path = path.parent
            solution.append(path.direction)
            path_length += 1  # Increment path length for each step
        solution = solution[:-1]
        solution.reverse()
        return solution, path_length  # Return both solution path and its length
