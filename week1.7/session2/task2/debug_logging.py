# Reference solution (rewritten after original work was lost)
# Week 1.7, Session 2: Task 2 - logging

import logging

def calculate_average(scores):
    # add logging configuration    
    logging.basicConfig(filename='log.txt', filemode='w', level=logging.DEBUG)
    
    # you can turn the logging off
    # logging.disable(logging.CRITICAL)
    
    logger = logging.getLogger()
    logger.info(f"calculate_average(): started")
    
    total_score = sum(scores)
    total_assignments = len(scores)
    
    # add debug logging here
    logger.debug(f"scores={scores}, total_score={total_score}, total_assignments={total_assignments}")
    
    # BUG: '//' is integer (floor) division, so 263 // 3 gave 87 and the
    # decimal part was thrown away. The log showed average=87 (an int).
    # FIX: use '/' for normal (true) division.
    average = total_score / total_assignments
    
    # add a debug logging here
    logger.debug(f"average={average} (type {type(average).__name__})")
    
    return round(average,2)

print(calculate_average([85, 90, 88]))
# Expected Output: 87.67
# Actual Output (before fix): 87.0
