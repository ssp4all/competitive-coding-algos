#include<iostream>
using namespace std;
#define NODE 5
void dfs(int [][NODE], int [], int);

int main(){
    //int adj[NODE][NODE];
    int adj [NODE][NODE] = {
                        {0,1,0,1,0},
                        {1,0,1,1,0},
                        {0,1,0,0,1},
                        {1,1,0,0,1},
                        {0,0,1,1,0}
                    };
    int visited[NODE]={0}, i;

    dfs(adj, visited, 0);
    return 0;
}
void dfs(int adj[NODE][NODE], int visited[NODE], int start){
    int i;
    int top = -1;
    int stack[NODE];

    stack[++top] = start;
    cout<<(char)(start+65)<<"\t";
    visited[start] = 1;
    while(top != -1){

        start = stack[top];

        for(i=0; i<NODE; i++){
            if(adj[start][i] == 1 && visited[i] == 0){
                cout<<(char)(i+65)<<"\t";
                stack[++top] = i;
                visited[i] = 1;
                break;
            }
        }
        if(i == NODE)
            top--;
    }
}


