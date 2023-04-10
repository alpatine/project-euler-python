A Formula for Fibonacci Numbers
===============================

Exploring the Sequence
----------------------

The Fibonacci sequence starts with 0 and 1, and each new term is calculated by
adding the previous two terms together:

.. math::
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, \dots

We can define the sequence as follows:

.. math::
    \begin{aligned}
        F_0 &= 0 \\
        F_1 &= 1 \\
        F_{n+2} &= F_{n+1} + F_n
    \end{aligned}

Example: using this definition to calculate the third Fibonacci number:

.. math::
    \begin{aligned}
        F_0 &= 0 \\
        F_1 &= 1 \\
        F_2 &= F_1 + F_0 = 1 + 0 = 1 \\
        F_3 &= F_2 + F_1 = 1 + 1 = 2
    \end{aligned}

This process can be completed to calculate the nth Fibonacci number, but it can
involve a lot of steps. We will use the relationship above to derive a formula
that will calculate the nth Fibonacci number. 

Finding the Generating Function
-------------------------------

To do this we will make use of generating functions and the formula for the sum
of an infinite geometric series:

.. math::
    \begin{aligned}
        \sum_{n=0}^\infty ax^n = a + ax + ax^2 + ax^3 + ax^4 + \cdots
            = \frac{a}{1-x} && (|x| < 1)
    \end{aligned}

We will start by defining the generating function and finding a closed form for
it. Then, we will take that closed form and express it as the sum of an infinite
geometric series. These two expressions will be equal by construction, meaning
that the coefficients of corresponding powers of :math:`x` will be equal in both
expressions. Importantly this applies to the general :math:`n` th term, which
will equate :math:`F_n` to its closed form.

We will define our generating function as:

.. math::
    \begin{aligned} F(x) &= \sum_{n=0}^\infty F_nx^n \\
        &= F_0x^0 + F_1x^1 + F_2x^2 + F_3x^3 + F_4x^4 + F_5x^5 + \cdots \\
        &= 0 + x + x^2 + 2x^3 + 3x^4 + 5x^5 + \cdots
    \end{aligned}

In our function, the variable :math:`x` will be treated as a formal variable. It
is there purely to assist with algebraic manipulation. Through our calculation
we will find constraints on the values that x could take e.g. :math:`(|x|<1)`.
Our final goal doesn't require :math:`x` to have any specific values so we can
and will assume :math:`x` has a value that satisfies those constraints.

Start by extracting the first two terms from the generating function:

.. math::
    F(x) = 0 + x + \sum_{n=2}^\infty F_nx^n 

Next, we will reindex the sum:

.. math::
    \begin{aligned}
        \text{Change } n &\to n+2 \\
        \text{Sum limit } n+2 &= 2 \\
        n &= 0 \\
        F(x) &= x + \sum_{n=0}^\infty F_{n+2}x^{n+2}
    \end{aligned}

Apply the recurrence relation to :math:`Fn+2` and split into separate sums:

.. math::
    \begin{aligned}
        F(x) &= x + \sum_{n=0}^\infty F_{n+2}x^{n+2} \\
        &= x + \sum_{n=0}^\infty (F_{n+1} + F_n)x^{n+2} \\
        &= x + \sum_{n=0}^\infty F_{n+1}x^{n+2}
            + \sum_{n=0}^\infty F_nx^{n+2}
    \end{aligned}

Factorise :math:`x` out of each sum so that the exponent for :math:`x` matches
the subscript for :math:`F`:

.. math::
    \begin{aligned}
        F(x) &= x + \sum_{n=0}^\infty F_{n+1}x^{n+2}
                + \sum_{n=0}^\infty F_nx^{n+2} \\
        &= x + x\sum_{n=0}^\infty F_{n+1}x^{n+1} + x^2\sum_{n=0}^\infty F_nx^n
    \end{aligned}

Now reindex the middle sum so that the exponent of :math:`x` and the subscript
of :math:`F` are both :math:`n`, then add :math:`F_0=0` back into the middle
sum:

.. math::
    \begin{aligned}
        F(x) &= x + x\sum_{n=0}^\infty F_{n+1}x^{n+1}
                + x^2\sum_{n=0}^\infty F_nx^n \\
        &= x + x\sum_{n=1}^\infty F_nx^n + x^2\sum_{n=0}^\infty F_nx^n
            && \text{(Reindex)} \\
        &= x + x\sum_{n=0}^\infty F_nx^n + x^2\sum_{n=0}^\infty F_nx^n
            && \text{(Add \(F_0 = 0\))}
    \end{aligned}

Notice that the second and third terms contain the original generating function
that we defined to be :math:`F(x)`. We will make that substitution and then
solve for :math:`F(x)`:

.. math::
    \begin{aligned}
        F(x) &= x + x\sum_{n=0}^\infty F_nx^n + x^2\sum_{n=0}^\infty F_nx^n \\
        &= x + xF(x) + x^2F(x) \\
        F(x) - xF(x) - x^2F(x) &= x \\
        (1 - x - x^2)F(x) &= x \\
        F(x) &= \frac{x}{1-x-x^2}
    \end{aligned}

Expressing as an Infinite Series
--------------------------------

We will need to manipulate the generating function to get it into a form that
can be directly converted to an infinite geometric series. To do this we will
factorise the denominator into factors of an appropriate form, and then use
partial fraction decomposition to break up the expression so that it can be
expanded as an infinite geometric series.

We will first assume that this is possible, and use the variables :math:`a`,
:math:`b`, :math:`A`, and :math:`B` as placeholders for values we will need to
calculate:

.. math::
    \begin{aligned}
        F(x) &= \frac{x}{1-x-x^2} \\
        &= \frac{x}{(1-ax)(1-bx)} && \text{(factorise denominator)} \\
        &= \frac{A}{1-ax} + \frac{B}{1-bx}
            && \text{(partial fraction decomposition)} \\
        &= A \sum_{n=0}^\infty(ax)^n + B \sum_{n=0}^\infty(bx)^n
            && \text{(sum of infinite geometric series)} \\
        &= \sum_{n=0}^\infty Aa^nx^n + \sum_{n=0}^\infty Bb^nx^n \\
        &= \sum_{n=0}^\infty(Aa^nx^n + Bb^nx^n) \\
        &= \sum_{n=0}^\infty(Aa^n + Bb^n)x^n
    \end{aligned}

We now have two expressions for :math:`F(x)`. Since they are both equal and
expressed as infinite series, we can extract coefficients to determine the form
of :math:`F_n`:

.. math::
    \begin{aligned}
        F(x) = \sum_{n=0}^\infty F_nx^n &= \sum_{n=0}^\infty(Aa^n + Bb^n)x^n \\
        \Rightarrow F_n &= Aa^n + Bb^n && \text{(extracting coefficients)}
    \end{aligned}

The Closed Formula
------------------

Now that we have the form of :math:`F_n` we need to detemine the values for
:math:`a`, :math:`b`, :math:`A`, and :math:`B`.

The first two values we will determine are :math:`a` and :math:`b`. From the
step where we factorised the denominator we have the following:

.. math::
    \begin{aligned}
        (1-ax)(1-bx) &= 1-x-x^2 \\
        1-(a+b)x + abx^2 &= 1-x-x^2
    \end{aligned}

Equating coefficients gives us the following system of equations to solve:

.. math::
    \begin{cases}
        a+b &= 1 \\
        ab &= -1
    \end{cases}

Solving this system:

.. math::
    \begin{aligned}
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
    \end{aligned}

The system of equations is symmetric in :math:`a` and :math:`b`, meaning we
could swap their values with no effect. Also, when :math:`a` is assigned one of
the roots, :math:`b` has the value of the other. These two facts together
indicate we have free choice in which root we assign to :math:`a` and :math:`b`,
so we will assign the positive root to :math:`a`.

.. math::
    \begin{aligned}
        a = \frac{1 + \sqrt5}{2}
        && b = \frac{1 - \sqrt5}{2}
    \end{aligned}

This leaves :math:`A` and :math:`B` left to determine. From our partial fraction
decomposition step we have:

.. math::
    \begin{aligned}
        \frac{x}{(1-ax)(1-bx)} &= \frac{A}{1-ax} + \frac{B}{1-bx} \\
        x &= A(1-bx) + B(1-ax) \\
        x &= (-Ab-Ba)x + (A+B)
    \end{aligned}

Equating coefficients of corresponding powers of :math:`x` on both sides of the
equation gives the following system of equations to be solved:

.. math::
    \begin{cases} -Ab-Ba &= 1 \\ A+B &= 0 \end{cases} 

Solving this system:

.. math::
    \begin{aligned}
        B &= -A \\
        -Ab-(-A)a &= 1 \\
        -Ab+Aa &= 1 \\
        A(a-b) &= 1 \\
        A &= \frac{1}{a-b} \\
        &= \frac{1}{\frac{1 + \sqrt5}{2} - \frac{1 - \sqrt5}{2}} \\
        &= \frac{1}{\sqrt5} \\
        B &= -A \\
        &= -\frac{1}{\sqrt5}
    \end{aligned}

We were able to determine values for all four of our placeholder variables with
no contradictions, indicating we do have a closed form. Now all that's required
is to substitute them into our formula for :math:`F_n`:

.. math::
    \begin{aligned}
        F_n &= Aa^n + Bb^n \\
        &=\left(\frac{1}{\sqrt5}\right) \left(\frac{1 + \sqrt5}{2}\right)^n
            + \left(-\frac{1}{\sqrt5}\right)\left(\frac{1 - \sqrt5}{2}\right)^n \\
        &= \frac{1}{\sqrt5}\left(\left(\frac{1+\sqrt5}{2}\right)^n
            - \left(\frac{1-\sqrt5}{2}\right)^n\right)
    \end{aligned}
