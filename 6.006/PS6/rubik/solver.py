import rubik

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    if not (legal(start) or legal(end)):
        return None
    
    if start==end:
        return[]
    f_visited={}
    b_visited={}
    f_visited[start] = {'parent':None, 'move':None}
    b_visited[end] = {'parent':None, 'move':None}
    forward_frontier=[start]
    backward_frontier=[end]
    count=0
    ans=None
    
    while count<8:
        
        f_next=[]
        b_next=[]
        
        BFS(forward_frontier, f_visited, f_next)
        BFS(backward_frontier, b_visited, b_next)
        
        for seq in f_next:
            if not b_visited.get(seq, False):
                continue
            else:
                ans=seq
                break
        forward_frontier=f_next
        backward_frontier=b_next
        count+=1
        if ans!=None:
            break
    
    if ans==None:
        return ans
    
    answer=[]
    value=f_visited[ans]
    while value['move']:
        answer.append(value['move'])
        value=f_visited[value['parent']]
    answer=answer[::-1]
    
    value = b_visited[ans]
    while value['move']:
        answer.append(rubik.perm_inverse(value['move']))
        value=b_visited[value['parent']]
    
    return answer

def BFS(frontier, dic, lis):
    for pos in frontier:
        for turn in rubik.quarter_twists:
                new_config=rubik.perm_apply(turn,pos)
                if dic.get(new_config, False):
                    continue
                dic[new_config]={'parent':pos,'move':turn}
                lis.append(new_config)
    
def legal(config):
    if config[-1]!=23 or config[-2]!=22 or config[-3]!=21:
        return False
    
    for i in range((len(config)//3)-1):
        a=config[3*i]//3
        b=config[3*i+1]//3
        c=config[3*i+2]//3
        if not a==b==c:
            return False
        return True