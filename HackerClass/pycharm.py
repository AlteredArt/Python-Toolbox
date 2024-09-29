def count_positives_sum_negatives(arr):
    
    if arr is None or arr is not arr:
        return []
    
    positive = 0
    negative = 0
    final_numbers = []
    
    for num in arr:
        if num > 0:
            num + positive
        elif num  < 0:
            num + negative
        
    final_numbers.append(positive)
    final_numbers.append(negative)    
    return final_numbers