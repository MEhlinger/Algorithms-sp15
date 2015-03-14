/*
* LEXICOGRAPHIC PERMUTER
* Generates next permutation of give input, lexicographically
*
* by Marshall Ehlinger
* Recursively implemented with a test array of four sequential integers
*/

# include <stdio.h>
# include <math.h>

void printArray(int a[], int aSize);
void lexPermute(int p[], int pSize);

main() {
	/* Test Program */
	int perm[] = {1, 2, 3, 4};
	int permSize = sizeof(perm) / sizeof(perm[0]);

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

void swap(int* a, int* b) {
	int temp = *b;
	*b = *a;
	*a = temp;
}

void lexPermute(int p[], int pSize) {
	int i, k, j, g, h, temp;

	/* 
	* If permutation array "a" (p in the code below) 
	* has two consecutive elements in increasing order, 
    * Find the largest index i so that a[i]< a[i+1] 
    */
	for (i = pSize - 2; i >= 0; i--) {
		if (p[i] < p[i + 1]) {

			// Find the largest index k so that array[i] < array[j]
			for (k = pSize - 1; k > i; k--) {
				if (p[k] > p[i]) {
					j = k;
					break;
				}
			}

			// Swap array[i] and array[j]
			swap(&p[i], &p[j]);

			// Reverse order of array[i + 1] up to a[n]
			// Where g is the lower bound of the reversing, and h is the upper
			g = i + 1;
			h = pSize -1;
			while (g < h) {
				swap(&p[g], &p[h]);
				g ++;
				h --;
			}

			printArray(p, pSize);
			lexPermute(p, pSize);
			return;
		}
	}
	return;
}


