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
struct node *tree,*ptr;

void create_tree(struct node *);
struct node *insert_node(struct node *, val);
int n,val;

int main(){
    do{
        printf("\n***   MENU   ***\n");
        printf("\n1:Create");
        printf("\n2:Add a Node");
        printf("\n5:Display");
        printf("\n6:Count");
        printf("\n99:Stop");
        printf("\nEnter Your Choice :");
        scanf("%d",&n);
        switch(n){
            case 1:
                printf("\nTree created");
                create_tree(tree);
                break;

            case 2:
                cout<<"\nInsert a node value:";
                cin>>val;
                tree = insert_node(tree,val);
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
void create_tree( struct node *tree){
    tree = NULL;
}
struct node *insert_node(struct node *, val){


}


