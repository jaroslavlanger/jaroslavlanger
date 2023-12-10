/*
 * Name:       Linear System Solver
 * Author:     Jaroslav Langer (langeja5@fit.cvut.cz)
 * Date:       2020, Dec. 16th
 *
 * Solution to the first assignment from nonlinear optimization course.
 */

#include <fstream>      // ofstream ifstream
#include <getopt.h>     // getopt_long
#include <iostream>     // cout
#include <string>       // string
#include <cmath>        // sqrt
#include <iomanip>      // setprecision

using namespace std;

// Read 1+n lines from given file, n is read from the first line.
// Write n rows of n floats to the matrix.
bool read_matrix(double ***A, int &n, string &f_matrix)
{
    ifstream file; file.open(f_matrix);

    file >> n;

    double *A1d = new double [n * n];
    for (int i = 0; i < n*n; i++) { file >> A1d[i]; }

    file.close();

    *A = new double *[n];
    for (int i = 0; i < n; i++) { (*A)[i] = &(A1d[i * n]); }
    return true;
}

// Read vector of a length n from given file.
bool read_vector(double **b, int n, string f_vector)
{
    *b = new double [n];

    ifstream file; file.open(f_vector);

    for (int i = 0; i < n; i++) { file >> (*b)[i]; }

    file.close();

    return true;
}

bool next_r_norm_alpha_Ar(double &r_norm, double &alpha, double *Ar, double *r,
    double **A, int n)
{
    double rTr = 0, rTAr = 0;
    for (int i = 0; i < n; i++) { Ar[i] = 0; }

    for (int i = 0; i < n; i++) {               // iterate over rows
        for (int j = 0; j < n; j++) {           // iterate over columns
            Ar[i] += A[i][j] * r[j];
        }
        rTr  += r[i]  * r[i];
        rTAr += Ar[i] * r[i];
    }
    r_norm = sqrt(rTr);
    alpha = rTr / rTAr;

    return true;
}

void next_x(double *x, const double &alpha, double *r, const int n)
{
    for (int i = 0; i < n; i++) { x[i] += alpha * r[i]; }
}

void next_r(double *r, const double &alpha, double *Ar, const int n)
{
    for (int i = 0; i < n; i++) { r[i] -= alpha * Ar[i]; }
}

bool gradient_descent(double **A, double *b, double *x, int n, double epsilon,
    bool verbose)
{
    int k = 0;
    double *r = new double[n];
    for (int i = 0; i < n; i++) { r[i] = b[i]; }

    double r_norm, alpha, *Ar = new double[n];

    while (true) {
        // r_norm:  || r_k || = sqrt( r_k^T * r_k )
        // alpha:   alpha_k = (A * r_k) / (r_k^T * A * r_k)
        // Ar:      A * r_k
        next_r_norm_alpha_Ar(r_norm, alpha, Ar, r, A, n);

        if (r_norm < epsilon) {     // || r_k || < epsilon
            cout << setprecision(16) << r_norm << endl;
            break;
        }

        next_x(x, alpha, r, n);     // x_{k+1} = x_k + (alpha_k * r_k)
        next_r(r, alpha, Ar, n);    // r_{k+1} = r_k - (alpha_k * A * r_k)

        if (verbose)
            cout << "step: " << k++ << " residuum: " << r_norm << endl;
    }
    delete[] r; delete[] Ar;
    return true;
}

void print_help()
{
    cout <<
        "<matrix_file>:       File with matrix\n"
        "<vector_file>:       File with vector\n"
        "<output_file>:       File to write output\n"
        "--method <text>:     Computation method [full |]\n"
        "--saving <text>:     Matrix representation approach [full |]\n"
        "--epsilon <float>:   Residuum threshold for the algorithm stopping\n"
        "--verbose:           Show the task, steps and solution.\n"
        "--help:              Show help\n";
    exit(1);
}

bool read_arguments(int argc, char** argv, string &f_matrix,
    string &f_vector, string &f_output, string &method, string &saving,
    double &epsilon, bool &verbose)
{
    const char* const short_opts = "m:s:e:vh";
    const option long_opts[] = {
        {"method", required_argument, nullptr, 'm'},
        {"saving", required_argument, nullptr, 's'},
        {"epsilon", required_argument, nullptr, 'e'},
        {"verbose", no_argument, nullptr, 'v'},
        {"help", no_argument, nullptr, 'h'},
        {nullptr, no_argument, nullptr, 0}
    };

    while (true) {
        const auto opt = getopt_long(argc, argv, short_opts, long_opts, nullptr);

        if (-1 == opt) break;

        switch (opt) {
        case 'm':
            method = string(optarg);
            cout << "Method set to: " << method << endl;
            break;
        case 's':
            saving = string(optarg);
            cout << "Saving set to: " << saving << endl;
            break;
        case 'e':
            epsilon = stod(optarg);
            cout << "Epsilon set to: " << epsilon << endl;
            break;
        case 'v':
            verbose = true;
            std::cout << "Verbose set to true" << std::endl;
            break;
        case 'h': // -h or --help
        case '?': // Unrecognized option
        default:
            print_help();
            break;
        }
    }

    if (argc - optind < 3) {
        cout << "Error: Three positional parameters are required, ";
        cout << (argc - optind) << " were given." << endl;
        return false;
    }
    f_matrix = string(argv[optind++]);
    f_vector = string(argv[optind++]);
    f_output = string(argv[optind++]);

    return true;
}

int main(int argc, char **argv)
{
    string f_matrix;
    string f_vector;
    string f_output;
    string method  = "gd";      // Gradient descent method.
    string saving  = "full";    // Matrix saved as 2D array.
    double epsilon = 0.00001;
    bool   verbose = false;

    if (! read_arguments(argc, argv, f_matrix, f_vector, f_output, method,
            saving, epsilon, verbose)) { return 1; }

    int n = 0;                  // Number of entries.
    double **A, *b, *x;

    if (saving == "full") {
        read_matrix(&A, n, f_matrix);
        read_vector(&b, n, f_vector);
    }

    if (verbose) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) { cout << A[i][j] << " "; }
            cout << endl;
        }; cout << endl;
        for (int i = 0; i < n; i++) { cout << b[i] << " "; }; cout << endl;
    }

    if (method == "gd") {
        x = new double[n]();    // Initialize vector x
        gradient_descent(A, b, x, n, epsilon, verbose);
    }

    if (verbose) {
        cout << endl << "solution:" << endl;
        for (int i = 0; i < n; i++) { cout << x[i] << " "; }
        cout << endl;
    }

    ofstream file; file.open(f_output);
    file << setprecision(16);
    for (int i = 0; i < n; i++) { file << x[i] << endl; }; file << endl;
    file.close();

    delete[] A[0]; delete[] A; delete[] b; delete[] x;

    return 0;
}

