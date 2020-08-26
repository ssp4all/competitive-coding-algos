#include<iostream>
using namespace std;
#define NODE 10
void bfs(int [][NODE], int [], int);

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

    bfs(adj, visited, 0);
    return 0;
}
void bfs(int adj[NODE][NODE], int visited[NODE], int start){
    int front=-1, rear=-1, queue[NODE]={0}, i, j;
    queue[++rear] = start;
    visited[start] = 1;
    while(rear != front){

        start = queue[++front];

        if(start == (NODE-1))
            cout<<"NODE"<<"\t";
        else
            cout<<(char)(start+65)<<"\t";

        for(i=0; i<NODE; i++){
            if(adj[start][i] == 1 && visited[i] == 0){
                queue[++rear] = i;
                visited[i] = 1;
            }
        }
    }
}



