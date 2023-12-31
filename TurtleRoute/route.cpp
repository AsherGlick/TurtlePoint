#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <cmath>
#include <unordered_map>
#include <sstream>
#include <algorithm>

using namespace std;

// TODO we should sanity check that we have actually reached the "end" of a route and not just an unintialized location
const int UNEXPLORED_LOCATION_INDEX = -1;
const int FINAL_LOCATION_INDEX = -2;

////////////////////////////////////////////////////////////////////////////////
// split
//
// A helper function to split a string into a vector of strings based on a
// specified delimiter.
////////////////////////////////////////////////////////////////////////////////
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


////////////////////////////////////////////////////////////////////////////////
// WeightedDistance
//
// A helper class that is used to allow for multiple values to be tracked,
// and each of those values has an infinite weight above the next value when
// it comes to comparisons.
////////////////////////////////////////////////////////////////////////////////
class WeightedDistance {
 public:
    double walking_distance;
    int coin_cost;
    double distance;

    // Default constructor, sets all values to -1 to represent an "unitialized" value of "infinity".
    WeightedDistance() {
        this->walking_distance = -1;
        this->coin_cost = -1;
        this->distance = -1;
    }

    // Constructor that takes in values for all three of the member variables.
    WeightedDistance(double walking_distance, int coin_cost, double distance)
        : walking_distance(walking_distance), coin_cost(coin_cost), distance(distance) {}

    // Constructor that parses values out of a string with each value in the
    // string being separated by a ':' character.
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
        if (this->is_uninitalized()){
            return *this;
        }
        else if (other.is_uninitalized()){
            return other;
        }
        return WeightedDistance(
            walking_distance + other.walking_distance,
            coin_cost + other.coin_cost,
            distance + other.distance
        );
    }

    // Overloaded subtraction operator
    WeightedDistance operator-(const WeightedDistance& other) const {
        if (this->is_uninitalized()){
            return *this;
        }
        else if (other.is_uninitalized()){
            return other;
        }
        return WeightedDistance(
            walking_distance - other.walking_distance,
            coin_cost - other.coin_cost,
            distance - other.distance
        );
    }

    // Overloaded less than operator
    bool operator<(const WeightedDistance& other) const {
        if (this->is_initalized() && other.is_uninitalized()) {
            return true;
        }
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
        if (this->is_uninitalized() && other.is_initalized()) {
            return true;
        }
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

    // Overloaded equality operator
    bool operator==(const WeightedDistance& other) const {
        return (
            walking_distance == other.walking_distance
            && coin_cost == other.coin_cost
            && distance == other.distance
        );
    }

    // Overloaded not equals operator
    bool operator!=(const WeightedDistance& other) const {
        return (
            walking_distance != other.walking_distance
            || coin_cost != other.coin_cost
            || distance != other.distance
        );
    }

    ////////////////////////////////////////////////////////////////////////////
    // is_uninitalized
    //
    // A helper function to easily identify if this weighed distance is in an
    // "invalid" or "uninitialized" psuedo state were all the values are set
    // to -1.
    ////////////////////////////////////////////////////////////////////////////
    bool is_uninitalized() const {
        return coin_cost == -1 && walking_distance == -1 && distance == -1;
    }
    bool is_initalized() const {
        return !this->is_uninitalized();
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
    bool is_optional;
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

    ////////////////////////////////////////////////////////////////////////////
    // distance_to
    //
    // A simple Pythagorean theorem distance between two points algorithm.
    ////////////////////////////////////////////////////////////////////////////
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
    // coordinates are two feet).
    ////////////////////////////////////////////////////////////////////////////
    uint coin_cost(const Point &p) const {
        return 50 * ( 0.78 + max(0.0, 0.0003 * (this->distance_to(p) - 600))) + 100;
    }

    ////////////////////////////////////////////////////////////////////////////
    // to_json
    //
    // Prints out a json string that contains the information we would like to
    // return to the user about this Point.
    ////////////////////////////////////////////////////////////////////////////
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
//
// @param current_node_index
//  The index of the node we are currently on.
// @param visited_nodes_bitflag
//   Bitflag for all of the nodes that have been visited.
// @param optional_nodes_bitflag
//   Bitflag for all of the nodes that are optional.
// @param distances
//   Precomputed distance between every node and every other node.
// @param final_node_distances
//   A vector of weights for every node to the final node.
// @param shortest_distance_to_end
//   A cache of current_node_index + visited_nodes_bitflag to shortest distance
//   to the end. Cache is N*2^N in size.
// @param optimal_next_node
//   The optimal node to achieve the shortest distance stored in shortest_distance_to_end.
////////////////////////////////////////////////////////////////////////////////
WeightedDistance shortest_distance(
    int current_node_index,
    int visited_nodes_bitflag,
    const int optional_nodes_bitflag,
    const vector<vector<WeightedDistance>> &distances,
    const vector<WeightedDistance> &final_node_distances,
    vector<vector<WeightedDistance>> &shortest_distance_to_end,
    vector<vector<int>> &optimal_next_node
) {
    // If this current_node_index + visited_node_bitflag exists in the cache
    // then we have already calculated the minimum distance required to visit
    // all the remaining nodes in the graph from this node. No need to
    // recalculate the value.
    if (shortest_distance_to_end[current_node_index][visited_nodes_bitflag].is_initalized()) {
        return shortest_distance_to_end[current_node_index][visited_nodes_bitflag];
    }
   
    // If the bitflag is full of 1's we have visited every node
    if (visited_nodes_bitflag == (1 << distances.size()) - 1) {
        // Add the distance from this point to the ending point
        optimal_next_node[current_node_index][visited_nodes_bitflag] = FINAL_LOCATION_INDEX;
        return final_node_distances[current_node_index];
    }


    WeightedDistance minDist = WeightedDistance(1e9, 1e9, 1e9);
    int bestNextCity = UNEXPLORED_LOCATION_INDEX;

    // If we have already completed all the required options then set that as the minDist
    if ((visited_nodes_bitflag | optional_nodes_bitflag) == (1 << distances.size()) - 1) {
        minDist = final_node_distances[current_node_index];
        bestNextCity = FINAL_LOCATION_INDEX;
    }

    // For every node index as i
    for (int i = 0; i < distances.size(); i++) {
        // If we are not currently on the node AND we have not visited it yet.
        if (i != current_node_index && !(visited_nodes_bitflag & (1 << i))) {
            WeightedDistance candidateDist = shortest_distance(
                i,
                visited_nodes_bitflag | (1 << i),
                optional_nodes_bitflag,
                distances,
                final_node_distances,
                shortest_distance_to_end,
                optimal_next_node
            ) + distances[current_node_index][i];

            if (candidateDist < minDist) {
                minDist = candidateDist;
                bestNextCity = i;
            }
        }
    }

    shortest_distance_to_end[current_node_index][visited_nodes_bitflag] = minDist;
    optimal_next_node[current_node_index][visited_nodes_bitflag] = bestNextCity;
    return minDist;
}



// Point Flags
// Can the player teleport to this point, effects how the weights to this point are calculated.
const uint32_t CAN_TELEPORT = 0b00000001;
// Is this point optional. Optional points are allowed to be left out of the final paths.
const uint32_t IS_OPTIONAL = 0b00000010;


////////////////////////////////////////////////////////////////////////////////
// Usage: ./route <startx>:<starty>[:<endx>:<endy>] <walk_weight>:<coin_weight> <flags> <id> [<startx>:<starty>[:<endx>:<endy>] <walk_weight>:<coin_weight> <flags> <id>]+
// Usage: ./route <startx>:<starty>[:<endx>:<endy>] <walk_weight>:<coin_weight> <flags> <id> V
//
// startx      - float   -Start x coordinate
// starty      - float   -Start y coordinate
// endx        - float   - end x coordinate
// endy        - float   - end y coordinate
// walk_weight - float   - additional walking weight for visiting the node
// coin_weight - integer - additional coin weight for visiting the node
// flags       - bitflag - Various different options. See Point Flags
// id          - string  - an identifier for the node that is returned in the output
// V           - n/a     - Argument at the end of the command to denote that the
//                         final point should not be treated as a required endpoint
////////////////////////////////////////////////////////////////////////////////
int main(int argc, char* argv[]) {
    vector<Point> points;
    bool any_final_node = false;

    size_t i;
    for (i = 1; i+3 < argc; i+=4){
        Point point;
        point.assign_position_from_string(argv[i+0]);
        point.extra_weight = WeightedDistance(argv[i+1]);
        uint32_t flags = atoi(argv[i+2]);
        point.id = argv[i+3];

        // Set Flags
        point.can_waypoint_teleport_to = flags & CAN_TELEPORT;
        point.is_optional = flags & IS_OPTIONAL;

        points.push_back(point);
    }
    if (argc == i) {}
    else if (argc == i+1) {
        if (argv[i][0] == 'V') {
            any_final_node = true;
            points.push_back(Point());
        }
    }
    else {
        cout << "Invalid argument count" << endl;
    }

    int n = points.size() - 1;

    // Build a cache of all the distances between every combination of points.
    vector<vector<WeightedDistance>> distances(n, vector<WeightedDistance>(n, WeightedDistance()));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            distances[i][j] = points[i].weighted_distance_to(points[j]);
        }
    }


    // Build a cache of all the distances from every node to the final node
    vector<WeightedDistance> final_node_distances(n, WeightedDistance());
    for (int i = 0; i < n; i++) {
        if (any_final_node) {
            final_node_distances[i] = WeightedDistance(0, 0, 0);
        }
        else {
            final_node_distances[i] = points[i].weighted_distance_to(points[points.size() - 1]);
        }
    }

    // Build the bitflag of the optional nodes
    unsigned int optional_bitflag = 0;
    for (int i = 0; i < n; i++) {
        if (points[i].is_optional){
            optional_bitflag |= (1<<i);
        }
    }

    // Prep the cache 
    vector<vector<WeightedDistance>> shortest_distance_to_end(n, vector<WeightedDistance>(1 << n, WeightedDistance()));
    vector<vector<int>> optimal_next_node(n, vector<int>(1 << n, UNEXPLORED_LOCATION_INDEX));


    // With a fixed starting point, calculate the shortest distance to all other points
    WeightedDistance shortestPath = shortest_distance(
        0,
        1,
        optional_bitflag,
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
        if (current_node == UNEXPLORED_LOCATION_INDEX) {
            cout << "===" << endl;
            cout << "We have a problem: We encountered an unexplored index when tracing the path." << endl;
            cout << "===" << endl;
            return 7;
        }
        else if (current_node == FINAL_LOCATION_INDEX) {
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
