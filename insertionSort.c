/* 
* Insertion Sort
* by Marshall Ehlinger
* Written for Spring 2015 Analysis of Algorithms
*/
# include <stdio.h>

main() {
	int i, j, k, temp;
	int array[] = {10, 2, 5, 2, 8, 9, 3};
	int arraySize = sizeof(array) / sizeof(array[0]);

	for (i = 1; i < arraySize; i++) {
		for (j = i; array[j - 1] > array[j]; j--) {
			temp = array[j];
			array[j] = array[j-1];
			array[j-1] = temp;
		}
	}

	for (k = 0 ; k < arraySize ; k++) {
		printf("%d\n", array[k]);
	}
}