// InsertioSort.c

#include "LibrarySort.h"


void LibrarySort( int *arr, int n){
    int epsilon = 1;
    int S[MAX2];
    int sLen, i, x;
    
    prepareLibrarySort(epsilon, n, S, &sLen);
    //O (n log n)
    libSort(arr, n, S, epsilon);
   
    for(i=0, x=0;i<sLen && x<n;i++)
        if(!IS_EMPTY(S[i])) arr[x++] = S[i];
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
           
            while(tmp<last && IS_EMPTY(sorted[tmp])) tmp ++;
            if(sorted[tmp]>e) {
                tmp = middle - 1;
                while(middle>first && IS_EMPTY(sorted[middle])) middle --;
                
                if(sorted[middle]<e)
                    return middle;
                last = middle - 1;
            } else first = tmp + 1;
        } else if(sorted[middle]<e) {
            first = middle + 1;
        } else {
            last = middle - 1;
        }
    }
    
    if(last>=0 && IS_EMPTY(sorted[last])) last --;
    return last;
}
 
void libSort(int A[MAX], int N, int S[MAX2], int EPSILON) {

    if(N==0) return;
 
    int x, z, step;
 
    
    int goal = 1;
    
    int pos = 1;
 
    S[0] = A[0];
 
   
    int sLen = max((1+EPSILON), goal + 1);
 
    
    while(pos<N) {
       
        for(x=0;x<goal;x++) {
            
            int insPos = searchFree(A[pos], S, sLen-1);
 
            
            insPos ++;
            if(!IS_EMPTY(S[insPos])) {
                int nextFree = insPos + 1;
                while(!IS_EMPTY(S[nextFree])) nextFree ++;
                
                if(nextFree>=sLen) {
                    insPos --;
                    if(!IS_EMPTY(S[insPos])) {
                       
                        nextFree = insPos - 1;
                        while(!IS_EMPTY(S[nextFree])) nextFree --;
                        
                        while(nextFree<insPos) {
                            S[nextFree] = S[nextFree+1];
                            nextFree ++;
                        }
                    }
                } else {
                    
                    while(nextFree>insPos) {
                        S[nextFree] = S[nextFree-1];
                        nextFree --;
                    }
                }
                
            } else if(insPos>=sLen) {
                
                insPos --;
                int nextFree = insPos - 1;
                while(!IS_EMPTY(S[nextFree])) nextFree --;
                
                while(nextFree<insPos) {
                    S[nextFree] = S[nextFree+1];
                    nextFree ++;
                }
                
            }
 
            S[insPos] = A[pos ++];
 
            if(pos>=N)
                return;
        }
 
        
        for(x=sLen-1, z=min(goal*(2+2*EPSILON), (1+EPSILON)*N)-1,
                step=(z+1)/(x+1);x>=0;x--, z-=step) {
            S[z] = S[x];
            S[x] = NONE;
        }
 
        
        sLen = min(goal*(2+2*EPSILON), N*(1+EPSILON));
        goal <<= 1;
    }
}

int min(int a, int b){
   return a < b ? a : b; 
}

int max(int a, int b){
   return a > b ? a : b; 
}