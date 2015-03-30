/*
* QuickSort in C
* by Marshall Ehlinger
* for Algorithms Spring 2015
* Main method sorts a test array of integers
*/

#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int firstIndex, int secondIndex) {
	int temp;
	temp = a[firstIndex];
	a[firstIndex] = a[secondIndex];
	a[secondIndex] = temp;
}

int partition(int *a, int lo, int hi) {
	int pivot = a[hi];
	int i;

	for (i = lo; i < hi; i++) {
		if (a[i] <= pivot) {
			swap(a, i, lo);
			lo++;
		}
	}
	swap(a, lo, hi);
	return lo;
}

void quickSort(int *a, int lo, int hi) {
	int pivot;
	if (lo < hi) {
		pivot = partition(a, lo, hi);
		quickSort(a, lo, pivot-1);
		quickSort(a, pivot+1, hi);
	}
}

void printArray(int a[], int arrayLen) {
	int i;
	for (i = 0; i < arrayLen; i++) {
		printf("%d ", a[i]);
	}
	printf("\n");
}

/////////////////
//     MAIN    //
/////////////////
int main() {
	int array[] = {2, 3, 5, 22, 1, 15, 4};
	int arrayLen = sizeof(array) / sizeof(array[0]);

	printArray(array, arrayLen);
	
	quickSort(array, 0, arrayLen-1);

	printArray(array, arrayLen);

}