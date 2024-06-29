# Given an integer n representing number of vertices. 
# Find out how many undirected graphs (not necessarily connected) 
# can be constructed out of a given n number of vertices.

def count(n):
    return 2 ** (((n - 1) * n) // 2)

if __name__ == "__main__":
    n = int(input("Enter number of Vertices: "))
    print("Number of undirected graphs that can be constructed: ", count(n))