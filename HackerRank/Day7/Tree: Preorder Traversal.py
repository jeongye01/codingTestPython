#Tree: Preorder Traversal
#내 풀이->테스트 통과 DATE=>5.18 풀이시간 15분
def preOrder(root):
    #Write your code here
    print(root,end=" ")
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)