// InsertioSort.c

#include "LibrarySort.h"


void LibrarySort( int *arr, int n){
    int epsilon = 1;
    int S[MAX2];
    int sLen, i, j;
    //This takes linear time
    prepareLibrarySort(epsilon, n, S, &sLen);
    //O (n log n)
    libSort(arr, n, S, epsilon);
    //This takes linear time
    for(i=0, j=0;i<sLen && j<n;i++)
        if(!IS_EMPTY(S[i])) arr[j++] = S[i];
}

 
void prepareLibrarySort(int epsilon, int n, int S[MAX2], int * sLen) {
    int i;
    *sLen = (1+epsilon)*n;
    for(i=0;i<*sLen;i++) S[i] = NONE;
}
 
int searchFree(int e, int sorted[MAX2], int last) {
    int first = 0;
    int middle;
 
    while(last>=0 && IS_EMPTY(sorted[last])) last --;
    while(first<=last && IS_EMPTY(sorted[first])) first ++;
    while(first<=last) {
        middle = (first+last)/2;
        if(IS_EMPTY(sorted[middle])) {
            int tmp = middle + 1;
            //Look to the right
            while(tmp<last && IS_EMPTY(sorted[tmp])) tmp ++;
            if(sorted[tmp]>e) {
                tmp = middle - 1;
                while(middle>first && IS_EMPTY(sorted[middle])) middle --;
                //Look to the left
                if(sorted[middle]<e)//Found intermediate position
                    return middle;
                last = middle - 1;
            } else first = tmp + 1;
        } else if(sorted[middle]<e) {
            first = middle + 1;
        } else {
            last = middle - 1;
        }
    }
    //If no position was found return -1 or if a lower position was found, return that
    if(last>=0 && IS_EMPTY(sorted[last])) last --;
    return last;
}
 
void libSort(int A[MAX], int N, int S[MAX2], int EPSILON) {

    if(N==0) return;
 
    int j, k, step;
 
    // ------ BASE CASE ------
    //Goal: We want 'goal' elements to be inserted into S, for now..
    int goal = 1;
    //How many elements have already been inserted, its 1 for efficiency
    int pos = 1;
 
    S[0] = A[0];//We insert element 0 at position 0
 
    //Initial size of array S
    int sLen = max((1+EPSILON), goal + 1);
 
    // ------ CONDITION -------
    //What has already been read must be less than the total array size
    while(pos<N) {
        // ------ ROUND ------
        //Each round i will end with goal=2^i sorted elements. i starts with 1
        for(j=0;j<goal;j++) {
            //Search where to insert A[pos] (with binary search)
            int insPos = searchFree(A[pos], S, sLen-1);
 
            //Because our binary search returns us the location of an smaller item than the one we search...
            insPos ++;
            if(!IS_EMPTY(S[insPos])) {//There is no place where we wanted to insert that element
                int nextFree = insPos + 1;//Search a free space forward
                while(!IS_EMPTY(S[nextFree])) nextFree ++;
                //At 'nextFree' there is a place, translate all elements one position to the right
                if(nextFree>=sLen) {//Wait! nextFree is out of bounds
                    insPos --;
                    if(!IS_EMPTY(S[insPos])) {
                        //Search backward
                        nextFree = insPos - 1;
                        while(!IS_EMPTY(S[nextFree])) nextFree --;
                        //Now we translate all the elements to the left
                        while(nextFree<insPos) {
                            S[nextFree] = S[nextFree+1];
                            nextFree ++;
                        }
                    }
                } else {
                    //Now we translate all the elements to the right
                    while(nextFree>insPos) {
                        S[nextFree] = S[nextFree-1];
                        nextFree --;
                    }
                }
                //Now nextFree is insPos; in other words, insPos is free
            } else if(insPos>=sLen) {//insPos is out of bounds
                //Search a free space backwards
                insPos --;//This place must be between the limits
                int nextFree = insPos - 1;
                while(!IS_EMPTY(S[nextFree])) nextFree --;
                //Now we translate all the elements to the left
                while(nextFree<insPos) {
                    S[nextFree] = S[nextFree+1];
                    nextFree ++;
                }
                //Now nextFree is insPos; in other words insPos is free
            }
 
            S[insPos] = A[pos ++];//We insert the element and increment our counter
 
            if(pos>=N)
                return;//That element was the last, return from the function
        }
 
        // ----- REBALANCE -----
        //It takes linear time. Tries to spread the elements as much as possible
        for(j=sLen-1, k=min(goal*(2+2*EPSILON), (1+EPSILON)*N)-1,
                step=(k+1)/(j+1);j>=0;j--, k-=step) {
            S[k] = S[j];
            S[j] = NONE;
        }
 
        //In each round insert the double of elements to the sorted array
        // because there will be the double of free spaces after the rebalance
        sLen = min(goal*(2+2*EPSILON), N*(1+EPSILON));
        goal <<= 1;//We increment i
    }
}

int min(int a, int b){
   return a < b ? a : b; 
}

int max(int a, int b){
   return a > b ? a : b; 
}