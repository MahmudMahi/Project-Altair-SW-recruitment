#include <iostream>
#include <vector>
#include <set>
#include <map>
using namespace std;
void dfs(const string &node, map<string, vector<string>> &graph, set<string> &visited);
void ans(int num_of_vertices, vector<pair<string, string>> &edges);
int main() {
    int num_of_vertices;
    cin >> num_of_vertices;
    vector<pair<string, string>> edges;
    string x, y;
    cout<<"enter ctrl+z after finishing giving input of edges.\nInput begins now:-"<<endl;
    while(cin >> x >> y){
        edges.push_back(make_pair(x, y));
    }
    ans(num_of_vertices, edges);
    return 0;
}

void dfs(const string &node, map<string, vector<string>> &graph, set<string> &visited) {
    visited.insert(node);
    for (const string& neighbor : graph[node]) {
        if (visited.find(neighbor) == visited.end()) {
            dfs(neighbor, graph, visited);
        }
    }
}
void ans(int num_of_vertices, vector<pair<string, string>> &edges) {
    
    if (num_of_vertices > 8) {
        cout<<"False"<<endl;
    }
    
    map<string, vector<string>> graph;
    set<string> vertices; //set is the most efficient one since it will have only unique value
                        // and all vertices are unique.
    
    for (const auto&i : edges) {
        const string &x = i.first; 
        const string &y = i.second;
        graph[x].push_back(y);
        graph[y].push_back(x);
        vertices.insert(x);
        vertices.insert(y);
    }
    set<string> visited;
    dfs(edges[0].first, graph, visited);
    //debug
    /*for(auto s= visited.begin(); s!=visited.end(); ++s){
        cout<<*s<<" ";
    }
    cout<<endl;*/
    cout<<((visited.size() == num_of_vertices)?"True":"False")<<endl;
}
/* for the given dataset there are 9 vertices not 8, therefore it will give FALSE output. 
    but if instead of 8, 9 is given as input for the num_of_vertices it will be TRUE
    All the 9 locations can be visited.*/
