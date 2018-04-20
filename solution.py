import sys
from collections import deque

def shortestLength( src, dest):
    # Solution implements a BFS That uses a queue of the set of tiles to be evaluated and a Dictionary for the tiles that we haev visited
    min = sys.maxint # Minimum value for the minimum moves we can make
    openSet = deque() # Queue for the titles we will visit in the future
    openSet.append(src) # initialize the openset with the starting location
    # Dictionary for the tiles we haev visited, Key corresponds to the tile 
    # location and value is the number of moves we took to get there
    # In this algorithm we will always have the minimum moves required to get to this tile first
    closedSet = dict() 
    closedSet[src[0] + src[1]*8] = 0
    # temp variable represents the titles we are about to visit
    temp = [0, 0]
    i = 0
    while( len(openSet) > 0): # While we still have tiles to visit
        a = openSet.popleft() 
        if ( a[0] == dest[0] and a[1] == dest[1] and closedSet[a[0] + a[1]*8] < min): # if the titles we just popped is the destination and is smaller than the current minimum
                min = closedSet[a[0] + a[1]*8] # update minimum
        # else go through all the possible moves from this title
        # We check if the love is legal( i.e it is inside the chessboard) and If the future tile is not in the ClosetSet(It has not been visited already)
        # If both conditions are met we add the title to the close set with the value of moves we took to get here.
        # Moves are the moves of the previous title added by one
        # If the moves we made are still less than the current min(if we already found the destination) append to the list
        # there is no need to search for the prospects of this title if it will take longer than the solution we already found
        else: 
            temp[0] = a[0] + 1
            temp[1] = a[1] + 2
            if( temp[0] >= 0 and temp[0] <= 63 and temp[1] >= 0 and temp[1] <= 63  and temp[0] + temp[1]*8 not in closedSet):
                closedSet[temp[0] + temp[1]*8] = closedSet[a[0] + a[1]*8] + 1    
                if (closedSet[temp[0] + temp[1]*8] < min):
                    openSet.append([temp[0], temp[1]])
            temp[0] = a[0] + 1
            temp[1] = a[1] - 2
            if( temp[0] >= 0 and temp[0] <= 63 and temp[1] >= 0 and temp[1] <= 63  and temp[0] + temp[1]*8 not in closedSet ):
                closedSet[temp[0] + temp[1]*8] = closedSet[a[0] + a[1]*8] + 1
                if (closedSet[temp[0] + temp[1]*8] < min):
                    openSet.append([temp[0], temp[1]])
            temp[0] = a[0] - 1
            temp[1] = a[1] + 2
            if( temp[0] >= 0 and temp[0] <= 63 and temp[1] >= 0 and temp[1] <= 63  and temp[0] + temp[1]*8 not in closedSet ):
                closedSet[temp[0] + temp[1]*8] = closedSet[a[0] + a[1]*8] + 1
                if (closedSet[temp[0] + temp[1]*8] < min):
                    openSet.append([temp[0], temp[1]])
            temp[0] = a[0] - 1
            temp[1] = a[1] - 2
            if( temp[0] >= 0 and temp[0] <= 63 and temp[1] >= 0 and temp[1] <= 63  and temp[0] + temp[1]*8 not in closedSet ):
                closedSet[temp[0] + temp[1]*8] = closedSet[a[0] + a[1]*8] + 1
                if (closedSet[temp[0] + temp[1]*8] < min):
                    openSet.append([temp[0], temp[1]])
            temp[0] = a[0] + 2
            temp[1] = a[1] + 1
            if( temp[0] >= 0 and temp[0] <= 63 and temp[1] >= 0 and temp[1] <= 63  and temp[0] + temp[1]*8 not in closedSet ):
                closedSet[temp[0] + temp[1]*8] = closedSet[a[0] + a[1]*8] + 1
                if (closedSet[temp[0] + temp[1]*8] < min):
                    openSet.append([temp[0], temp[1]])
            temp[0] = a[0] + 2
            temp[1] = a[1] - 1
            if( temp[0] >= 0 and temp[0] <= 63 and temp[1] >= 0 and temp[1] <= 63  and temp[0] + temp[1]*8 not in closedSet ):
                closedSet[temp[0] + temp[1]*8] = closedSet[a[0] + a[1]*8] + 1
                if (closedSet[temp[0] + temp[1]*8] < min):
                    openSet.append([temp[0], temp[1]])
            temp[0] = a[0] - 2
            temp[1] = a[1] + 1
            if( temp[0] >= 0 and temp[0] <= 63 and temp[1] >= 0 and temp[1] <= 63  and temp[0] + temp[1]*8 not in closedSet ):
                closedSet[temp[0] + temp[1]*8] = closedSet[a[0] + a[1]*8] + 1
                if (closedSet[temp[0] + temp[1]*8] < min):
                    openSet.append([temp[0], temp[1]])
            temp[0] = a[0] - 2
            temp[1] = a[1] - 1
            if( temp[0] >= 0 and temp[0] <= 63 and temp[1] >= 0 and temp[1] <= 63  and temp[0] + temp[1]*8 not in closedSet ):
                closedSet[temp[0] + temp[1]*8] = closedSet[a[0] + a[1]*8] + 1
                if (closedSet[temp[0] + temp[1]*8] < min):
                    openSet.append([temp[0], temp[1]])
    # We have searched all the titles return the minimum 
    return min

def answer(src, dest):
    # Solution to here
    # Check if src and dest values are invalid and return
    if( src < 0 or src > 63 or dest < 0 or dest > 63):
        print( "Invalid inputs, Enter a value between 0 and 63")
        return
    # Chesss board takes the horizontal rows as the 0th index and the vertical rows as the 1st index
    start = [src / 8, src % 8]
    destination = [ dest / 8 , dest % 8]
    # call the solution method with fixed parameters
    return shortestLength(start, destination)

