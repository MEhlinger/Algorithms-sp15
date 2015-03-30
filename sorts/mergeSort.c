/*
* MergeSort in C
* by Marshall Ehlinger
* for Algorithms Spring 2015
* Main method sorts a test array of integers
*/

#include <stdio.h>
#include <stdlib.h>

void merge(int array[], int midpoint, int arrayLen) {
	// Iterators
	int li = 0;
	int ri = 0;
	int di = 0;
	int mergei = 0;

	int *newArray = malloc(arrayLen * sizeof(int));


	while((li < midpoint) && (midpoint + ri < arrayLen)) {
		if (array[li] < array[midpoint + ri]) {
			newArray[di] = array[li];
			li++;
		} else {
			newArray[di] = array[midpoint + ri];
			ri++;
		}
		di++;
	}

	while (li < midpoint) {
		newArray[di] = array[li];
		li++;
		di++;
	}

	while (midpoint + ri < arrayLen) {
		newArray[di] = array[midpoint + ri];
		ri++;
		di++;
	}

	for (mergei = 0; mergei < arrayLen; mergei++) {
		array[mergei] = newArray[mergei];
	}

	free(newArray); 
}

void mergeSort(int *array, int arrayLen) {
	int midpoint;

	if (arrayLen < 2) {
		return;
	} else {
		midpoint = arrayLen / 2;
		mergeSort(array, midpoint);
		mergeSort(array + midpoint, arrayLen - midpoint);
		merge(array, midpoint, arrayLen);
	}
}

void printArray(int array[], int arrayLen) {
	int i;
	for (i = 0; i < arrayLen; i++) {
		printf("%d ", array[i]);
	}
	printf("\n");
}

int main() {
	int a[] = {3, 11, 2, 9, 5, 22, 15, 100};
	int arrayLen = sizeof(a) / sizeof(a[0]);

	printArray(a, arrayLen);
	mergeSort(a, arrayLen);
	printArray(a, arrayLen);
	return 0;
}