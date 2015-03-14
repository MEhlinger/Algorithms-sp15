/*
* LEXICOGRAPHIC PERMUTER
* Generates next permutation of give input, lexicographically
*
*
*
*/

# include <stdio.h>
# include <math.h>

void printArray(int a[], int aSize);
void lexPermute(int p[], int pSize);

main() {
	/* Test Program */
	int perm[] = {1, 2, 3, 4};
	int permSize = (int) sizeof(perm) / sizeof(perm[0]);

	printArray(perm, permSize);
	printArray(perm, permSize);

	lexPermute(perm, permSize);
}

void printArray(int a[], int aSize) {
	int i;

	for (i = 0; i < aSize; i++) {
		printf("%d\n", a[i]);
	}
	printf("\n");
}

void lexPermute(int p[], int pSize) {
	int i, k, j, g, temp;

	/* 
	* If permutation array "a" (p in the code below) 
	* has two consecutive elements in increasing order, 
    * Find the largest index i so that a[i]< a[i+1] 
    */
	for (i = pSize - 2; i >= 0; i--) {
		if (p[i] < p[i + 1]) {

			// Find the largest index k so that array[i] < array[j]
			for (k = pSize - 1; k < i; k--) {
				if (p[k] > p[i]) {
					j = k;
					break;
				}
			}

			// Swap array[i] and array[j]
			temp = p[i];
			p[i] = p[j];
			p[j] = temp;

			// Reverse order of array[i + 1] up to a[n]
			for (g = i+1; g < ceil((pSize + i + 1) / 2); g++) {
				temp = p[pSize - (g - 1)];
				p[pSize - (g - 1)] = p[g];
				p[g] = temp;
			}
			printArray(p, pSize);
			lexPermute(p, pSize);
			return;
		}
	}
	return;
}


