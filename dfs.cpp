Struct Node {
	int self ;
	Node* left ;
	Node* right ;
} ;
const int TREE_SIZE = 9 ;
std::stack<Node*> visited , unvisted ;
Node nodes[TREE_SIZE] ;
Node* current ;

for (int i = 0 ; i <TREE_SIZE ; i++ ) {
	nodes[i].self = i ;
	int child = i * 2 + 1 ;
	if (child < TREE_SIZE) // Left child
		nodes[i].left = &nodes[child] ;
	else
		nodes[i].left = NULL ;
	child ++ ;
	if (child < TREE_SIZE) // Right child
 		nodes[i].right = &nodes[child] ;
 	else
 		nodes[i].right = NULL ;
}

unvisted.push(&nodes[0]) ;//先把0放入unvisited stack 

//只有unvisited不空
while (!unvisted.empty()) {
	current = (unvisted.top()) ; //当前应访问的
	unvisted.pop() ;

	if (current->right != NULL)
		unvisted.push(current->right) ; //把右边压入，因为右边的访问次序是在左边之后
	if (current->left != NULL) 
		unvisted.push(current->left) ;

	visited.push(current) ;

	cout << current->self << endl ;
} 