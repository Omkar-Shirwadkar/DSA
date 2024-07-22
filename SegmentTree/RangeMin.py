# Segment Tree takes 4N space

N = 100000
tree1 = [0] * (4 * N)

# Builds tree from the end i.e leaf nodes, 
# grouping starts from last index
def build(arr, n):
    for i in range(n):
        tree1[n + i] = arr[i]
    for i in range(n - 1, 0, -1):
        tree1[i] = min(tree1[i << 1],tree1[i << 1 | 1])

def query(l, r):
    res = float("inf")
    l += n
    r += n
    while l < r : 
        if (l & 1) : 
            res = min(res, tree1[l])
            l += 1
        if (r & 1) : 
            r -= 1
            res = min(res, tree1[r])
        l >>= 1
        r >>= 1
    return res

def update(p, value) :
    tree1[p + n] = value
    p = p + n
    i = p
    while i > 1:
        tree1[i >> 1] = min(tree1[i], tree1[i ^ 1])
        i >>= 1


# Builds the tree from the root node and keeps dividing, 
# grouping works according to division
tree2 = [0] * (2 * N)
def buildR(arr, si, ss, se):
    # Leaf node
    if ss == se:
        tree2[si] = arr[ss]
        return
    
    # Calculate the mid value
    mid = (ss + se) // 2
    # Build left subtree
    buildR(arr, 2 * si, ss, mid)
    # Build right subtree
    buildR(arr, (2 * si) + 1, mid + 1, se)
    
    # Build current node
    tree2[si] = min(tree2[2 * si], tree2[(2 * si) + 1])

def queryR(si,ss,se,l,r):

    # Completely Inside
    if ss >= l and se <= r:
        return tree2[si]
    
    # Completely Outside
    if l > se or r < ss:
        return float("inf")
    
    mid = (ss + se) // 2
    qleft = queryR(2 * si, ss, mid, l, r)
    qright = queryR(2 * si + 1, mid + 1, se, l, r)

    return min(qleft, qright)

def updateR(arr,si,ss,se,qi):
    if ss == se:
        tree2[si] = arr[qi]
        return
    
    mid = (ss + se) // 2
    if qi <= mid:
        updateR(arr, 2 * si, ss, mid, qi)
    else:
        updateR(arr, 2 * si + 1, mid + 1, se, qi)
    
    tree2[si] = min(tree2[2 * si], tree2[(2 * si) + 1])

if __name__ == "__main__":
    a = [1,5,2,-3,4,-1]
    n = len(a)
    # build(a, n)
    # print(*tree1[:20])
    # print(query(2, 4))
    a = [0] + a
    # Keep it 1 based index
    # si = 1, ss = 1, se = n
    buildR(a, 1, 1, n)

    print(*tree2[:20])

    # si = 1, ss = 1, se = n, l = l + 1, r = r + 1
    print(queryR(1, 1, n, 2 + 1, 4 + 1))

    # Update 3rd element
    a[3] = -21
    updateR(a, 1, 1, n, 3)
    print(queryR(1, 1, n, 2 + 1, 4 + 1))