#include <vector>
#include <string>
#include <iostream>
#include <chrono>
#include <algorithm>
#include <iterator>
#include <numeric>

using namespace std;

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

void trace_back(Problem &prob, Result &resu, vector<vector<State>> &dp)
{
    int w = prob.W;
    int i;
    for (i = 0; i < prob.n; i++) {
        if (dp[i][w].w == dp[i][w].p) {
            resu.solution.push_back(false);
            // w = dp[i][w].w;
        } else {
            resu.solution.push_back(true);
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
        // cout << "v/w: " << ((float) prob.items[i].v / prob.items[i].w);
        // cout << " (value/weight: " << prob.items[i].v << "/" << prob.items[i].w << ")" << endl;
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
    copy_if(prob.items.begin(), prob.items.end(),
        back_inserter(problem.items),
        [prob] (Item i) { return i.w <= prob.W; });

    // for (auto item: problem.items)
    //     cout << "Item: weight = " << item.w << ", value = " << item.v << endl;

    auto max_item = max_element(problem.items.begin(), problem.items.end(),
         [] (const Item &i1, const Item &i2) {return i1.v < i2.v;});

    // cout << "Max Item: weight = " << max_item[0].w << " , value = " << max_item[0].v << endl;

    if (max_item[0].v > resu.max_value) {
        resu.max_value = max_item[0].v;
        resu.solution = vector<bool>(prob.n);
        resu.solution[max_item[0].i] = true;
    }
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
    cout << endl;
}

int main()
{
    Problem problem;
    Result result;

    while (read_problem(problem)) {
        result = Result({0, vector<bool>(problem.n, false), vector<bool>(problem.n), 0, 0});
        
        // auto start = std::chrono::steady_clock::now();
        // dynamic_programming(problem, state, result);
        // dynamic_programming(problem, result);
        // greedy_heuristic(problem, result);
        // redux(problem, result);
        fptas(problem, result, 0);
        // auto end = std::chrono::steady_clock::now();
        // result.seconds = (end-start).count();

        write_result(problem, result);
    }
    return 0;
}
