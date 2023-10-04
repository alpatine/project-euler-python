# Generating Pythagorean Triples

## What are Pythagorean Triples?
A *pythagorean triple* is three positive integers $a$, $b$, and $c$ that make up
the integer side lengths of a right triangle. The three numbers have the
following relationship with each other:

$$ (a, b, c) \text{ is a pythagorean triple} \Leftrightarrow a^2 + b^2 = c^2 $$

All pythagoran triples can be scaled to create new pythagorean triples by
multiplying $a$, $b$, and $c$ by a positive integer $k$.

$$
\begin{aligned}
    \text{Given} && a, b, c, k &\in \mathbb{Z}_{>0}
        && \text{positive integers} \\
    \text{Such that} && a^2 + b^2 &= c^2
        && \text{$(a, b, c)$ is a pythagorean triple} \\
    \text{Consider} && (ak)^2 + (bk)^2 &= a^2k^2 + b^2k^2 \\
        &&&= (a^2+b^2)k^2 \\
        &&&= c^2k^2 \\
        &&&= (ck)^2 \\
    
\end{aligned}
$$

A pythagorean triple is called a *primitive pythagorean triple* if the greatest
common divisor of $a$, $b$, and $c$ is 1.

$$
    \text{Given a pythagorean triple } (a, b, c) \\
    (a, b, c) \text{ is primitive} \Leftrightarrow \gcd(a, b, c) = 1
$$

Finally, the sum $a+b$ is less than $c$. This follows directly from the triangle
inequality given $a$, $b$, and $c$ are all side lengths of a triangle.
Alternatively, it can be shown algebarically:

$$
\begin{aligned} \text{Claim} &&&&c &< a+b\\
    \text{Proof} &&&&a^2 + b^2 &< a^2 + b^2 + 2ab \\
    &&\Rightarrow && c^2 &< (a+b)^2 \\
    &&\Rightarrow && |c| &< |a + b| \\
    &&\Rightarrow && c &< a + b && a, b, c \in \mathbb{Z}_{>0}
\end{aligned}
$$

## Generating Pythagorean Triples
See: [Wikipedia: Tree of primitive Pythagorean
triples](https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples)

All primitive pythagorean triples exist within a ternary tree structure, with
$(3, 4, 5)$ as the root of the tree. The following three matricies are used to
generate the three child branches of a given primitive pythagorean triple.

$$
\begin{aligned}
    A = \begin{pmatrix}
        1 & -2 & 2 \\
        2 & -1 & 2 \\
        2 & -2 & 3
    \end{pmatrix} &&
    B = \begin{pmatrix}
        1 & 2 & 2 \\
        2 & 1 & 2 \\
        2 & 2 & 3
    \end{pmatrix} &&
    C = \begin{pmatrix}
        -1 & 2 & 2 \\
        -2 & 1 & 2 \\
        -2 & 2 & 3
    \end{pmatrix}
\end{aligned}
$$

For example, starting with the triple $(3, 4, 5)$ and multiplying by each of the
three matricies yields three new primitive pythagorean triples.

$$
\begin{aligned}
    \text{Given: } \\
    &&& p = \begin{pmatrix} 3 \\ 4 \\ 5 \end{pmatrix} \\
    \text{Define: } \\
    &&& p_A = Ap = \begin{pmatrix}
        1 & -2 & 2 \\
        2 & -1 & 2 \\
        2 & -2 & 3
    \end{pmatrix} \begin{pmatrix} 3 \\ 4 \\ 5 \end{pmatrix} 
    = \begin{pmatrix} 5 \\ 12 \\ 13 \end{pmatrix} \\ \\
    &&& p_B = Bp = \begin{pmatrix}
        1 & 2 & 2 \\
        2 & 1 & 2 \\
        2 & 2 & 3
    \end{pmatrix} \begin{pmatrix} 3 \\ 4 \\ 5 \end{pmatrix}
    = \begin{pmatrix} 21 \\ 20 \\ 29 \end{pmatrix} \\ \\
    &&& p_C = Cp = \begin{pmatrix}
        -1 & 2 & 2 \\
        -2 & 1 & 2 \\
        -2 & 2 & 3
    \end{pmatrix} \begin{pmatrix} 3 \\ 4 \\ 5 \end{pmatrix}
    = \begin{pmatrix} 15 \\ 8 \\ 17 \end{pmatrix} \\
\end{aligned}
$$

$p_A$, $p_B$, and $p_C$ are all primitive pythagorean triples, 'decended' from
$p$.

In general, the equations are:

$$
\begin{aligned}
    \text{Given: } \\
    &&& q = \begin{pmatrix} a \\ b \\ c \end{pmatrix}
        \qquad \text{(a primitive pythagorean triple)}\\
    \text{Define: } \\
    &&& q_A = \begin{pmatrix} a_A \\ b_A \\ c_A \end{pmatrix} = Aq
    = \begin{pmatrix}
        1 & -2 & 2 \\
        2 & -1 & 2 \\
        2 & -2 & 3
    \end{pmatrix} \begin{pmatrix} a \\ b \\ c \end{pmatrix}
    = \begin{pmatrix} a-2b+2c \\ 2a-b+2c \\ 2a-2b+3c \end{pmatrix} \\ \\
    &&& q_B = \begin{pmatrix} a_B \\ b_B \\ c_B \end{pmatrix} = Bq
    = \begin{pmatrix}
        1 & 2 & 2 \\
        2 & 1 & 2 \\
        2 & 2 & 3
    \end{pmatrix} \begin{pmatrix} a \\ b \\ c \end{pmatrix}
    = \begin{pmatrix} a+2b+2c \\ 2a+b+2c \\ 2a+2b+3c \end{pmatrix} \\ \\
    &&& q_C = \begin{pmatrix} a_C \\ b_C \\ c_C \end{pmatrix} = Cq
    = \begin{pmatrix}
        -1 & 2 & 2 \\
        -2 & 1 & 2 \\
        -2 & 2 & 3
    \end{pmatrix} \begin{pmatrix} a \\ b \\ c \end{pmatrix}
    = \begin{pmatrix} -a+2b+2c \\ -2a+b+2c \\ -2a+2b+3c \end{pmatrix} \\ \\
\end{aligned}
$$

Where $q_A$, $q_B$, and $q_C$ are all primitive pythagorean triples.

One property of $q_A$, $q_B$, and $q_C$ that will be important for problem
solving is the fact that the sum of the components of $q_A$, $q_B$, or $q_C$ is
larger than the sum of the components of $q$. Several problems involve searching
all pythagorean triples where the sum of the components less than a given value.

$$
\begin{aligned}
    \text{Claim: } \\
    && a_A + b_A + c_A &> a + b + c \\
    \text{Proof: } \\
    && a_A + b_A + c_A &= (a-2b+2c) + (2a-b+2c) + (2a-2b+3c) \\
    &&&= 5a - 5b + 7c \\
    &&&= 5a - 5b + 6c + c \\
    &&&> 5a - 5b + 6b + c && b < c \\
    &&&= 5a + b + c \\
    &&&> a + b + c \\ \\
    \text{Claim: } \\
    && a_B + b_B + c_B &> a + b + c \\
    \text{Proof: } \\
    && a_B + b_B + c_B &= (a+2b+2c) + (2a+b+2c) + (2a+2b+3c) \\
    &&&= 5a + 5b + 7c \\
    &&&> a + b + c \\ \\
    \text{Claim: } \\
    && a_C + b_C + c_C &> a + b + c \\
    \text{Proof: } \\
    && a_C + b_C + c_C &= (-a+2b+2c) + (-2a+b+2c) + (-2a+2b+3c) \\
    &&&= -5a + 5b + 7c \\
    &&&= -5a + 6c + 5b + c \\
    &&&> -5a +6a + 5b + c && a < c \\
    &&&= a + 5b + c \\
    &&&> a + b + c
\end{aligned}
$$

