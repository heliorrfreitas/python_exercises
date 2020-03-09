def latest(scores):
    if scores:    
        return scores[-1]

def personal_best(scores):
    greatest_score = 0
    
    for score in scores:
        if score > greatest_score:
            greatest_score = score
        
    return greatest_score

def personal_top_three(scores):
    top_tree_scores = []    

    for score in scores:            
        if len(top_tree_scores) >= 3:
            smaller_score = min(top_tree_scores)
            if score > smaller_score:
                top_tree_scores.remove(smaller_score)
                top_tree_scores.append(score)
        else:
            top_tree_scores.append(score)    

    top_tree_scores.sort(reverse=True)
    return top_tree_scores 
