# Generating Prime Numbers

## What's the problem?
Many of the problems within Project Euler involve prime numbers. Having an
efficient way to generate prime numbers will be essential to keeping the
execution of solutions acceptably fast.

All known formulae for directly calculating the n'th prime number are slow when
implemented on a classical computer. To make this worse, we will often need to
search through ALL primes up to a large number. An approach where we directly
calculate the 1st prime, then independently and directly generate the 2nd, and
so on, is not an option for us.

## Checking if numbers are prime
One approach for building a list of prime numbers would be to start with a list
of all candidate numbers, and then test each number individually to see if it is
prime.

All natural numbers can be written as a unique (up to ordering) product of prime
numbers. A prime number will only contain one copy of itself in its product. A
composite number will contain multiple primes in the product. One is neither
prime nor composite - it is the unit of the natural numbers.

$$\begin{aligned}
    \text{Unit:} && 1 & \\
    \text{Prime:} && 5 &= 5 \\
    \text{Composite:} && 6 &= 2 * 3 \\
    \text{Composite:} && 9 &= 3 * 3 = 3^2
\end{aligned}$$

Consider the number 47. To check if it is prime, we can simply check if any
of the numbers less than 47 divides 47. Using division with remainder:

$$\begin{aligned}
    47 = 23 \cdot 2 + 1 \Rightarrow 2 \nmid 47 \\
    47 = 15 \cdot 3 + 2 \Rightarrow 3 \nmid 47 \\
    47 = 11 \cdot 4 + 3 \Rightarrow 4 \nmid 47 \\
    47 = 9 \cdot 5 + 2 \Rightarrow 5 \nmid 47 \\
    47 = 7 \cdot 6 + 5 \Rightarrow 6 \nmid 47 \\
    47 = 6 \cdot 7 + 5 \Rightarrow 7 \nmid 47
\end{aligned}$$

For 47 we can stop here and do not need to test any numbers greater than 5\.
Notice that when we tested 7 the quotient was 6, this was the first result where
the quotient was less than the number we were testing.

If we find a larger number (less than 47) that divides evenly into 47, then the
quotient must be one of the smaller numbers already tested. This would mean that
smaller number also divides evenly into 47. However, we know from our testing
that there is no such smaller number. This causes a contradiction that means
there are no larger numbers that will divide evenly into 47. With no smaller
numbers that divide evenly into 47, and the impossibility of any larger numbers
dividing evenly into 47, we conclude that 47 is prime.

We can make this faster with the following observations:
* When checking if a number $n$ is prime, we only need to test numbers up to and
  including $\lfloor\sqrt{n}\rfloor$.
* Making 2 the only even number we test. Every even number greater than 2
  contains 2 as a factor. If 2 does not divide into $n$, then no greater even
  number will either.
* Ideally the only numbers we would test would be prime numbers. This requires
  us to know the prime numbers up to $\lfloor\sqrt{n}\rfloor$, which requires us
  to already know the result that this process is calculating.

Even with these optimisations in place, this technique will prove to be too slow
for our needs.

## The Sieve of Eratosthenes
There are faster ways to generate a list of prime numbers. The method we will
use is called the *Sieve of Eratosthenes*. It is not the fastest method known,
but it is fast enough for our needs and easy to understand.

As an example, start with the numbers from 1 to fifty. We can immediately
eliminate 1 because it is the unit of the natural numbers, so it is not prime.

$$
\begin{array}{|c|c|c|c|c|c|c|c|c|c|}
    \hline
    & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
    \hline
    11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 & 20 \\
    \hline
    21 & 22 & 23 & 24 & 25 & 26 & 27 & 28 & 29 & 30 \\
    \hline
    31 & 32 & 33 & 34 & 35 & 36 & 37 & 38 & 39 & 40 \\
    \hline
    41 & 42 & 43 & 44 & 45 & 46 & 47 & 48 & 49 & 50 \\
    \hline
\end{array}
$$

2 is the next available number, so we note it as being prime and then eliminate
all larger multiples of it from the table. The smallest such multiple is $2^2 =
4$. This gives us:

$$
\begin{array}{|c|c|c|c|c|c|c|c|c|c|}
    \hline
    & \color{green}{2} & 3 & \color{red}{4} & 5 & \color{red}{6} & 7
        & \color{red}{8} & 9 & \color{red}{10} \\
    \hline
    11 & \color{red}{12} & 13 & \color{red}{14} & 15 & \color{red}{16} & 17
        & \color{red}{18} & 19 & \color{red}{20} \\
    \hline
    21 & \color{red}{22} & 23 & \color{red}{24} & 25 & \color{red}{26} & 27
        & \color{red}{28} & 29 & \color{red}{30} \\
    \hline
    31 & \color{red}{32} & 33 & \color{red}{34} & 35 & \color{red}{36} & 37
        & \color{red}{38} & 39 & \color{red}{40} \\
    \hline
    41 & \color{red}{42} & 43 & \color{red}{44} & 45 & \color{red}{46} & 47
        & \color{red}{48} & 49 & \color{red}{50} \\
    \hline
\end{array}
\rightarrow
\begin{array}{|c|c|c|c|c|c|c|c|c|c|}
    \hline
    & \color{blue}{2} & 3 & & 5 & & 7 & & 9 & \\
    \hline
    11 & & 13 & & 15 & & 17 & & 19 & \\
    \hline
    21 & & 23 & & 25 & & 27 & & 29 & \\
    \hline
    31 & & 33 & & 35 & & 37 & & 39 & \\
    \hline
    41 & & 43 & & 45 & & 47 & & 49 & \\
    \hline
\end{array}
$$

3 is the next available number, so we note it as being prime and then eliminate
all larger multiples of it from the table. The smallest such multiple is $3^2 =
9$. This gives us:

$$
\begin{array}{|c|c|c|c|c|c|c|c|c|c|}
    \hline
    & \color{blue}{2} & \color{green}{3} & & 5 & & 7 & & \color{red}{9} & \\
    \hline
    11 & & 13 & & \color{red}{15} & & 17 & & 19 & \\
    \hline
    \color{red}{21} & & 23 & & 25 & & \color{red}{27} & & 29 & \\
    \hline
    31 & & \color{red}{33} & & 35 & & 37 & & \color{red}{39} & \\
    \hline
    41 & & 43 & & \color{red}{45} & & 47 & & 49 & \\
    \hline
\end{array}
\rightarrow
\begin{array}{|c|c|c|c|c|c|c|c|c|c|}
    \hline
    & \color{blue}{2} & \color{blue}{3} & & 5 & & 7 & & & \\
    \hline
    11 & & 13 & & & & 17 & & 19 & \\
    \hline
    & & 23 & & 25 & & & & 29 & \\
    \hline
    31 & & & & 35 & & 37 & & & \\
    \hline
    41 & & 43 & & & & 47 & & 49 & \\
    \hline
\end{array}
$$

5 is the next available number, so we note it as being prime and then eliminate
all larger multiples of it from the table. The smallest such multiple is $5^2 =
25$. This gives us:

$$
\begin{array}{|c|c|c|c|c|c|c|c|c|c|}
    \hline
    & \color{blue}{2} & \color{blue}{3} & & \color{green}{5} & & 7 & & & \\
    \hline
    11 & & 13 & & & & 17 & & 19 & \\
    \hline
    & & 23 & & \color{red}{25} & & & & 29 & \\
    \hline
    31 & & & & \color{red}{35} & & 37 & & & \\
    \hline
    41 & & 43 & & & & 47 & & 49 & \\
    \hline
\end{array}
\rightarrow
\begin{array}{|c|c|c|c|c|c|c|c|c|c|}
    \hline
    & \color{blue}{2} & \color{blue}{3} & & \color{blue}{5} & & 7 & & & \\
    \hline
    11 & & 13 & & & & 17 & & 19 & \\
    \hline
    & & 23 & & & & & & 29 & \\
    \hline
    31 & & & & & & 37 & & & \\
    \hline
    41 & & 43 & & & & 47 & & 49 & \\
    \hline
\end{array}
$$

7 is the next available number, so we note it as being prime and then eliminate
all larger multiples of it from the table. The smallest such multiple is $7^2 =
49$. This gives us:

$$
\begin{array}{|c|c|c|c|c|c|c|c|c|c|}
    \hline
    & \color{blue}{2} & \color{blue}{3} & & \color{blue}{5} &
        & \color{green}{7} & & & \\
    \hline
    11 & & 13 & & & & 17 & & 19 & \\
    \hline
    & & 23 & & & & & & 29 & \\
    \hline
    31 & & & & & & 37 & & & \\
    \hline
    41 & & 43 & & & & 47 & & \color{red}{49} & \\
    \hline
\end{array}
\rightarrow
\begin{array}{|c|c|c|c|c|c|c|c|c|c|}
    \hline
    & \color{blue}{2} & \color{blue}{3} & & \color{blue}{5} &
        & \color{blue}{7} & & & \\
    \hline
    11 & & 13 & & & & 17 & & 19 & \\
    \hline
    & & 23 & & & & & & 29 & \\
    \hline
    31 & & & & & & 37 & & & \\
    \hline
    41 & & 43 & & & & 47 & & & \\
    \hline
\end{array}
$$

11 is the next available number, so we note it as being prime and then eliminate
all larger multiples of it from the table. However, the smallest such multiple
is $11^2 = 121$ which is larger than all of the numbers remaining on the table.
This situation will repeat for all remaining numbers on the table so we know
they are all also prime, and the process ends.

$$
\begin{array}{|c|c|c|c|c|c|c|c|c|c|}
    \hline
    & \color{blue}{2} & \color{blue}{3} & & \color{blue}{5} &
        & \color{blue}{7} & & & \\
    \hline
    \color{green}{11} & & 13 & & & & 17 & & 19 & \\
    \hline
    & & 23 & & & & & & 29 & \\
    \hline
    31 & & & & & & 37 & & & \\
    \hline
    41 & & 43 & & & & 47 & & & \\
    \hline
\end{array}
\rightarrow
\begin{array}{|c|c|c|c|c|c|c|c|c|c|}
    \hline
    & \color{blue}{2} & \color{blue}{3} & & \color{blue}{5} &
        & \color{blue}{7} & & & \\
    \hline
    \color{blue}{11} & & \color{blue}{13} & & & & \color{blue}{17} &
        & \color{blue}{19} & \\
    \hline
    & & \color{blue}{23} & & & & & & \color{blue}{29} & \\
    \hline
    \color{blue}{31} & & & & & & \color{blue}{37} & & & \\
    \hline
    \color{blue}{41} & & \color{blue}{43} & & & & \color{blue}{47} & & & \\
    \hline
\end{array}
$$

With the process finished we read the primes less then 50 straight off the
table:

$$ {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47} $$

## Python Implementation
Our initial implementation will follow the algorithm outlined above. We will
build the list using an array of boolean values where each number equals it's
index, and a True indicates it is prime.

$$
\begin{array}{|c|c|c|c|}
    \hline
    \text{Index} & \text{Number} & \text{Is Prime?} \\
    \hline
    0 & 0 & \text{False} \\
    \hline
    1 & 1 & \text{False} \\
    \hline
    2 & 2 & \text{True} \\
    \hline
    3 & 3 & \text{True} \\
    \hline
    4 & 4 & \text{False} \\
    \hline
    5 & 5 & \text{True} \\
    \hline
    6 & 6 & \text{False} \\
    \hline
    7 & 7 & \text{True} \\
    \hline
    8 & 8 & \text{False} \\
    \hline
    9 & 9 & \text{False} \\
    \hline
    10 & 10 & \text{False} \\
    \hline
    11 & 11 & \text{True} \\
    \hline
    12 & 12 & \text{False} \\
    \hline
    13 & 13 & \text{True} \\
    \hline
    14 & 14 & \text{False} \\
    \hline
    15 & 15 & \text{False} \\
    \hline
    16 & 16 & \text{False} \\
    \hline
    17 & 17 & \text{True} \\
    \hline
    18 & 18 & \text{False} \\
    \hline
    19 & 19 & \text{True} \\
    \hline
    20 & 20 & \text{False} \\
    \hline
\end{array}
$$

``` python
def primes(upper: int) -> Iterator[int]:
    """Generate the prime numbers.

    The sequence starts with 2 and continues until upper is reached.
    The value upper is not included in the sequence.
    """
    prime_list = [True] * upper
    max_factor = floor(sqrt(upper))

    for i in range(2, upper):
        if prime_list[i] == True:
            yield i
            if i <= max_factor:
                for j in range(i*i, upper, i):
                    prime_list[j] = False
```

While this implementation is correct and accurate to the algorithm described
above, it can be made faster. We know there is only 1 even prime number (2), so
there is no point in storing or processing any larger even numbers. We also know
the smallest odd prime is 3. Putting this together we should start the list at
3, with each subsequent element representing the next odd number.

$$
\begin{array}{|c|c|c|c|}
    \hline
    \text{Index ($i$)} & \text{Number ($n_i$)} & \text{Is Prime?} \\
    \hline
    0 & 3 & \text{True} \\
    \hline
    1 & 5 & \text{True} \\
    \hline
    2 & 7 & \text{True} \\
    \hline
    3 & 9 & \text{False} \\
    \hline
    4 & 11 & \text{True} \\
    \hline
    5 & 13 & \text{True} \\
    \hline
    6 & 15 & \text{False} \\
    \hline
    7 & 17 & \text{True} \\
    \hline
    8 & 19 & \text{False} \\
    \hline
\end{array}
$$

This gives us the following maps between array index and number represented. In
this document we will include zero in the natural numbers.
$$
\begin{aligned}
    \text{Given:} & \\
    && \mathbb{N} &= \{0, 1, 2, 3, \dots\} && \text{the natural numbers} \\
    && i &\in \mathbb{N}
        && \text{array index in the primes list} \\
    && n_i &\in \mathbb{N} &&\text{number represented at index $i$} \\
    \text{Then:} & \\
    n_i &= 2i + 3 && \Leftrightarrow &i &= \frac{n_i - 3}{2}
    
\end{aligned}
$$

Under this setup we will need to calculate indexes for the boundary conditions
within the algorithm. When the algorithm is called it is passed an upper number
$u$. Primes are generated up to (but excluding) that upper number. We need to
determine what index represents that upper number so that we generate the
correct number of primes.

We start by checking some initial boundaries:

* If $u \leq 2$, then there are no primes and the algorithm ends
* If $u \gt 2$, then return 2 as the first prime.
* If $u \gt 3$, then there will be additional primes and we continue with the
  algorithm.

It is possible that the $u$ passed is not odd, and therefore not representable
by our table. To correct this will will define $u_o$ to be the smallest odd
number greater than or equal to $u$:

$$
\begin{aligned}
    \text{With:} & \\
    && u \gt 3 &\in \mathbb{N}
        && \text{the upper number passed to the algorithm} \\
    && u_o &\in \mathbb{N} && \text{smallest odd number not in list} \\
    && n_i &\in \mathbb{N}
        && \text{number (odd) represented by index $i$} \\
    && i &\in \mathbb{N} && \text{any index in the list} \\
    \text{Then:} & \\
    && u_o &= \begin{cases}
        u &\text{$u$ odd} \\
        u + 1 & \text{$u$ even}
    \end{cases} \\
    && n_i &< u_o \\
    \Rightarrow && 2i + 3 &< u_o \\
    \Rightarrow && 2i &< u_o - 3 \\
    \Rightarrow && i &< \frac{u_o-3}{2} \in \mathbb{N}\\
    
\end{aligned}
$$

When we note a number as prime, we need to mark subsequent multiples of it
within the list as composite. This means we need to calculate two things:

1. The index that represents the first multiple to mark
1. The amount to increment the index to reach each subsequent multiple

From before, we saw that the first multiple of a prime that needs to be marked
as composite is the square of that prime.

$$
\begin{aligned}
\text{Given:} \\
&& n_p &\in \mathbb{N} && \text{the prime found} \\
&& i &\in \mathbb{N} && \text{index of the prime found} \\
&& n_p^2 = n_m &\in \mathbb{N} && \text{the next multiple} \\
&& m &\in \mathbb{N} && \text{index of the next multiple} \\
\text{Then:} & \\
&& n_m &= 2m + 3 \\
\Rightarrow && m &= \frac{n_m-3}{2} \\
\Rightarrow && m &= \frac{n_p^2 - 3}{2}
\end{aligned}
$$

An increase of 1 to an index corresponds to an increase of 2 to the value
represented. Since we ignore the even multiples of $p_i$, we need to increase
the value represented by $2p_i$, meaning the corresponding increase to the index
is simply $p_i$.

After making these modifications, the code now looks like:

``` python
def primes(upper: int) -> Iterator[int]:
    """Generate the prime numbers.

    The sequence starts with 2 and continues until upper is reached.
    The value upper is not included in the sequence.
    """
    if upper > 2:
        yield 2

    upper_odd = upper + 1 - (upper % 2)
    index_stop = (upper_odd - 3) // 2
    prime_list = [True] * index_stop
    max_factor = floor(sqrt(upper))

    for index in range(0, index_stop):
        if prime_list[index] == True:
            factor = 2 * index + 3
            yield factor
            if factor <= max_factor:
                for j in range((factor * factor - 3) // 2, index_stop, factor):
                    prime_list[j] = False
```

This more efficient implementation is roughly twice as fast at generating primes
than the initial implementation.
