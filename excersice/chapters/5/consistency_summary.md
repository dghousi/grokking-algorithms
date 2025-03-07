## Summary

- **f1** always returns `1`, making it consistent.
- **f2** returns a random number each time, making it inconsistent.
- **f3** simulates a hash table and may return different empty slots depending on the state of the table, making it inconsistent.
- **f4** returns the length of the input, making it consistent.

## Consistent Hash Functions:

- \( f(x) = 1 \) (5.1)
- \( f(x) = \text{len}(x) \) (5.4)

## Inconsistent Hash Functions:

- \( f(x) = \text{random.random()} \) (5.2)
- \( f(x) = \text{next_empty_slot()} \) (5.3)
