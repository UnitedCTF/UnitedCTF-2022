# Inflation

```c
float my_salary_increase(char *encrypted_coefficient) {
  int res = 0;
  int i = 0;

  for (char *p = encrypted_coefficient; *p; ++p)
    res += (*p - '0') << (i++ * 4);

  return *(float *)&res;
}
```

# Flag

`FLAG-14.3456%`
