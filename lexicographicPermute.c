/*
* LEXICOGRAPHIC PERMUTER
* Generates next permutation of give input, lexicographically
*
*
*
*/

# include <stdio.h>;
# include <math.h>;

void printArray(int a[]) {
	int i;
	int aSize = sizeof(a) / sizeof(a[0]);

	for (i = 0; i < aSize; i++) {
		printf("%d\n", a[i]);
	}
	printf("\n");
}

int* lexPermute(int p[]) {
	int i, k, j, g, temp;
	int pSize = sizeof(p) / sizeof(p[0]);

	/* 
	* If permutation array "a" (p in the code below) 
	* has two consecutive elements in increasing order, 
    * Find the largest index i so that a[i]< a[i+1] 
    */
	for (i = pSize - 2; i >= 0; i--) {
		if (p[i] < p[i + 1]) {

			/* Find the largest index k so that array[i] < array[j] */
			for (k = pSize - 1; k < i; k--) {
				if (p[k] > p[i]) {
					j = k;
					break;
				}
			}

			/* Swap array[i] and array[j] */
			temp = p[i];
			p[i] = p[j];
			p[j] = temp;

			/* Reverse order of array[i + 1] up to a[n] */
			for (g = i+1; g < ceil((pSize + i + 1) / 2); g++) {
				temp = p[pSize - (g - 1)];
				p[pSize - (g - 1)] = p[g];
				p[g] = temp;
			}

			printArray(p);
			lexPermute(p);
		}
	}

	return p;

}


main() {
	/* Test Program */
	int perm[] = {1, 2, 3, 4};
	lexPermute(perm);
}