#include <iostream>
#include <vector>

using namespace std;

struct ITEM {
    int w; // weight
    int v; // value
};

struct PROBLEM {
    int id;                 // ID of the problem
    int n;                  // Number of items
    int W;                  // Weight capacity
    // int V;               // Required total value
    vector<ITEM> items;     // vector of items
    vector<int> val_left;   // sums of values left
    void init_size(int s){
        items = vector<ITEM>(s);
        val_left = vector<int>(s+1);
        val_left[0] = 0;
    };
};

bool read_problem(PROBLEM &p)
{
    int i, w, v;
    if (! (cin >> p.id >> p.n >> p.W))
        return false;
    p.init_size(p.n);
    for (i = 0; i < p.n; i++) {
        cin >> w >> v;
        p.items[i] = ITEM({w, v});
        p.val_left[i+1] = p.val_left[i] + v;
    }
    return true;
}

void write_problem(PROBLEM &p)
{
    // ITEM i;
    cout << p.id << " " << p.n << " " << p.W;
    for (ITEM i : p.items)
        cout << " " << i.w << " " << i.v;
    cout << endl;
}

int main()
{
    PROBLEM problem;

    while (read_problem(problem)) {
        write_problem(problem);
    }

    return 0;
}
