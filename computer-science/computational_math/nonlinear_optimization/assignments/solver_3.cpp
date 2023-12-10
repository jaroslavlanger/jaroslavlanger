/*
 * Name:       Linear System Solver
 * Author:     Jaroslav Langer (langeja5@fit.cvut.cz)
 * Date:       2020, Dec. 18th
 *
 * Solution to the third assignment from nonlinear optimization course.
 *
 * The solver is able to store the matrix either as full matrix (2D array n*n)
 * or with the Compressed Row approach.
 *
 * To solve the system it is possible to use either the steepest descent method
 * or the conjugate gradient method.
 */

#include <fstream>      // ofstream ifstream
#include <getopt.h>     // getopt_long
#include <iostream>     // cout
#include <string>       // string
#include <cmath>        // sqrt
#include <iomanip>      // setprecision

using namespace std;

void print_help()
{
    cout <<
        "<matrix_file>:       File with matrix\n"
        "<vector_file>:       File with vector\n"
        "<output_file>:       Output file\n"
        "--method <text>:     Computation method [ sd | cg ]\n"
        "--saving <text>:     Matrix representation approach [ full | cr ]\n"
        "--epsilon <float>:   Residuum threshold for the algorithm stopping\n"
        "--verbose:           Show the task, steps and solution\n"
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
            case 'm':   method = string(optarg);    break;
            case 's':   saving = string(optarg);    break;
            case 'e':   epsilon = stod(optarg);     break;
            case 'v':   verbose = true;             break;
            case 'h':   // -h or --help
            case '?':   // Unrecognized option
            default:    print_help();               break;
        }
    }

    if (argc - optind < 3) {
        cout << "Error: Three positional parameters are required, "
            << (argc - optind) << " were given." << endl;
        return false;
    }
    f_matrix = string(argv[optind++]);
    f_vector = string(argv[optind++]);
    f_output = string(argv[optind++]);

    return true;
}

/* Read 1+n lines from given file, n is read from the first line.
 * Write n rows of n floats to the matrix.*/
bool read_matrix_full(double ***A, int &n, const string &f_matrix)
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

bool read_matrix_compressed_rows(double **A, int **ci, int **adr, int &a_len,
    int &n, const string &f_matrix)
{
    ifstream file; file.open(f_matrix);

    file >> n >> a_len;

    *A = new double [a_len];
    *ci = new int [a_len];
    *adr = new int [n];

    int offset = 0; // if the rows and columns indices does not start with 0.
    int row_idx = 0, row = 0, next_row = 0, col;
    (*adr)[row_idx++] = row;

    for (int i = 0; i < a_len; i++) {
        file >> next_row >> col >> (*A)[i];
        if (i == 0) { offset = next_row; }
        next_row -= offset;
        (*ci)[i] = col - offset;
        if (row != next_row) { (*adr)[row_idx++] = i; row = next_row; }
    }

    file.close();
    return true;
}

// Read vector of a length n from given file.
bool read_vector(double **b, const int n, const string f_vector)
{
    *b = new double [n];

    ifstream file; file.open(f_vector);
    if(! file.is_open()) { return false; }

    for (int i = 0; i < n; i++) { file >> (*b)[i]; }

    file.close();
    return true;
}

void show_matrix_and_vector(const double *const *A, const double *b, const int n)
{
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) { cout << A[i][j] << " "; }
            cout << endl;
    }; cout << endl;
    for (int i = 0; i < n; i++) { cout << b[i] << " "; }; cout << endl;
}

void show_matrix_and_vector(const double *a, const int *ci, const int *adr,
    const int a_len, const int n, const double *b)
{
    for (int i = 0; i < a_len; i++) { cout << a[i] << " "; }; cout << endl << endl;
    for (int i = 0; i < n; i++) { cout << adr[i] << " "; }; cout << endl << endl;

    int row_idx, next_col_idx, next_col;
    for (int i = 0; i < n; i++) {
        row_idx = adr[i];                //# index of the first column at the i-th row
        next_col_idx = row_idx;
        next_col = ci[next_col_idx];     //# next column index at the i-th row
        for (int j = 0; j < n; j++) {
            if (j == next_col) {
                cout << a[next_col_idx] << " ";
                next_col_idx += 1;
                next_col = (next_col_idx < a_len)? ci[next_col_idx]: 0;
            } else {
                cout << "X ";
            }
        }
        cout << endl;
    }
    cout << endl;
    for (int i = 0; i < n; i++) { cout << b[i] << " "; }; cout << endl;
}

void plus_scalar_x_vector(double *it, const double scalar,
    const double *vector, const int n)
{
    for (int i = 0; i < n; i++) { it[i] += scalar * vector[i]; }
}

void minus_scalar_x_vector(double *it, const double scalar,
    const double *vector, const int n)
{
    for (int i = 0; i < n; i++) { it[i] -= scalar * vector[i]; }
}

void x_scalar_plus_vector(double *it, const double scalar,
    const double *vector, const int n)
{
    for (int i = 0; i < n; i++) { it[i] = (it[i] * scalar) + vector[i]; }
}

void next_r_norm_alpha_Ar(double &r_norm, double &alpha, double *Ar,
    const double *r, const double *const *A, const int n)
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
}

void next_r_norm_alpha_Ar(double &r_norm, double &alpha, double *Ar,
    const double *r, const double *a, const int *ci, const int *adr,
    const int a_len, const int n)
{
    double rTr = 0, rTAr = 0;
    for (int i = 0; i < n; i++) { Ar[i] = 0; }

    int row = 0;
    int next_row_idx = adr[row + 1];

    for (int idx = 0; idx < a_len; idx++){
        if (idx == next_row_idx) {
            row += 1;
            next_row_idx = (row + 1 < n)? adr[row + 1]: 0;
        }
        Ar[row] += a[idx] * r[ci[idx]];
    }
    for (int i = 0; i < n; i++) {
        rTr  += r[i]  * r[i];
        rTAr += Ar[i] * r[i];
    }

    r_norm = sqrt(rTr);
    alpha = rTr / rTAr;
}

void steepest_descent(double *x, const double *const *A, const double *b,
    const int n, const double epsilon, const bool verbose)
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
            cout << "step: " << k;
            cout << setprecision(16) << " residuum: " << r_norm << endl;
            break;
        }

        plus_scalar_x_vector(x, alpha, r, n);   // x_{k+1}=x_k+(alpha_k*r_k)
        minus_scalar_x_vector(r, alpha, Ar, n);  // r_{k+1}=r_k-(alpha_k*A*r_k)
        k++;
        if (verbose) {
            cout << "step: " << k << setprecision(16)
                << " residuum: " << r_norm << endl;
        }
    }
    delete[] r; delete[] Ar;
}

void steepest_descent(double *x, const double *a, const int *ci,
    const int *adr, const int a_len, const int n, const double *b,
    const double epsilon, const bool verbose)
{
    int k = 0;
    double *r = new double[n];
    for (int i = 0; i < n; i++) { r[i] = b[i]; }

    double r_norm, alpha, *Ar = new double[n];

    while (true) {
        // r_norm:  || r_k || = sqrt( r_k^T * r_k )
        // alpha:   alpha_k = (A * r_k) / (r_k^T * A * r_k)
        // Ar:      A * r_k
        next_r_norm_alpha_Ar(r_norm, alpha, Ar, r, a, ci, adr, a_len, n);

        if (r_norm < epsilon) {     // || r_k || < epsilon
            cout << "step: " << k;
            cout << setprecision(16) << " residuum: " << r_norm << endl;
            break;
        }

        plus_scalar_x_vector(x, alpha, r, n);   // x_{k+1}=x_k+(alpha_k*r_k)
        minus_scalar_x_vector(r, alpha, Ar, n);  // r_{k+1}=r_k-(alpha_k*A*r_k)
        k++;
        if (verbose) {
            cout << "step: " << k
                << setprecision(16) << " residuum: " << r_norm << endl;
        }
    }
    delete[] r; delete[] Ar;
}

void next_alpha_As(double &alpha, double *As, const double *const *A,
    const double *s, const double &rTr, const int n)
{
    double sTAs = 0;
    for (int i = 0; i < n; i++) { As[i] = 0; }

    for (int i = 0; i < n; i++) {               // iterate over rows
        for (int j = 0; j < n; j++) {           // iterate over columns
            As[i] += A[i][j] * s[j];
        }
        sTAs += As[i] * s[i];
    }
    alpha = rTr / sTAs;
}

void next_alpha_As(double &alpha, double *As, const double *a,
    const int *ci, const int *adr, const int a_len, const int n,
    const double *s, const double &rTr)
{
    double sTAs = 0;
    for (int i = 0; i < n; i++) { As[i] = 0; }

    int row = 0;
    int next_row_idx = adr[row + 1];

    for (int idx = 0; idx < a_len; idx++){
        if (idx == next_row_idx) {
            row += 1;
            next_row_idx = (row + 1 < n)? adr[row + 1]: 0;
        }
        As[row] += a[idx] * s[ci[idx]];
    }
    for (int i = 0; i < n; i++) {
        sTAs += As[i] * s[i];
    }
    alpha = rTr / sTAs;
}

void next_r_norm_beta_rTr(double &r_norm, double &beta, double &rTr,
    const double *r, const int n)
{
    double next_rTr = 0;
    for (int i = 0; i < n; i++) { next_rTr += r[i] * r[i]; }
    r_norm = sqrt(next_rTr);
    beta = next_rTr / rTr;
    rTr = next_rTr;
}

void conjugate_gradient(double *x, const double *const *A, const double *b, 
    const int n, const double epsilon, const bool verbose)
{
    int k = 0;
    double *r = new double[n], *s = new double[n];
    double rTr = 0;
    for (int i = 0; i < n; i++) { r[i] = b[i]; s[i] = b[i]; rTr += r[i]*r[i]; }

    double r_norm, alpha, beta,*As = new double[n];

    while (true) {
        next_alpha_As(alpha, As, A, s, rTr, n);

        plus_scalar_x_vector(x, alpha, s, n);   // x_{k+1} = x_k + alpha_k*s_k
        minus_scalar_x_vector(r, alpha, As, n); // r_{k+1} = r_k + alpha_k*A*s_k

        next_r_norm_beta_rTr(r_norm, beta, rTr, r, n);

        if (r_norm < epsilon) {     // || r_k || < epsilon
            cout << "step: " << k;
            cout << setprecision(16) << " residuum: " << r_norm << endl;
            break;
        }
        x_scalar_plus_vector(s, beta, r, n);

        k++;
        if (verbose) {
            cout << "step: " << k
                << setprecision(16) << " residuum: " << r_norm << endl;
        }
    }
    delete[] r; delete[] s; delete[] As;
}

void conjugate_gradient(double *x, const double *A, const int *ci,
    const int *adr, const int a_len, const int n, const double *b,
    const double epsilon, const bool verbose)
{
    int k = 0;
    double *r = new double[n], *s = new double[n];
    double rTr = 0;
    for (int i = 0; i < n; i++) { r[i] = b[i]; s[i] = b[i]; rTr += r[i]*r[i]; }

    double r_norm, alpha, beta,*As = new double[n];

    while (true) {
        next_alpha_As(alpha, As, A, ci, adr, a_len, n, s, rTr);

        plus_scalar_x_vector(x, alpha, s, n);   // x_{k+1} = x_k + alpha_k*s_k
        minus_scalar_x_vector(r, alpha, As, n); // r_{k+1} = r_k + alpha_k*A*s_k

        next_r_norm_beta_rTr(r_norm, beta, rTr, r, n);

        if (r_norm < epsilon) {     // || r_k || < epsilon
            cout << "step: " << k;
            cout << setprecision(16) << " residuum: " << r_norm << endl;
            break;
        }

        x_scalar_plus_vector(s, beta, r, n);

        k++;
        if (verbose) {
            cout << "step: " << k
                << setprecision(16) << " residuum: " << r_norm << endl;
        }
    }
    delete[] r; delete[] s; delete[] As;
}

bool solve_linear_system_full_matrix(double *x, const double *const *A,
    const double *b, const int n, const string method, double epsilon,
    const bool verbose)
{
    if (method == "sd") {
        steepest_descent(x, A, b, n, epsilon, verbose);
    } else if (method == "cg") {
        conjugate_gradient(x, A, b, n, epsilon, verbose);
    } else {
        cout << "Desired method is not implemented." << endl;
        return false;
    }
    return true;
}

bool solve_linear_system_compressed_rows(double *x, const double *A,
    const int *ci, const int *adr, const int a_len, const int n,
    const double *b, const string method, double epsilon, const bool verbose)
{
    if (method == "sd") {
        steepest_descent(x, A, ci, adr, a_len, n, b, epsilon, verbose);
    } else if (method == "cg") {
        conjugate_gradient(x, A, ci, adr, a_len, n, b, epsilon, verbose);
    } else {
        cout << "Desired method is not implemented." << endl;
        return false;
    }
    return true;
}

int main(int argc, char **argv)
{
    string f_matrix;
    string f_vector;
    string f_output;
    string method  = "cg";      // Conjugate gradient or steepest descent.
    string saving  = "cr";    // Matrix saved as 2D array.
    double epsilon = 0.000001;
    bool   verbose = false;

    if (! read_arguments(argc, argv, f_matrix, f_vector, f_output, method,
            saving, epsilon, verbose)) { return 1; }

    if (verbose) {
        std::cout
             << "method:  " << method << std::endl
             << "saving:  " << saving << std::endl
             << "epsilon: " << epsilon << std::endl
             << "verbose: " << std::boolalpha << verbose << std::endl;
    }
    double **A;                 // Pointer for 2D array matrix
    double *a;                  // Pointer for compressed row matrix
    int n = 0;                  // Number of entries.
    int *ci, *adr, a_len;       // Helper variables for compressed row matrix
    double *b, *x;              // Right-hand side vector and solution vector

    // Read the matrix
    if (saving == "full") {
        if (! read_matrix_full(&A, n, f_matrix)) {
            delete[] A[0]; delete[] A;
            return 1;
        }
    } else if (saving == "cr") {
        if (! read_matrix_compressed_rows(&a, &ci, &adr, a_len, n, f_matrix)) {
            delete[] a; delete[] ci; delete[] adr;
            return 1;
        }
    }
    // Read the right-hand side vector
    if (! read_vector(&b, n, f_vector)) {
        if (saving == "full") {
            delete[] A[0]; delete[] A;
        } else {
            delete[] a; delete[] ci; delete[] adr;
        }
        delete[] b;
        return 1;
    }
    // Show matrix and vector
    if (verbose) {
        if (saving == "full") {
            show_matrix_and_vector(A, b, n);
//        } else if (saving == "cr") {
//            show_matrix_and_vector(a, ci, adr, a_len, n, b); }
        }
    }

    // Initialize vector x with zeros.
    x = new double[n]();    
    
    // Calculate the relative epsilon based on the right-hand side vector
    double b_norm = 0;
    for (int i = 0; i < n; i++) { b_norm += b[i] * b[i]; } 
    epsilon = epsilon * b_norm;
    cout << "residuum threshold: " << epsilon << endl;

    // Solve the linear system
    if (saving == "full") {
        if (! solve_linear_system_full_matrix(
                x, A, b, n, method, epsilon, verbose)) {
            delete[] A[0]; delete[] A; delete[] b; delete[] x;
            return 1;
        }
        delete[] A[0]; delete[] A;
    } else if (saving == "cr") {
        if (! solve_linear_system_compressed_rows(
                x, a, ci, adr, a_len, n, b, method, epsilon, verbose)) {
            delete[] a; delete[] ci; delete[] adr; delete[] b; delete[] x;
            return 1;
        }
        delete[] a; delete[] ci; delete[] adr;
    }

    // Show the solution
//   if (verbose && saving != "rc") {
//       cout << endl << "Solution:" << endl;
//       for (int i = 0; i < n; i++) { cout << x[i] << " "; }
//       cout << endl;
//   }

   ofstream file; file.open(f_output);
   file << setprecision(16);
   for (int i = 0; i < n; i++) { file << x[i] << endl; }; file << endl;
   file.close();

   delete[] b; delete[] x;
   return 0;
}

