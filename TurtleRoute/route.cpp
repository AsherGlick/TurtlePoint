#include <cstddef>
#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <unordered_map>
#include <sstream>
#include <algorithm>

using namespace std;



vector<string> split(string input, string delimiter) {
    vector<string> output;
    size_t cursor_position = 0;
    while ((cursor_position = input.find(delimiter)) != std::string::npos) {
        output.push_back(input.substr(0, cursor_position));
        input.erase(0, cursor_position + delimiter.length());
    }
    output.push_back(input);
    return output;
}


class WeightedDistance {
 public:
    double walking_distance;
    int coin_cost;
    double distance;

    WeightedDistance() {
        this->walking_distance = -1;
        this->coin_cost = -1;
        this->distance = -1;
    }

    WeightedDistance(double walking_distance, int coin_cost, double distance) : walking_distance(walking_distance), coin_cost(coin_cost), distance(distance) {}

    WeightedDistance(string input) {
        vector<string> elements = split(input, ":");
        if (elements.size() != 2) {
            cout << "Invalid Weighted Distance " << input << endl;
            return;
        }
        this->walking_distance = atof(elements[0].c_str());
        this->coin_cost = atoi(elements[1].c_str());
    }

    // Overloaded addition operator
    WeightedDistance operator+(const WeightedDistance& other) const {
        return WeightedDistance(
            walking_distance + other.walking_distance,
            coin_cost + other.coin_cost,
            distance + other.distance
        );
    }

    // Overloaded subtraction operator
    WeightedDistance operator-(const WeightedDistance& other) const {
        return WeightedDistance(
            walking_distance - other.walking_distance,
            coin_cost - other.coin_cost,
            distance - other.distance
        );
    }

    // Overloaded less than operator
    bool operator<(const WeightedDistance& other) const {
        if (walking_distance < other.walking_distance) {
            return true;
        }
        else if (walking_distance == other.walking_distance) {
            if (coin_cost < other.coin_cost) {
                return true;
            }
            else if (coin_cost == other.coin_cost) {
                return distance < other.distance;
            }
        }
        return false;
    }

    // Overloaded greater than operator
    bool operator>(const WeightedDistance& other) const {
        if (walking_distance > other.walking_distance) {
            return true;
        }
        else if (walking_distance == other.walking_distance) {
            if (coin_cost > other.coin_cost) {
                return true;
            }
            else if (coin_cost == other.coin_cost) {
                return distance > other.distance;
            }
        }
        return false;

    }

    bool operator==(const WeightedDistance& other) const {
        return walking_distance == other.walking_distance
            && coin_cost == other.coin_cost
            && distance == other.distance;
    }

    bool operator!=(const WeightedDistance& other) const {
        return walking_distance != other.walking_distance
        || coin_cost != other.coin_cost
        || distance != other.distance;
    }

    bool is_negative_one() {
        return coin_cost == -1 && walking_distance == -1 && distance == -1;
    }

};

////////////////////////////////////////////////////////////////////////////////
// Point
//
// A struct to store all the information associated with a point.
////////////////////////////////////////////////////////////////////////////////
struct Point {
    float x;
    float y;
    float exit_x;
    float exit_y;
    string id;
    bool can_waypoint_teleport_to;
    WeightedDistance extra_weight;


    void assign_position_from_string(string input) {
        vector<string> elements = split(input, ":");

        if (elements.size() == 2 ) {
            this->x = atof(elements[0].c_str());
            this->y = atof(elements[1].c_str());
            this->exit_x = atof(elements[0].c_str());
            this->exit_y = atof(elements[1].c_str());

        }
        else if (elements.size() == 4) {
            this->x = atof(elements[0].c_str());
            this->y = atof(elements[1].c_str());
            this->exit_x = atof(elements[2].c_str());
            this->exit_y = atof(elements[3].c_str());
        }
        else {
            cout << "Invalid Position " << input << endl;
            return;
        }

    }

    double distance_to(const Point &p) const {
        return sqrt(
            pow(exit_x - p.x, 2)
            + pow(exit_y - p.y, 2)
        );
    }

    ////////////////////////////////////////////////////////////////////////////
    // weighted_distance_to
    //
    // Calculates the weighted distance to a point, taking into account if the
    // point can be teleported to or not to determine which weight calculation
    // should be used.
    ////////////////////////////////////////////////////////////////////////////
    WeightedDistance weighted_distance_to(const Point &p) const {
        if (p.can_waypoint_teleport_to) {
            return WeightedDistance(0, coin_cost(p), distance_to(p));
        }
        else {
            return WeightedDistance(distance_to(p), 0, distance_to(p));
        }
    }

    ////////////////////////////////////////////////////////////////////////////
    // coin_cost
    //
    // How many coins waypoint travel will cost from this location to a waypoint
    // at location p. Algorithim derived from https://wiki.guildwars2.com/wiki/Waypoint
    // cost = C1 * [ 0.78 + max(0, (0.0003 / 24) * (Distance - 14400)) ] + C2
    // using the level 80 values of C1 and C2 (50 and 100 respectively) and
    // modifying distance to use continent coordinates which are 24 times the
    // length of the ingame unit. (Ingame units are an inch and continent
    // coordinates are two feet)
    ////////////////////////////////////////////////////////////////////////////
    uint coin_cost(const Point &p) const {
        return 50 * ( 0.78 + max(0.0, 0.0003 * (this->distance_to(p) - 600))) + 100;
    }

    string to_json() {
        stringstream s;
        s << "{" 
            << "\"x\": " << this->x << ", "
            << "\"y\": " << this->y << ", "
            << "\"exit_x\": " << this->exit_x << ", "
            << "\"exit_y\": " << this->exit_y << ", "
            << "\"id\": \"" << this->id << "\""
            << "}";
        return s.str();
    }
};


////////////////////////////////////////////////////////////////////////////////
// shortest_distance
//
// A traveling salesman solver
////////////////////////////////////////////////////////////////////////////////
WeightedDistance shortest_distance(
    // An integer to represent the index of the current node.
    int current_node_index,

    // Bitflag for if a node has been visited.
    int visited_nodes_biflag,

    // Precomputed distance between every node and every other node.
    const vector<vector<WeightedDistance>> &distances,

    // A vector of weights from every node to the final node
    const vector<WeightedDistance> &final_node_distances,

    // n x 2^n vector cache of minimum distance
    // Cache of shortest distances from current_node to the end for a given visited_nodes_bitflag
    vector<vector<WeightedDistance>> &shortest_distance_to_end,
    // The optimal next node to achieve the shortest distance stored in shortest_distance_to_end
    vector<vector<int>> &optimal_next_node
) {
    // If this current_node_index + visited_node_bitflag exists in the cache
    // then we have already calculated the minimum distance required to visit
    // all the remaining nodes in the graph from this node. No need to
    // recalculate the value.
    if (!shortest_distance_to_end[current_node_index][visited_nodes_biflag].is_negative_one()) {
        return shortest_distance_to_end[current_node_index][visited_nodes_biflag];
    }
   
    // If the bitflag is full of 1's we have visited every node
    if (visited_nodes_biflag == (1 << distances.size()) - 1) {
        // Add the distance from this point to the ending point
        return final_node_distances[current_node_index];
    }

    WeightedDistance minDist = WeightedDistance(1e9, 1e9, 1e9);
    int bestNextCity = -1;
    // For every node index as i
    for (int i = 0; i < distances.size(); i++) {
        // If we are not currently on the node AND we have not visited it yet.
        if (i != current_node_index && !(visited_nodes_biflag & (1 << i))) {
            WeightedDistance candidateDist = distances[current_node_index][i]
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



// Usage: ./route <x> <y> <ex> <ey> <id> <t> <w> [<x> <y> <ex> <ey> <id> <t> <w>]+
int main(int argc, char* argv[]) {
    vector<Point> points;

    for (size_t i = 1; i < argc; i+=4){
        Point point;
        point.assign_position_from_string(argv[i]);
        point.id = argv[i+1];
        point.can_waypoint_teleport_to = argv[i+2][0] == 'T';
        point.extra_weight = WeightedDistance(argv[i+3]);

        points.push_back(point);
    }
    int n = points.size() - 1;

    // Build a cache of all the distances between every combination of points.
    vector<vector<WeightedDistance>> distances(n, vector<WeightedDistance>(n, WeightedDistance(0, 0, 0)));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            distances[i][j] = points[i].weighted_distance_to(points[j]);
        }
    }


    // Build a cache of all the distances from every node to the final node
    vector<WeightedDistance> final_node_distances(n, WeightedDistance(0, 0, 0));
    for (int i = 0; i < n; i++) {
        final_node_distances[i] = points[i].weighted_distance_to(points[points.size() - 1]);
    }


    // Prep the cache 
    vector<vector<WeightedDistance>> shortest_distance_to_end(n, vector<WeightedDistance>(1 << n, WeightedDistance(-1, -1, -1)));
    vector<vector<int>> optimal_next_node(n, vector<int>(1 << n, -1));


    // With a fixed starting point, calculate the shortest distance to all other points
    WeightedDistance shortestPath = shortest_distance(
        0,
        1,
        distances,
        final_node_distances,
        shortest_distance_to_end,
        optimal_next_node
    );

    // Trace through the cache to find the shortest path taken to print out the
    // JSON representation of the path.
    vector<Point> path;
    int current_node = 0;
    int current_visited = 1;

    cout << "{" << endl;
    cout << "    \"walking_distance\": " << shortestPath.walking_distance << "," << endl;
    cout << "    \"teleporting_cost\": " << shortestPath.coin_cost << "," << endl;
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



