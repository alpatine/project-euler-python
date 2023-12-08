# A Formula for Fibonacci Numbers

## Exploring the Sequence
The Fibonacci sequence starts with 0 and 1, and each new term is calculated by
adding the previous two terms together:

$$ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, \dots $$

We can define the sequence as follows:

$$\begin{aligned}
    F_0 &= 0 \\
    F_1 &= 1 \\
    F_{n+2} &= F_{n+1} + F_n
\end{aligned}$$

Using this definition to calculate the third Fibonacci number:

$$\begin{aligned}
    F_0 &= 0 \\
    F_1 &= 1 \\
    F_2 &= F_1 + F_0 = 1 + 0 = 1 \\
    F_3 &= F_2 + F_1 = 1 + 1 = 2
\end{aligned}$$

This process can be repeated to calculate the nth Fibonacci number, but it will
involve a lot of steps for large $n$. Instead, the relationship above can be
used to derive a formula that will calculate the nth Fibonacci number. 

## Finding the Generating Function
Doing this will make use of generating functions and the following formula for
the sum of an infinite geometric series:

$$\begin{aligned}
    \sum_{n=0}^\infty x^n = 1 + x + x^2 + x^3 + x^4 + \cdots
        = \frac{1}{1-x} && (|x| < 1)
\end{aligned}$$

Start by defining the generating function and finding a closed form for it. Then
take that closed form and express it as the sum of an infinite geometric series.
These two expressions will be equal by construction, meaning that the
coefficients of corresponding powers of $x$ will be equal in both expressions.
Importantly this applies to the general nth term, which will equate $F_n$ to its
closed form.

Define the generating function as:

$$\begin{aligned} F(x) &= \sum_{n=0}^\infty F_nx^n \\
    &= F_0x^0 + F_1x^1 + F_2x^2 + F_3x^3 + F_4x^4 + F_5x^5 + \cdots \\
    &= 0 + x + x^2 + 2x^3 + 3x^4 + 5x^5 + \cdots
\end{aligned}$$

In $F(x)$, the variable $x$ is a formal variable. It is there purely to assist
with algebraic manipulation. Through our calculation we will encounter
constraints on the values that x could take e.g. $(|x|<1)$. The result does not
depend on $x$ so we will assume it to have a value that satisfies those
constraints.

Extract the first two terms from the generating function:

$$ F(x) = 0 + x + \sum_{n=2}^\infty F_nx^n $$

Reindex the sum:

$$\begin{aligned}
    \text{Change } n &\to n+2 \\
    F(x) &= x + \sum_{n=0}^\infty F_{n+2}x^{n+2}
\end{aligned}$$

Apply the recurrence relation to $F_{n+2}$ and split into separate sums:

$$\begin{aligned}
    F(x) &= x + \sum_{n=0}^\infty F_{n+2}x^{n+2} \\
    &= x + \sum_{n=0}^\infty (F_{n+1} + F_n)x^{n+2} \\
    &= x + \sum_{n=0}^\infty F_{n+1}x^{n+2}
        + \sum_{n=0}^\infty F_nx^{n+2}
\end{aligned}$$

Factorise powers of $x$ out of each sum so that the exponent for $x$ matches the
subscript for $F$:

$$\begin{aligned}
    F(x) &= x + \sum_{n=0}^\infty F_{n+1}x^{n+2}
            + \sum_{n=0}^\infty F_nx^{n+2} \\
    &= x + x\sum_{n=0}^\infty F_{n+1}x^{n+1} + x^2\sum_{n=0}^\infty F_nx^n
\end{aligned}$$

Reindex the middle sum so that the exponent of $x$ and the subscript of $F$ are
both $n$, then add $F_0=0$ back into the middle sum:

$$\begin{aligned}
    F(x) &= x + x\sum_{n=0}^\infty F_{n+1}x^{n+1}
            + x^2\sum_{n=0}^\infty F_nx^n \\
    &= x + x\sum_{n=1}^\infty F_nx^n + x^2\sum_{n=0}^\infty F_nx^n
        && \text{(reindex)} \\
    &= x + x\sum_{n=0}^\infty F_nx^n + x^2\sum_{n=0}^\infty F_nx^n
        && \text{(add $F_0 = 0$)}
\end{aligned}$$

Notice that the second and third terms contain the original generating function
defined as $F(x)$. Make that substitution and then solve for $F(x)$:

$$\begin{aligned}
    F(x) &= x + x\sum_{n=0}^\infty F_nx^n + x^2\sum_{n=0}^\infty F_nx^n \\
    &= x + xF(x) + x^2F(x) \\
    F(x) - xF(x) - x^2F(x) &= x \\
    (1 - x - x^2)F(x) &= x \\
    F(x) &= \frac{x}{1-x-x^2}
\end{aligned}$$

## Expressing as an Infinite Series
The generating function can be manipulated into a form that can be directly
converted to an infinite geometric series. To do this, factorise the denominator
into factors of an appropriate form and then use partial fraction decomposition
to break up the expression.

Assuming this is possible, the variables $a$, $b$, $A$, and $B$ will be
placeholders for values to be calculated later. If values for them can be found,
then the assumption holds and the result holds.

$$\begin{aligned}
    F(x) &= \frac{x}{1-x-x^2} \\
    &= \frac{x}{(1-ax)(1-bx)} && \text{(factorise denominator)} \\
    &= \frac{A}{1-ax} + \frac{B}{1-bx}
        && \text{(partial fraction decomposition)} \\
    &= A \sum_{n=0}^\infty(ax)^n + B \sum_{n=0}^\infty(bx)^n
        && \text{(sum of infinite geometric series)} \\
    &= \sum_{n=0}^\infty Aa^nx^n + \sum_{n=0}^\infty Bb^nx^n \\
    &= \sum_{n=0}^\infty(Aa^nx^n + Bb^nx^n) \\
    &= \sum_{n=0}^\infty(Aa^n + Bb^n)x^n
\end{aligned}$$

There is now two equal expressions for $F(x)$. Since they are equal and
expressed as power series, coefficients of corresponding powers of $x$ are also
equal. Extracting the nth power of $x$:

$$\begin{aligned}
    F(x) = \sum_{n=0}^\infty F_nx^n &= \sum_{n=0}^\infty(Aa^n + Bb^n)x^n \\
    \Rightarrow F_n &= Aa^n + Bb^n && \text{(extracting coefficients)}
\end{aligned}$$

## The Closed Formula
Now that the form of $F_n$ has been determined, values for the placeholder
variables $a$, $b$, $A$, and $B$ should be determined.

The first two values to be determined will be $a$ and $b$. From the step
factorising the denominator:

$$\begin{aligned}
    (1-ax)(1-bx) &= 1-x-x^2 \\
    1-(a+b)x + abx^2 &= 1-x-x^2
\end{aligned}$$

Equating coefficients produces the following system of equations:

$$\begin{cases}
    a+b &= 1 \\
    ab &= -1
\end{cases}$$

Solving this system:

$$\begin{aligned}
    b &= 1-a \\
    ab = a(1-a) &= -1 \\
    a - a^2 &= -1 \\
    a^2-a-1 &= 0 \\
    a &= \frac{-(-1) \pm \sqrt{(-1)^2-4\cdot(1)\cdot(-1)}}{2\cdot(1)}
        && \text{(quadratic formula)} \\
    &= \frac{1 \pm \sqrt5}{2} \\
    \text{If } a = \frac{1 + \sqrt5}{2} \text{:} \\
    b &= 1 - \frac{1 + \sqrt5}{2} \\
    &= \frac{2}{2} - \frac{1 + \sqrt5}{2} \\
    &= \frac{1 - \sqrt5}{2} \\
    \text{If } a = \frac{1 - \sqrt5}{2} \text{:} \\
    b &= 1 - \frac{1 - \sqrt5}{2} \\
    &= \frac{2}{2} - \frac{1 - \sqrt5}{2} \\
    &= \frac{1 + \sqrt5}{2}
\end{aligned}$$

The system of equations is symmetric in $a$ and $b$, meaning their values can be
swapped with no effect. Without loss of generality, assign the positive root to
$a$.

$$\begin{aligned}
    a = \frac{1 + \sqrt5}{2}
    && b = \frac{1 - \sqrt5}{2}
\end{aligned}$$

This leaves $A$ and $B$ to be determined. From the partial fraction
decomposition:

$$\begin{aligned}
    \frac{x}{(1-ax)(1-bx)} &= \frac{A}{1-ax} + \frac{B}{1-bx} \\
    x &= A(1-bx) + B(1-ax) \\
    x &= (-Ab-Ba)x + (A+B)
\end{aligned}$$

Equating coefficients of corresponding powers of $x$ gives the following system
of equations:

$$ \begin{cases} -Ab-Ba &= 1 \\ A+B &= 0 \end{cases} $$

Solving this system:

$$\begin{aligned}
    B &= -A \\
    -Ab-(-A)a &= 1 \\
    -Ab+Aa &= 1 \\
    A(a-b) &= 1 \\
    A &= \frac{1}{a-b} \\
    &= \frac{1}{\frac{1 + \sqrt5}{2} - \frac{1 - \sqrt5}{2}} \\
    &= \frac{1}{\sqrt5} \\
    B &= -A \\
    &= -\frac{1}{\sqrt5}
\end{aligned}$$

Values were determined for all four placeholder variables without
contradictions, so the result holds. Substituting those values into the form of
$F_n$:

$$\begin{aligned}
    F_n &= Aa^n + Bb^n \\
    &=\left(\frac{1}{\sqrt5}\right) \left(\frac{1 + \sqrt5}{2}\right)^n
        + \left(-\frac{1}{\sqrt5}\right)\left(\frac{1 - \sqrt5}{2}\right)^n \\
    &= \frac{1}{\sqrt5}\left(\left(\frac{1+\sqrt5}{2}\right)^n
        - \left(\frac{1-\sqrt5}{2}\right)^n\right)
\end{aligned}$$
