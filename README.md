# Profiling

**Idea:** Use profiling to assess the impact of polymorphism on the performance of Python programs.

Benchmarks of similar Java code in [advasileva/benchmarks](https://github.com/advasileva/benchmarks)

## Impelentations

We have written 3 implementations that give the same result, but with different logic of method calls

**First case:** There is a mutable object `c` with the field `p`, which contains an object with the method `price()`.
This method is called to repeatedly calculate `total()`. 
In this case, `p` alternately contains objects of the `Book` and `Movie` classes inherited from `Product`.

```python
c = Cart(Book("1984"))
c.p = Movie("Godfather")
for i in range(100000000):
    c.total()
```

**Second case:** We use the immutable `Cart1` and `Cart2` here instead of `Cart`. The rest of the logic is similar.

```python
c1 = Cart1(Book("1984"))
c2 = c1.withMovie(Movie("Godfather"))
for i in range(100000000):
    c2.total()
```

**Third case:** In this case, we replaced `Book` and `Movie` with `Book1` and `Movie1`, which are not inherited from `Product` and use their own `price()`.

```python
c1 = Cart1(Book1("1984"))
c2 = c1.withMovie(Movie1("Godfather"))
for i in range(100000000):
    c2.total()
```

## Results

Case | Total time | `total()` exec time | `price()` exec time
------ | ------ | ------ | ------
`case1.py` | `144s` | `90.3s` | `23.8s`
`case2.py` | `144s` | `89.7s` | `23.2s`
`case3.py` | `120s` | `75.2s` | `18.5s`

Similar results for the first and second cases are expected due to Python dynamic typing (we have not simplified the function call).

In the third case, the code runs faster because calling its own method is faster than calling the methods of the base class.

## Usage

Install snakeviz:
```bash
make init
```

Start profiling 3 cases:
```bash
make profile
```

Visualize the results in the browser:
```bash
make viz
```

