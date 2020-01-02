#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'timeOfBuffering' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts foll owing parameters:
 *  1. INTEGER arrivalRate
 *  2. INTEGER_ARRAY packets
 */

int timeOfBuffering(int arrivalRate, vector<int> packets) {
    unordered_set<int> buffer;
    int t = 1;
    for(int i = 0; i < packets.size(); i=i+arrivalRate)
    {
       auto it = packets.end();
       if(i + arrivalRate > packets.size()) 
       {
         it = packets.end();
       }
       else  {
         it = i + arrivalRate + packets.begin();
       }
       vector<int> receivedPackets(packets.begin() + i, it);

       int packetToPlay = receivedPackets[0];
  
       bool found = false;
       if(buffer.find(t) != buffer.end())
       {
           found = true;
       }

       else {
            if(packetToPlay != t) return t;
            else{
                int j = 1;
                found = true;
                while(j < arrivalRate)
                {
                    if(receivedPackets[j] > t)
                        buffer.insert(receivedPackets[j]);
                    j++;
                } 
            }                  
       }
       if(!found) return t;
       t++; 
    }
    return -1;
}