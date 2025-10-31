#include <stdio.h>
int main()
{int n;
int i;
scanf("%d",&n);
int h[100001];
int count[100001] = {0};
for(i=0;i<n;i++){
     scanf("%d", &h[i]);
    }
    count[h[0]]++;
    for (int i = 0; i < n - 1; i++) {
        int start = h[i];
        int end = h[i + 1];

        if (start < end) {
            for (int j = start + 1; j <= end; j++) {
                count[j]++;
            }
        } else {
            for (int j = start - 1; j >= end; j--) {
                count[j]++;
            }
        }
    }

    // Find maximum frequency
    int maxFreq = 0;
    for (int i = 1; i <= 1000; i++) {
        if (count[i] > maxFreq) {
            maxFreq = count[i];
        }
    }

    printf("%d\n", maxFreq);


	return 0;
}
