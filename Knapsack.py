def knapsack(e, cap, n):

    if n == 0 or cap == 0:
        return 0
    
    if e[n-1][0] > cap:
        return knapsack(e, cap, n-1)
    
    else:
        return max(e[n-1][1] + knapsack(e, cap - e[n-1][0], n-1), knapsack(e, cap, n-1))

def main():
    e = [(3, 4), (5, 6), (5, 5), (2, 1)]
    cap = 15

    print(knapsack(e, cap, len(e)))
    
main()