#ifndef TESTHEAP_FILE
#define TESTHEAP_FILE

 
static void max_heapify( int *arr, int i, int hs);

static void min_heapify( int *arr, int i, int hs);

static int _left_child(int i);

static int _right_child(int i);

static void build_max_heap(int *arr, int len);

static void build_min_heap(int *arr, int len);



#endif
