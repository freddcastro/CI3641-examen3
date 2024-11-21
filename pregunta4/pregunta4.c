#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <math.h>


// Para evaluar de forma dinámica sin warnings en la compilación, el último argumento debe ser int **matriz
int sumaPorFila(int N, int M, int matriz[N][M]) {
    int suma = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            suma += matriz[i][j];
        }
    }
    return suma;
}

// Para evaluar de forma dinámica sin warnings en la compilación, el último argumento debe ser int **matriz
int sumaPorColumna(int N, int M, int matriz[N][M]) {
    int suma = 0;
    for (int j = 0; j < M; j++) {
        for (int i = 0; i < N; i++) {
            suma += matriz[i][j];
        }
    }
    return suma;
}
int main() {

    for (int i = 2; i <= 3; i++)
    {
        for (int j = 2; j <= 3; j++)
        {
            int N1 = (int)pow(10, i);
            int M1 = (int)pow(10, j);
            
            int matriz[N1][M1];
            
            printf("Matriz de %d x %d\n", N1, M1);

            for (int i = 1; i <= 3; i++)
            {
                clock_t inicio = clock();
                int suma = sumaPorFila(N1, M1, matriz);
                clock_t fin = clock();
                double tiempo_segundos = (double)(fin - inicio) / CLOCKS_PER_SEC;
                printf("Iteracion %d\n", i);
                printf("Tiempo de ejecución de Suma por Fila: %.6f segundos\n", tiempo_segundos);

                clock_t inicio2 = clock();
                int suma2 = sumaPorColumna(N1, M1, matriz);
                clock_t fin2 = clock();
                double tiempo_segundos2 = (double)(fin2 - inicio2) / CLOCKS_PER_SEC;
                printf("Tiempo de ejecución de Suma por Columna: %.6f segundos\n", tiempo_segundos2);
            }
        }
        
    }
    

    
    
    return 0;
}