#ifndef INSERTIONSORT_FILE
#define INSERTIONSORT_FILE

#define MAX 10000
#define MAX2 20000
 
#define IS_EMPTY(e) (e<0)
#define NONE -1

#include <stdio.h>
#include <math.h>

/*
 * Insertion Sort
 * 
 * @param arr pointer to array of int
 * 
 * @param n size of the array
 * 
 * @return void
 * 
 */
void LibrarySort( int *arr, int n);
void prepareLibrarySort(int epsilon, int n, int S[MAX2], int * sLen);
int searchFree(int e, int sorted[MAX2], int last);
void libSort(int A[MAX], int N, int S[MAX2], int EPSILON);
int min(int a, int b);
int max(int a , int b);

#endif