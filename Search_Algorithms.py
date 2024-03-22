from State import State
from queue import PriorityQueue
from queue import Queue


#Breadth-first Search
def BFS(given_state , n):
    root = State(given_state, None, None, 0, 0, n) 
    if root.test():
        return root.solution()
    frontier = Queue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        explored.append(current_node.state)
        
        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    return
      

def DLS(given_state , n, depth_limit):
    root = State(given_state, None, None, 0, 0, n) 
    if root.test():
        return root.solution()
    frontier = Queue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        if current_node.depth <= depth_limit:
            explored.append(current_node.state)

            children = current_node.expand(n)
            for child in children:
                if child.state not in explored:
                    if child.test():
                        return child.solution(), len(explored)
                    frontier.put(child)
    return



def AStar_search(given_state , n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0, n)
    evaluation = root.Manhattan_Distance(n) 
    frontier.put((evaluation[1], counter, root)) #based on A* evaluation

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        
        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                evaluation = child.Manhattan_Distance(n) 
                frontier.put((evaluation[1], counter, child)) #based on A* evaluation
    return