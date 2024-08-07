#include<iostream>
#include<stdio.h>
//#include<bits/stdc++.h>
#include<stdlib.h>
using namespace std;
struct node
{
    int data;
    struct node *left;
    struct node *right;
};
struct node *tree;

//Initialize all ptrs and values
//function signature
void create_tree(struct node *);
struct node *insert_node(struct node *, int);
void preordertraversal(struct node *);
void inordertraversal(struct node *);
void postordertraversal(struct node *);
struct node *smallestElement(struct node *);
struct node *largestElement(struct node *);
struct node *mirror(struct node *);
struct node *delete_tree(struct node *);
int Height(struct node *);
int totalNodes(struct node *);
//main body
int main(){

    struct node *ptr;
    int n, val, total=0;

    do{
        printf("\n***   MENU   ***\n");
        printf("\n1:Create");
        printf("\n2:Add a Node");
        printf("\n3:Preorder");
        printf("\n4:Inorder");
        printf("\n5:Postorder");
        printf("\n6:Smallest");
        printf("\n7:Largest");
        printf("\n8:Total Number of Nodes");
        printf("\n9:Height");
        printf("\n10:Mirror");
        printf("\n11:Delete");
        printf("\n99:Stop");
        printf("\nEnter Your Choice :");
        scanf("%d",&n);
        switch(n){
            case 1:
                create_tree(tree);
                printf("\nTree created!");
                break;

            case 2:
                cout<<"\nInsert a node value:";
                cin>>val;
                tree = insert_node(tree,val);
                break;

            case 3:
                cout<<"\n Preorder :";
                if(tree == NULL)
                    cout<<"NULL";
                else
                    preordertraversal(tree);
                break;

            case 4:
                cout<<"\n Inorder :";
                inordertraversal(tree);
                break;

            case 5:
                cout<<"\n Postorder :";
                postordertraversal(tree);
                break;

            case 6:
                cout<<"\nSmallest Element is: ";
                ptr = smallestElement(tree);
                if(ptr == NULL)
                    cout<<"\nError";
                else
                    cout<<ptr->data;
                break;

            case 7:
                cout<<"\nLargest Element is: ";
                ptr = largestElement(tree);
                if(ptr == NULL)
                    cout<<"\nNot found...Error";
                else
                    cout<<ptr->data;
                break;

            case 8:
                cout<<"\nTotal Number of Nodes are: "<<totalNodes(tree);
                break;

            case 9:
                cout<<"\nHeight of a tree is: "<<Height(tree);
                break;

            case 10:
                cout<<"\nMirrored!";
                tree = mirror(tree);
                break;

            case 11:
                cout<<"\nTree deleted!";
                tree = delete_tree(tree);
                break;

            case 99:
                cout<<"Thank You!";
                break;

            default:
                printf("\nInvalid Input \n");
                break;
        }
    }
    while(n != 99);
    return 0;
}
void create_tree(struct node *tree){
    tree = NULL;
}

struct node *mem_allocate(){
    return (struct node *)malloc(sizeof(struct node));
}

struct node *insert_node(struct node *tree, int val){
    struct node *ptr, *parentptr, *nodeptr;
    ptr = mem_allocate();
    ptr->data = val;
    ptr->left = NULL;
    ptr->right = NULL;
    if(tree == NULL){
        tree = ptr;
        tree->left = NULL;
        tree->right = NULL;
    }
    else{
    parentptr = NULL;
    nodeptr = tree;
    while(nodeptr != NULL){
        parentptr = nodeptr;
        if(val < nodeptr->data)
            nodeptr = nodeptr->left;
        else
            nodeptr = nodeptr->right;
    }
    if(val < parentptr->data)
        parentptr->left = ptr;
    else
        parentptr->right = ptr;
    }
    return tree;
}

void preordertraversal(struct node *tree){
    if(tree != NULL){
        cout<<"\t"<<tree->data;
        preordertraversal(tree->left);
        preordertraversal(tree->right);
    }
}

void inordertraversal(struct node *tree){
    if(tree != NULL){
        inordertraversal(tree->left);
        cout<<"\t"<<tree->data;
        inordertraversal(tree->right);
    }
}

void postordertraversal(struct node *tree){
    if(tree != NULL){
        inordertraversal(tree->left);
        inordertraversal(tree->right);
        cout<<"\t"<<tree->data;
    }
}

struct node *smallestElement(struct node *tree){
    if( (tree == NULL) || (tree->left == NULL) )
        return tree;
    else
        return smallestElement(tree->left);
}

struct node *largestElement(struct node *tree){
    if( (tree == NULL) || (tree->right == NULL) )
        return tree;
    else
        return smallestElement(tree->right);
}

int totalNodes(struct node *tree){
    if(tree == NULL)
        return 0;
    else
        return (totalNodes(tree->left) + totalNodes(tree->right) + 1);
}

int Height(struct node *tree){
    int LH, RH;
    if(tree == NULL)
        return 0;
    else{
        LH = Height(tree->left);
        RH = Height(tree->right);
        if(LH>RH)
            return (LH+1);
        else
            return (RH+1);
    }
}
struct node *mirror(struct node *tree){
    struct node *temp;
    if(tree != NULL){
        mirror(tree->left);
        mirror(tree->right);
        temp = tree->left;
        temp->left = temp->right;
        tree->right = temp;
    }
    return tree;
}
struct node *delete_tree(struct node *tree){
    if(tree != NULL){
        delete(tree->left);
        delete(tree->right);
        free(tree);
    }
    return tree;
}
