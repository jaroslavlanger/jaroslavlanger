#include <vector>
#include <string>
#include <iostream>
#include <chrono>
#include <algorithm>
#include <iterator>
#include <numeric>
#include <cmath>

using namespace std;

enum APPROACH {
    BF=1,       // Brute Force
    BAB=2,      // Branch and Bound
    DP=3,       // Dynamic Programming
    GH=4,       // Greedy Heuristic
    REDUX=5,    // REDUX
    FPTAS=6     // FPTAS
};

struct Item {
    int i; // original index
    int w; // weight
    int v; // value
};

struct Problem {
    int id;                 // ID of the problem
    int n;                  // Number of items
    int W;                  // Weight capacity
    // int V;               // Required total value
    vector<Item> items;     // vector of items
    vector<int> val_left;   // sums of values left
    void init_size(int s){
        items = vector<Item>(s);
        val_left = vector<int>(s+1);
        val_left[0] = 0;
    };
};

struct State {
    int i; // index of the state item
    int w; // total weight of the state
    int v; // total value of the state
    int p; // previous weight or value
};

struct Result {
    int max_value;                      // value of items
    vector<bool> solution;              // boolean choice of every item
    vector<bool> sol_tmp;               // temporary vector of boolean solution
    unsigned long long int complexity;  // number of called recursion tails
    double seconds;                     // number of computation seconds
};

/**
 * item | states 1-15 (example n = 3)
 * 3    |              1                | 2^0 = 1 | log2(1) = 0
 * 2    |       2            3          | 2^1 = 2 | log2(2) = 1
 * 1    |    4     5      6      7      | 2^2 = 4 | log2(4) = 2
 * 0    |  8  9  10 11  12 13  14 15    | 2^3 = 8 | log2(8) = 3
 */
void solution_from_node(State & max_node, Problem & prob, Result & resu)
{
    resu.max_value = max_node.v;
    int node = max_node.i;

    for (int i = 0; i < prob.n; i++) {
        resu.solution[i] = (node %2 == 1)? true: false;
        node = node/2;
    }
}

void brute_force(Problem & prob, Result & resu)
{
    int n = prob.n;
    int max_state_num = pow(2, n)-1;

    vector<State> sts(max_state_num+1); // +1 is because it will be indexed from 1
    sts[1] = State({1, 0, 0, 0});

    State max = State({0, 0, 0, 0});

    int i, lvl, idx;
    for (i = 1; i <= max_state_num; i++) {
        lvl = (int)log2(i)+1;
        idx = n-lvl;
        if (idx > 0) {
            sts[i*2] = {idx, sts[i].w, sts[i].v, i};
            sts[i*2+1] = {idx, sts[i].w+prob.items[idx].w, sts[i].v+prob.items[idx].v, i};
        } else {
            if (sts[i].w <= prob.W && sts[i].v > max.v)
                max = State({i*2, sts[i].w, sts[i].v, i});
            if (sts[i].w+prob.items[idx].w <= prob.W && sts[i].v+prob.items[idx].v > max.v)
                max = State({i*2+1, sts[i].w+prob.items[idx].w, sts[i].v+prob.items[idx].v, i});
        }
    }
    solution_from_node(max, prob, resu);
}

// void branch_and_bound(Problem &prob, Result &resu)
// {
    // vector<bool> solution;
    // vector<State> stack = ; //, next_indices;
    
    // vector<State> candidates; // vector<int> * next = & curr_indices, * curr = & next_indices;
    // State st;
// }

void trace_back(Problem &prob, Result &resu, vector<vector<State>> &dp)
{
    int w = prob.W;
    int i;
    for (i = 0; i < prob.n; i++) {
        if (dp[i][w].w == dp[i][w].p) {
            resu.solution[i] = false;
            // w = dp[i][w].w;
        } else {
            resu.solution[i] = true;
            w = dp[i][w].p; // dp[i][w].w - prob.items[i].w;
        }
    }
}

void dynamic_programming(Problem &prob, Result &resu)
{
    int i, j;
    vector<vector<State>> dp(prob.n+1, vector<State>(prob.W+1));
    vector<State> choices;
    for (i = prob.n; i >= 0; i--) {
        for (j = 0; j <= prob.W; j++) {
            if (i == prob.n) {
                dp[i][j] = State({i, 0, 0, 0}); // = 0;
            } else {
                choices = vector<State>();
                choices.push_back({i, dp[i+1][j].w, dp[i+1][j].v, dp[i+1][j].w}); // dp[i+1][j]
                if (j >= prob.items[i].w) {
                    choices.push_back({i, dp[i+1][j-prob.items[i].w].w+prob.items[i].w,
                        dp[i+1][j-prob.items[i].w].v+prob.items[i].v, dp[i+1][j-prob.items[i].w].w});
                }
                auto max_st = max_element(choices.begin(), choices.end(),
                    [] (const State &ls, const State &rs) {return ls.v < rs.v;});
                dp[i][j] = *max_st;
            }
        }
    }
    trace_back(prob, resu, dp);
    resu.max_value = dp[0][prob.W].v;
}

bool cmp_value_per_weight(Item i1, Item i2) 
{ 
    return ((float)i1.v/i1.w >= (float)i2.v/i2.w);
}

void greedy_heuristic(Problem &prob, Result &resu)
{
    sort(prob.items.begin(), prob.items.end(), cmp_value_per_weight);
    int i;
    State st = {0, 0, 0, 0};
    for (i = 0; i < prob.n; i++) {
        if (st.w + prob.items[i].w <= prob.W) {
            st.w += prob.items[i].w;
            st.v += prob.items[i].v;
            resu.solution[prob.items[i].i] = true;
        } else {
            resu.solution[prob.items[i].i] = false;
        }
    }
    resu.max_value = st.v;
}

void get_most_valuable_item(Problem & prob, Item & item)
{
    auto max_item = max_element(prob.items.begin(), prob.items.end(),
         [] (const Item &i1, const Item &i2) {return i1.v < i2.v;});
    item = max_item[0];
}

void redux(Problem &prob, Result &resu)
{
    greedy_heuristic(prob, resu);
    
    Problem problem;
    copy_if(prob.items.begin(), prob.items.end(), back_inserter(problem.items),
        [prob] (Item i) { return i.w <= prob.W; });

    if (problem.items.empty()) return;

    auto max_item = max_element(problem.items.begin(), problem.items.end(),
         [] (const Item &i1, const Item &i2) {return i1.v < i2.v;});

    if (max_item[0].v <= resu.max_value) return;

    resu.max_value = max_item[0].v;
    resu.solution = vector<bool>(prob.n);
    resu.solution[max_item[0].i] = true;
}

int filter_items(Problem &prob)
{
    // Remove items heavier than prob.W
    prob.items.erase(
        remove_if(prob.items.begin(), prob.items.end(),
            [prob] (Item i) { return i.w > prob.W; }), prob.items.end()
    );
    return prob.items.size();
}

int sum_item_values(Problem &prob)
{
    // Get total value, of items that passed the fillter
    return accumulate(prob.items.begin(), prob.items.end(), 0,
        [prob] (int sum, const Item &item) { return sum + item.v; }
    );
}

double calculate_k(Problem & prob, int & n, double epsilon)
{
    Item max_item;
    get_most_valuable_item(prob, max_item);
    return ((epsilon*max_item.v) > n)? (epsilon*max_item.v)/n: 1;
}

void get_most_valuable_state(vector<vector<State>> & dp, Result & resu)
{
    auto max_st = max_element(dp[0].begin(), dp[0].end(),
        [] (const State &ls, const State &rs) {return ls.v < rs.v;});
    resu.max_value = max_st[0].v;
}

void trace_back_solution_by_value(Problem & prob, Result & resu, vector<vector<State>> & dp, double & K)
{
    int value = resu.max_value/K;
    unsigned int i;
    for (i = 0; i < prob.items.size(); i++) {
        if (dp[i][value].v == dp[i][value].p) {
            resu.solution[prob.items[i].i] = false; // w = dp[i][w].w;
        } else {
            resu.solution[prob.items[i].i] = true; // resu.solution[dp[i][value].i] = true;
            value = dp[i][value].p/K; // dp[i][w].w - prob.items[i].w;
        }
    }
}

void fptas(Problem &prob, Result &resu, double epsilon)
{
    int n = filter_items(prob);
    if (! (n > 0)) return; // Return if all the items are heavier than knapsack capacity

    int value_sum = sum_item_values(prob);
    double K = calculate_k(prob, n, epsilon);
    value_sum = value_sum/K;

    vector<vector<State>> dp(n+1, vector<State>(value_sum+1, State({0,0,0,0})));
    vector<int> curr_indices = {0}, next_indices;
    vector<int> * next = & curr_indices, * curr = & next_indices;

    int i, j, weight, value;
    for (i = n; i >= 0; i--) {
        swap(curr, next);

        while(! curr->empty()) {
            j = curr->back();
            next->push_back(j);
            curr->pop_back();

            if (i == n) {
                dp[i][j] = State({0,0,0,0}); // = 0;
            } else {
                if (dp[i][j].w > dp[i+1][j].w || dp[i][j].w == 0) {
                    dp[i][j] = State({i, dp[i+1][j].w, dp[i+1][j].v, dp[i+1][j].v});
                }
                weight = dp[i+1][j].w + prob.items[i].w;
                value = (dp[i+1][j].v + prob.items[i].v)/K;
                if (weight <= prob.W && value <= value_sum) {
                    if (dp[i][value].w > weight || dp[i][value].w == 0) {
                        dp[i][value] = State({i, weight, (dp[i+1][j].v + prob.items[i].v), dp[i+1][j].v});
                    }
                    next->push_back(value);
                }
            }
        }
    }
    get_most_valuable_state(dp, resu);
    trace_back_solution_by_value(prob, resu, dp, K);
}

bool read_problem(Problem &p)
{
    int i, w, v;
    if (! (cin >> p.id >> p.n >> p.W))
        return false;
    p.init_size(p.n);
    for (i = 0; i < p.n; i++) {
        cin >> w >> v;
        p.items[i] = Item({i, w, v});
        p.val_left[i+1] = p.val_left[i] + v;
    }
    return true;
}

void write_result(Problem &p, Result &r)
{
    cout << p.id << " " << p.n << " " << r.max_value << " ";
    for (int i : r.solution)
        cout << i << " ";
    cout << r.seconds << endl;
}

int main(int argc, char **argv)
{
    // Approach is expected as a number 1-6, epsilon in case of fptas method
    // if (argc < 2) { cout << "Error: Approach was not specified." << endl; return 1; }
    // APPROACH approach = (APPROACH)stoi(argv[1]);
    APPROACH approach = BF;
    double epsilon = (argc == 3)? stod(argv[2]): 0;

    Problem problem;
    Result result;

    while (read_problem(problem)) {
        result = Result({0, vector<bool>(problem.n, false), vector<bool>(problem.n), 0, 0});

        auto start = std::chrono::steady_clock::now();
        switch (approach) {
            case BF:    brute_force(problem, result);               break;
            case BAB:
                // branch_and_bound(problem, result);
                break;
            case DP:    dynamic_programming(problem, result);       break;
            case GH:    greedy_heuristic(problem, result);          break;
            case REDUX: redux(problem, result);                     break;
            case FPTAS: fptas(problem, result, epsilon);            break;
            default:    cout << "Error: Approach does not exist";   return 1;
        }
        auto end = chrono::steady_clock::now();
        result.seconds = ((chrono::duration<double>)(end-start)).count();

        write_result(problem, result);
    }
    return 0;
}
