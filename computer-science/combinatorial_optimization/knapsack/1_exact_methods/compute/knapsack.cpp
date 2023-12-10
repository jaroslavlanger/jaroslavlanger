#include <iostream>
#include <fstream>
#include <chrono>
#include <cassert>
#include <bits/stdc++.h> 
#include "knapsack.h"

using namespace std;


struct Item
{ 
    int w, v; 
}; 
  
bool compareItems(Item i1, Item i2) 
{ 
    // return (i1.v >= i2.v);
    // return (i1.v*i1.w >= i2.v*i2.w);
    // return (i1.w >= i2.w);
    return ((double) i1.v/i1.w >= (double)i2.v/i2.w);
} 


void showProblem(int n, int m, int b, int *wgts, int *vals)
{
    cout << "Number: " << n << ", Max weight: " << m << ", Boundary value: " << b << endl;
    int i = 0;
    for (i = 0; i < n; i++)
        cout << wgts[i] << ", " << vals[i] << endl;
}

void showDecision(bool decision, int n, int *wgts, int *vals, bool *solution)
{
    cout << decision << "\t";
    int value = 0;
    int i;
    for (i = 0; i < n; i++)
        value += vals[i] * solution[i];
    cout << value << "\t";
    for (i = 0; i < n; i++)
        (i < n - 1)? cout << solution[i] << " ": cout << solution[i] << endl;
}

void writeDecision(ofstream *f_out, int id, int n, bool decision, Item* items, 
    bool *solution, int complexity, double seconds)
{
    int value = 0;
    int i;
    for (i = 0; i < n; i++)
        value += items[i].v * solution[i];
    
    *f_out << id << " " << n << " " << decision << " " << value << " ";
    for (i = 0; i < n; i++)
        *f_out << solution[i] << " ";
    *f_out << complexity << " " << seconds << endl;
}

/**
 * Decide the knapsack problem.
 *
 * @param sol One particular solution of the problem.
 * @param n Number of items.
 * @param m Maximum weight.
 * @param b Boundary condition of minimal value for success.
 * @param wght Array of weights.
 * @param vals Array of values.
 * @return True if there is a solution that fits the boundary value.
 */
bool branch_and_bound(bool *sol, unsigned long long int &cmx, int wgt, int val, int *values_left, int idx, int n, int m,
    int b, Item *items)
{
    cmx++;
    if (wgt > m || val + values_left[idx] < b) {
        return false;
    } else if (val >= b) {
        return true;
    } else if (idx > n - 1) {
        return false;
    }
    cmx--;

    int i;
    bool put;
    for (i = 1; i >= 0; i--) {
        put = (bool)i;
        sol[idx] = put;
        if (branch_and_bound(sol, cmx, wgt + items[idx].w * put, val + items[idx].v * put, values_left, idx+1, n, m, b, items)) {
            return true;
        }
    }
    return false;
}

bool brute_force(bool *sol, bool *tmp, unsigned long long int &cmx, int wgt, int val, int idx,
    int n, int m, int b, Item *items)
{
    if (idx > n - 1) {
        cmx++;
        return (wgt <= m && val >= b)? true: false;
    }
    bool keep;
    bool *ptr;
    keep = (brute_force(sol, tmp, cmx, wgt + items[idx].w, val + items[idx].v, idx+1, n, m, b, items));
    ptr = (keep)? tmp: sol;

    if (brute_force(ptr, tmp, cmx, wgt, val, idx+1, n, m, b, items) || keep)
        return true;
    return false;
}


double solve(int method, const char *file_in, const char *file_out)
{
    int id, n, m, b;
    Item *items;
    int i;
    bool *solution, *temporary;
    unsigned long long int complexity;
    double seconds;
    bool decision;
    int total_value = 0;
    int *values_left;

    ifstream f_in;
    f_in.open(file_in);
    // assert(("Input file was not possible to open", f_in.fail() == false));
    ofstream f_out;
    f_out.open(file_out);
    // assert(("Output file was not possible to create", f_out.fail() == false));

    while (f_in >> id >> n >> m >> b) {
        auto start = std::chrono::steady_clock::now();
        items = new Item [n];
        // weights = new int [n];
        // values = new int [n];
        for (i = 0; i < n; i++) {
            f_in >> items[i].w >> items[i].v;
            total_value += items[i].v;
        }
        solution = new bool[n]();
        complexity = 0;

        switch (method) {
        case 0:
            temporary = new bool[n];

            decision = brute_force(solution, temporary, complexity, 0, 0, 0, n, m, b, items);

            delete[] temporary;
            break;
        case 1:
            values_left = new int[n];
            for (i = 0; i < n; i++) {
                values_left[i] = (i == 0)? total_value: values_left[i - 1] - items[i - 1].v;
            }

            decision = branch_and_bound(solution, complexity, 0, 0, values_left, 0, n, m, b, items);
            
            delete[] values_left;
            break; //optional
        case 2:
            int size = sizeof(items)/sizeof(items[0]); 
            sort(items, items+n, compareItems);
            // sort the intervals in increasing order of 
            // start time 
            values_left = new int[n];
            for (i = 0; i < n; i++) {
                values_left[i] = (i == 0)? total_value: values_left[i - 1] - items[i - 1].v;
            }

            decision = branch_and_bound(solution, complexity, 0, 0, values_left, 0, n, m, b, items);
            
            delete[] values_left;
            break; //optional
        }

        auto end = std::chrono::steady_clock::now();
        std::chrono::duration<double> elapsed_seconds = end-start;
        seconds = elapsed_seconds.count();
        writeDecision(&f_out, id, n, decision, items, solution, complexity, seconds);
        delete[] items;
        delete[] solution;
    }
    f_in.close();
    f_out.close();
    return 0;
}

int main()
{
    // return (int) solve(1, "../data/nr/NR15_inst.dat", "./test_here.txt");
    return (int) solve(1, "./tests/in_10_28.txt", "./test_here.txt");
}