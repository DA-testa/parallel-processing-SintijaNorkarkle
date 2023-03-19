"""
Sintija Norkārkle, RDCPO, 1. grupa
"""

# python3

def SiftDown(i, heap):
    indekss = i
    kreisais_b = 2 * i + 1
    labais_b = 2 * i + 2

    if kreisais_b < len(heap):
        if heap[indekss][1] > heap[kreisais_b][1]:
            indekss = kreisais_b
        elif heap[indekss][1] == heap[kreisais_b][1] and heap[indekss][0] > heap[kreisais_b][0]:
            indekss = kreisais_b
    
    if labais_b < len(heap):
        if heap[indekss][1] > heap[labais_b][1]:
            indekss = labais_b
        elif heap[indekss][1] == heap[labais_b][1] and heap[indekss][0] > heap[labais_b][0]:
            indekss = labais_b

    if indekss != i:
        heap[i], heap[indekss] = heap[indekss], heap[i]
        SiftDown(indekss, heap)



def parallel_processing(n, m, data):
    output = []
    threads = [(i, 0) for i in range(n)]

    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    
    for d in data:
            nd = threads[0][0]
            output.append((nd, threads[0][1]))
            threads[0] = (nd, threads [0][1] + d)
            SiftDown(0, threads)

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for d in result:
        print(d[0], d[1])

    # n = 0
    # m = 0

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    # data = []

    # TODO: create the function
    
    # TODO: print out the results, each pair in it's own line

if __name__ == "__main__":
    main()
