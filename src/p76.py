from p31 import p31

def p76(target: int) -> int:
    # We can reuse the solution to p31 to solve this one by allowing a 'coin'
    # for every value up to the target - 1. The target - 1 ensures no single
    # coin reaches the target, so the target must be reached with a sum.
    
    result = p31(target, list(range(1, target)))
    return result

if __name__ == '__main__':
    print(p76(5))
    print(p76(100))
