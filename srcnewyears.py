def minPossBribes(Q):
    #
    # initialize the number of moves
    possibleMoves = 0 
    #
    # decrease Q by 1 to make index-matching more intuitive
    # so that our values go from 0 to N-1, just like our
    # indices.  (Not necessary but makes it easier to
    # understand.)
    Q = [P-1 for P in Q]
    #
    # Loop through each person (P) in the queue (Q)
    for i,P in enumerate(Q):
        # i is the current position of P, while P is the
        # original position of P.
        #
        # First check if any P is more than two ahead of 
        # its original position
        if P - i > 2:
            print("Too chaotic")
            return
        #
        # From here on out, we don't care if P has moved
        # forwards, it is better to count how many times
        # P has RECEIVED a bribe, by looking at who is
        # ahead of P.  P's original position is the value
        # of P.
        # Anyone who bribed P cannot get to higher than
        # one position in front if P's original position,
        # so we need to look from one position in front
        # of P's original position to one in front of P's
        # current position, and see how many of those 
        # positions in Q contain a number large than P.
        # In other words we will look from P-1 to i-1,
        # which in Python is range(P-1,i-1+1), or simply
        # range(P-1,i).  To make sure we don't try an
        # index less than zero, replace P-1 with
        # max(P-1,0)
        for j in range(max(P-1,0),i):
            if Q[j] > P:
                possibleMoves += 1
    print(possibleMoves)
    
    
    
    
    
    
    #Solution # 2
    
    def minBribes(Q):
        
        possMoves = 0
        q = [P-1 for P in Q]
        if P - i > 2:
          for i, P in enumerate(Q):
       
            print("too chaotic")
       	    return
       	    
       	    for J in range(max(P-1,0),i):
       	    	if Q[J] > P:
       	    		possMoves += 1
       	    		print(possMoves)
