#Binary Tree
class Node:
    head = None
    def __init__(self, data,p):
        self.data = data
        self.left = None
        self.right = None
        self.p = p
        print('created '+str(data))


    def insert(self,data):
        if(data<self.data):
            if self.left is None:
                self.left = Node(data,self)
                print('left'+ 'prev = '+str(self.data))
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data,self)
                print('right'+ 'prev = '+str(self.data))
            else:
                self.right.insert(data)

def inorder(node):
    if(node != None):
        inorder(node.left)
        print(' '+str(node.data))
        inorder(node.right)

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

def getmax(node):
    tmp = node
    while(tmp.right is not None):
        tmp = tmp.right
    return tmp

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
        y = x
        x = x.p
    return x

def run():
    head = Node(15,None)
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
    print(itersearch(head,5))
    print('*****MAX****')
    print(getmax(head).data)
    print('*****MIN****')
    print(getmin(head).data)
    print('*****SUCCESSOR****')
    obj = getsuccessor(itersearchObj(head,13))
    if(obj is not None):
        print(obj.data)
    else:
        print('No successor')
    print('*****PREDECESSOR****')
    obj = getpredecessor(itersearchObj(head,17))
    if(obj is not None):
        print(obj.data)
    else:
        print('No predecessor')


if __name__ == '__main__':
    run()
