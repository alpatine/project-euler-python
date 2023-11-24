# A Formula for Triangle Numbers
Triangle numbers are formed by adding consecutive numbers, starting at 1. The
following table describes the first 5 triangle numbers. The $ n^\text{th} $
triangle number will be denoted as $ T(n) $.

$$
\begin{array}{|c|l|c|}
\hline
n & \text{Sum} & T(n) \\
\hline
1 & 1 & 1 \\
2 & 1 + 2 & 3 \\
3 & 1 + 2 + 3 & 6 \\
4 & 1 + 2 + 3 + 4 & 10 \\
5 & 1 + 2 + 3 + 4 + 5 & 15 \\
\hline
\end{array}
$$

Express $ T(n) $ as the sum of natural numbers up to $ n $:

$$ T(n) = \sum_{k=1}^nk = 1 + 2 + 3 + \dots + (n-2) + (n-1) + n $$

Being a finite sum there is no issue with writing it in reverse order:

$$ T(n) = n + (n-1) + (n-2) + \dots + 3 + 2 + 1 $$
    
Note that $T(n)$ has exactly $n$ terms. If we add both versions together we get
the following expression:

$$\begin{array}{rlllllllllll}
    & T(n) &= &1 &+ &2 &+ &\cdots &+ &n \\
    + & T(n) &= &n &+ &(n-1) &+ &\cdots &+ &1 \\
    \hline & 2T(n) &= &(1+n) &+ &(2+(n-1)) &+ &\cdots &+ &(n+1) \\
    &  &= &(n+1) &+ &(n+1) &+ &\cdots &+ &(n+1) \\
    & 2T(n) &= &n(n+1)
\end{array}$$

Dividing both sides by 2 we get a closed formula:

$$ T(n) = \frac{n(n+1)}{2} $$