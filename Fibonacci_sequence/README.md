# Fibonacci sequence
## General info
This was my attempt to create recurring fibonacci sequence generator.

>In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.
[Fibonacci number Wiki](https://en.wikipedia.org/wiki/Fibonacci_number)

There are three scripts doing the same think, they have the same core of the function but two of these scripts use memorization (in this case this means storing previously calculated values in memory) to improve the overall performance of the function.
* Fibonacci_wm.py - sript without implemetyd memorization, poor overall performance. Calculating mor than 30 fibonaci numbers takes       significant amount of time.
* Fibonacci_mbh.py - script uscing python dictionary as cache memory. Great impovement over script without memorization. Calculating 500 numbers takes less than second.
* Fibonacci_mwc.py - script uscing python lru_cache function to creat cach. Similar perfomence to Fibonacci_mbh.py, slightly faster too.

## Technologies
* Python 3.7.3

Libraries:
* functools
* time

## Sources and helpful materials
[Fibonacci number Wiki](https://en.wikipedia.org/wiki/Fibonacci_number)

[Recursion (computer science) Wiki](https://en.wikipedia.org/wiki/Recursion_(computer_science))

[Fibonacci Mystery - Numberphile](https://www.youtube.com/watch?v=Nu-lW-Ifyec)
