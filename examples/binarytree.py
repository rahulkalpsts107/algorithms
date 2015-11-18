#Binary Tree
class Node:
    pindex =0
    head = None
    def __init__(self, data,p,h):
        self.data = data
        self.left = None
        self.right = None
        self.p = p
        self.height=h
        self.index =Node.pindex
        Node.pindex+=1
        print('created '+str(data))


    def insert(self,data):
        if(data<self.data):
            if self.left is None:
                self.left = Node(data,self,self.height+1)
                print('left'+ 'prev = '+str(self.data))
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data,self,self.height+1)
                print('right'+ 'prev = '+str(self.data))
            else:
                self.right.insert(data)

def inorder(node):
    if(node != None):
        inorder(node.left)
        print('key= '+str(node.data)+' ht = '+str(node.height))
        inorder(node.right)

def inorder_nonrecur(node,stack):
    l = node
    #stack.append(None)
    while(len(stack) is not 0 or l is not None):
        if(l is not None):
            stack.append(l)
            l = l.left
        else:
            r = stack.pop()
            print(r.data)
            l=r.right


def postorder(node):
    if(node != None):
        postorder(node.left)
        postorder(node.right)
        print(' '+str(node.data))

def preorder(node):
    if(node != None):
        print(' '+str(node.data))
        preorder(node.left)
        preorder(node.right)

def itersearch(node,k):
    x = node
    found =0
    while(x is not None):
        if(x.data == k):
            found = 1
            break
        if(k<=x.data):
            x = x.left
        if(k > x.data):
            x = x.right
    return found

def itersearchObj(node,k):
    x = node
    while(x is not None):
        if(x.data == k):
            break
        if(k<=x.data):
            x = x.left
        if(k > x.data):
            x = x.right
    return x

#log time
def getmax(node):
    tmp = node
    while(tmp.right is not None):
        tmp = tmp.right
    return tmp

#sdef getnodeofmaxht(node):

#log time
def getmin(node):
    tmp = node
    while(tmp.left is not None):
        tmp = tmp.left
    return tmp

def getsuccessor(node):
    #case 1
    if(node.right is not None):
        return getmin(node.right)
    #case2
    y = node
    x = y.p
    while(x!= None and y == x.right):
        y = x
        x = x.p
    return x

def getpredecessor(node):
    #case 1
    if(node.left is not None):
        return getmax(node.left)
    #case2
    y = node
    x = y.p
    while(x!= None and y == x.left):
        print(x.data,y.data)
        y = x
        x = x.p
    return x

def printPath(path,head):
    array=[]
    array.append(0)
    node=[]
    path_preorder(head,path,array,node)

# Order(N) runtime recurrence = 2T(N/2)+O(N)
def path_preorder(node,path,stack,nodes):
    if(node != None):
        stack.append(node.data+stack[len(stack)-1])
        #print(stack)
        nodes.append(node.data)
        if(stack[len(stack)-1] == path):
            print('found a path ='+str(path))
            print(nodes)
        #print('in stack= '+str(node.data)+' seq ='+str(node.index))
        path_preorder(node.left,path,stack,nodes)
        path_preorder(node.right,path,stack,nodes)
        nodes.pop()
        r = stack.pop()
        #print('path = '+str(r))
    else :
        return -1

def run():
    head = Node(15,None,0)
    head.insert(6)
    head.insert(18)
    head.insert(3)
    head.insert(7)
    head.insert(17)
    head.insert(20)
    head.insert(2)
    head.insert(4)
    head.insert(13)
    head.insert(9)

    print('******IN*****')
    inorder(head)
    print('******PRE*****')
    preorder(head)
    print('******POST*****')
    postorder(head)
    print('****SEARCH****')
    print(itersearch(head,15))
    print('*****MAX****')
    print(getmax(head).data)
    print('*****MIN****')
    print(getmin(head).data)
    print('*****SUCCESSOR****')
    obj = getsuccessor(itersearchObj(head,15))
    if(obj is not None):
        print(obj.data)
    else:
        print('No successor')
    print('*****PREDECESSOR****')
    obj = getpredecessor(itersearchObj(head,15))
    if(obj is not None):
        print(obj.data)
    else:
        print('No predecessor')
    #print('max lt node = '+str(getnodeofmaxht(head,-1)))
    array=[]
    print('inorder non recursive')
    inorder_nonrecur(head,array)

    printPath(28,head)

if __name__ == '__main__':
    run()
