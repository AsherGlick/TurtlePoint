#include <cstddef>
#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <unordered_map>
#include <sstream>


using namespace std;


////////////////////////////////////////////////////////////////////////////////
// Point
//
// A struct to store all the information associated with a point.
////////////////////////////////////////////////////////////////////////////////
struct Point {
    float x;
    float y;
    string id;

    double distance_to(const Point &p) const {
        return sqrt((x - p.x) * (x - p.x) + (y - p.y) * (y - p.y));
    }

    string to_json() {
        stringstream s;
        s << "{\"x\": " << this->x << ", \"y\": " << this->y << ", \"id\": \"" << this->id << "\"}";
        return s.str();
    }
};


////////////////////////////////////////////////////////////////////////////////
// shortest_distance
//
// A traveling salesman solver
////////////////////////////////////////////////////////////////////////////////
double shortest_distance(
    // An integer to represent the index of the current node.
    int current_node_index,

    // Bitflag for if a node has been visited.
    int visited_nodes_biflag,

    // Precomputed distance between every node and every other node.
    const vector<vector<double>> &distances,

    // A vector of weights from every node to the final node
    const vector<double> &final_node_distances,

    // n x 2^n vector cache of minimum distance
    // Cache of shortest distances from current_node to the end for a given visited_nodes_bitflag
    vector<vector<double>> &shortest_distance_to_end,
    // The optimal next node to achieve the shortest distance stored in shortest_distance_to_end
    vector<vector<int>> &optimal_next_node
) {
    // If this current_node_index + visited_node_bitflag exists in the cache
    // then we have already calculated the minimum distance required to visit
    // all the remaining nodes in the graph from this node. No need to
    // recalculate the value.
    if (shortest_distance_to_end[current_node_index][visited_nodes_biflag] != -1) {
        return shortest_distance_to_end[current_node_index][visited_nodes_biflag];
    }
   
    // If the bitflag is full of 1's we have visited every node
    if (visited_nodes_biflag == (1 << distances.size()) - 1) {
        // Add the distance from this point to the ending point
        return final_node_distances[current_node_index];
    }

    double minDist = 1e9;
    int bestNextCity = -1;

    // For every node index as i
    for (int i = 0; i < distances.size(); i++) {
        // If we are not currently on the node AND we have not visited it yet.
        if (i != current_node_index && !(visited_nodes_biflag & (1 << i))) {
            double candidateDist = distances[current_node_index][i]
                + shortest_distance(
                    i,
                    visited_nodes_biflag | (1 << i),
                    distances,
                    final_node_distances,
                    shortest_distance_to_end,
                    optimal_next_node
                );
            if (candidateDist < minDist) {
                minDist = candidateDist;
                bestNextCity = i;
            }
        }
    }

    shortest_distance_to_end[current_node_index][visited_nodes_biflag] = minDist;
    optimal_next_node[current_node_index][visited_nodes_biflag] = bestNextCity;
    return minDist;
}



// Usage: ./route <x> <y> <id> [<x> <y> <id>]+

// 68 82 a 54 89 b 86 52 c 5 78 d 83 46 e 26 39 f 64 5 g 75 62 h 72 5 i 6 2 j 82 45 k 15 71 l 93 59 m 38 95 n 41 8 o 56 77 p 98 38 q 39 60 r 75 9 s 90 1 t

        // {6, 55},
        // {83, 46},
        // {71, 19},
        // {39, 71},
        // {66, 67},


int main(int argc, char* argv[]) {

    vector<Point> points;

    for (size_t i = 1; i < argc; i+=3){
        Point point;

        point.x = atoi(argv[i]);
        point.y = atoi(argv[i+1]);
        point.id = argv[i+2];

        points.push_back(point);
    }
    int n = points.size() - 1;

    // Build a cache of all the distances between every combination of points.
    vector<vector<double>> distances(n, vector<double>(n, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            distances[i][j] = points[i].distance_to(points[j]);
        }
    }


    // Build a cache of all the distances from every node to the final node
    vector<double> final_node_distances(n, 0);
    int FINAL_TRAVERSAL_WEIGHT_MULTIPLIER = 100;
    for (int i = 0; i < n; i++) {
        final_node_distances[i] = FINAL_TRAVERSAL_WEIGHT_MULTIPLIER * points[i].distance_to(points[points.size() - 1]);
    }


    // Prep the cache 
    vector<vector<double>> shortest_distance_to_end(n, vector<double>(1 << n, -1));
    vector<vector<int>> optimal_next_node(n, vector<int>(1 << n, -1));


    // With a fixed starting point, calculate the shortest distance to all other points
    double shortestPath = shortest_distance(
        0,
        1,
        distances,
        final_node_distances,
        shortest_distance_to_end,
        optimal_next_node
    );


    // Trace through the cache to find the shortest path taken to print out the
    // json representation of the path.
    vector<Point> path;
    int current_node = 0;
    int current_visited = 1;

    cout << "{" << endl;
    cout << "    \"distance\": " << shortestPath << "," << endl;
    cout << "    \"points\": [" << endl;
    cout  << "        " << points[current_node].to_json() <<  "," << endl;
    while (true) {
        current_node = optimal_next_node[current_node][current_visited];
        if (current_node == -1) {
            break;
        }
        cout << "        " << points[current_node].to_json() << "," <<  endl;
        current_visited |= (1 << current_node);
    }
    cout  << "        " << points[points.size()-1].to_json() << endl;
    cout << "    ]" << endl;
    cout << "}" << endl;

    return 0;
}



