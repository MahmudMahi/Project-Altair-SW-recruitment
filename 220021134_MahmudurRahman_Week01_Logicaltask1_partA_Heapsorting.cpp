#include <iostream>
using namespace std;
void heapify(int[], int);
void buildMaxHeap(int heap[], int n);
int main(){
   int  n = 9;
   int heap[9] = {5,7,4,9,3,1,6,3,8};
   buildMaxHeap(heap, n);
   return 0;
}
void buildMaxHeap(int heap[], int n){
   int c, r, t;
   for (int i = 1; i < n; i++) {
      c = i;
      while (c != 0){
         r = (c - 1) / 2;
         if (heap[r] < heap[c]) { // to create MAX heap array
            t = heap[r];
            heap[r] = heap[c];
            heap[c] = t;
         }
         c = r;
      } 
   }
   cout << "Heap array: ";
   for (int i = 0; i < n; i++)
      cout <<heap[i]<<" ";
   heapify(heap, n);
}
void heapify(int heap[], int n){
   int c, root, temp;
   for (int j = n - 1; j >= 0; j--) {
      temp = heap[0];
      heap[0] = heap[j]; // swap max element with rightmost leaf element
      heap[j] = temp;
      root = 0;
      while (c < j){
         c = 2 * root + 1; // left node of root element
         if ((heap[c] < heap[c + 1]) && c < j-1)
            c++;
         if (heap[root]<heap[c] && c<j) { // again rearrange to max heap array
            temp = heap[root];
            heap[root] = heap[c];
            heap[c] = temp;
         }
         root = c;
      } 
   }
   for (int i = 0; i < n; i++)
      cout <<heap[i]<<" ";
}
