#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * Ton patron, un peu freak, te dit que tu auras une augmentation de salaire cette année. 
 * Pour pimenter un peu la sauce, il dit que seul ceux qui réussirons à trouver le bon 
 * coefficient d'augmentation l'auront cette année.
 *
 * Il te donne cet algorithme en disant que la sortie de cet algorithme est `49785614`, 
 * trouve le coefficient que ton patron a passé en paramètre et l'augmentation sera tienne !
 */

char *money_money_cypher(float coefficient) {
  char *res = (char *)malloc(sizeof(char) * 8);
  int count = 0;
  
  for (int i = *(int *)&coefficient; i > 0; i >>= 4)
    res[count++] = '0' + (i & 0b1111);

  return res;
}


float my_salary_increase(const char *encrypted_coefficient) {
  // TODO !
  return 0.0f;
}

int main() {
  const char *encrypted_coefficient = "49785614";

  printf("FLAG-%g%%\n", my_salary_increase(encrypted_coefficient));

  return 0;
}