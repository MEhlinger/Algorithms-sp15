/* 
* Insertion Sort
* by Marshall Ehlinger
* Written for Spring 2015 Analysis of Algorithms
*/
# include <stdio.h>

main() {
	int i, j, k, temp;
	int array[] = {10, 2, 5, 2, 8, 9, 3};
	const int ARRAY_LENGTH = sizeof(array) / sizeof(array[0]);

	for (i = 1; i < ARRAY_LENGTH; i++) {
		j = i;
		while ((j > 0)  && (array[j-1] > array[j])) {
			temp = array[j];
			array[j] = array[j-1];
			array[j-1] = temp;
			j--;
		}
	}

	for (k = 0 ; k < ARRAY_LENGTH ; k++) {
		printf("%d\n", array[k]);
	}
}