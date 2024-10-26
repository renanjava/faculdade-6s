#include <stdio.h>
#include <time.h>

void RelogioAlarme(int horaAlarme) {
    // Mostrar a hora atual
    time_t t;
    time(&t);
    printf("Hora atual: %s", ctime(&t));

    // Verificar alarme
    struct tm* localTime = localtime(&t);
    if (localTime->tm_hour == horaAlarme) {
        printf("Alarme! Acorde!\n");
    }
}

int main() {
    RelogioAlarme(8);  // Definir alarme para 8 horas
    return 0;
}
