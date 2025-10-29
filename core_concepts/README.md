# Python Core Concepts: Building Blocks

This guide covers Python's foundational building blocks: variables, data types, operators, and expressions. You'll work with strings, numbers, and booleans, perform type conversions, and use formatted strings (f-strings) for clean, expressive output. Each section includes examples, tips, and mini exercises.

## Table of Contents
1. Introduction
2. Variables
3. Data Types Overview
4. Numbers (int & float)
5. Booleans & Truthiness
6. Strings
7. Operators
   - Arithmetic
   - Comparison
   - Logical (Boolean)
   - Assignment & Augmented Assignment
   - Membership & Identity (bonus)
8. Expressions
9. Type Conversion (Casting)
10. Formatted Strings (f-strings)
11. Common Pitfalls & Best Practices
12. Mini Exercises
13. Summary & Next Steps

---

## 1. Introduction
Python code is a series of expressions and statements that operate on data. Understanding how Python stores values (variables), categorizes them (data types), manipulates them (operators), and combines them (expressions) is essential for everything you build later.

## 2. Variables
A variable is a name bound to a value in memory. In Python, assignment both creates and updates the binding.

```python
message = "Hello"      # create variable 'message'
count = 3               # create variable 'count'
count = count + 1       # update using previous value
```

Guidelines:
- Use snake_case: `user_name`, `total_distance`.
- Choose descriptive names: `total_price` > `tp`.
- Avoid shadowing built-ins (e.g., don't name a variable `list`, `str`, or `sum`).

Multiple assignment:
```python
x, y = 10, 20
```
Chained assignment (same object reference):
```python
a = b = 0
```

Swapping values (Pythonic):
```python
a, b = b, a
```

## 3. Data Types Overview
Core immutable types you'll use immediately:
- `int` – whole numbers: `0`, `-5`, `42`
- `float` – decimal numbers: `3.14`, `0.0`, `-2.5`
- `bool` – truth values: `True`, `False`
- `str` – text: `"Python"`, `'AI'`

You can inspect a type with `type(value)`.

```python
type(42)        # <class 'int'>
type(3.14)      # <class 'float'>
type(True)      # <class 'bool'>
type("hello")  # <class 'str'>
```

## 4. Numbers (int & float)
Arithmetic is straightforward:
```python
5 + 2      # 7
5 - 2      # 3
5 * 2      # 10
5 / 2      # 2.5   (float division)
5 // 2     # 2     (floor division)
5 % 2      # 1     (remainder)
5 ** 2     # 25    (power)
```

Integer division vs floor division:
- `/` always returns a float.
- `//` performs floor division (toward negative infinity for negatives): `-3 // 2 == -2`.

Floating point precision:
```python
0.1 + 0.2 == 0.3      # False (binary floating point rounding)
```
Mitigation: use `round()` or the `decimal` module when exact decimal is required.

Numeric conversion:
```python
int(3.9)     # 3 (truncates toward zero)
float(5)     # 5.0
```

## 5. Booleans & Truthiness
Booleans result from comparisons or logical operations.
```python
is_ready = True
result = 5 > 2          # True
```

Truthiness: In boolean contexts, Python treats certain values as False:
- `False`, `0`, `0.0`, `""` (empty string), `None`, empty containers (`[]`, `{}`, `()`, `set()`). Everything else is True.

```python
if "hello":
	print("Non-empty strings are truthy")
```

## 6. Strings
Strings are sequences of Unicode characters (immutable).
Creation:
```python
single = 'Hi'
double = "Hi"
multi_line = """Line1\nLine2"""
```

Concatenation & repetition:
```python
"Py" + "thon"     # 'Python'
"ha" * 3          # 'hahaha'
```

Indexing & slicing (0-based):
```python
text = "Python"
text[0]       # 'P'
text[-1]      # 'n' (last char)
text[1:4]     # 'yth'
text[:2]      # 'Py'
text[2:]      # 'thon'
text[::2]     # 'Pto'
```

Immutability: you cannot modify in place.
```python
text[0] = 'J'   # TypeError
```
Instead build a new string:
```python
"J" + text[1:]  # 'Jython'
```

Useful methods:
```python
"python".upper()        # 'PYTHON'
"Python".lower()        # 'python'
"  spaced  ".strip()   # 'spaced'
"a,b,c".split(',')      # ['a', 'b', 'c']
"-".join(['a','b'])     # 'a-b'
"Python".startswith("Py")  # True
"Python".replace("Py", "My") # 'Mython'
```

Escapes & raw strings:
```python
path = "C:\\new\\folder"   # escape backslashes
raw_path = r"C:\new\folder" # raw string leaves backslashes
```

## 7. Operators
Operators perform actions on operands (values/variables).

### Arithmetic
`+ - * / // % **`

### Comparison
`== != < <= > >=` return booleans.
```python
5 == 5    # True
"a" != "b"  # True
3 < 10    # True
```

String comparisons are lexicographical (Unicode code point order):
```python
"apple" < "banana"   # True
```

### Logical (Boolean)
`and` (both True), `or` (either True), `not` (negates).
Short-circuit behavior:
```python
expr = expensive() and cheap()  # 'cheap()' only runs if expensive() returned truthy
```

`and` / `or` return one of the original operands (not coerced to strictly True/False):
```python
[] or "fallback"    # 'fallback'
"data" and 123      # 123
```

### Assignment & Augmented Assignment
Basic: `name = value`
Augmented: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`
```python
total = 10
total += 5    # 15
```

### Membership (bonus)
`in` / `not in` check containment.
```python
"Py" in "Python"    # True
"java" not in "Python"  # True
```

### Identity (bonus)
`is` / `is not` compare object identity (same memory reference), not equality.
```python
a = [1]
b = [1]
a == b      # True (values equal)
a is b      # False (distinct lists)
```
Use `is` for singletons like `None`:
```python
if value is None:
	...
```

## 8. Expressions
An expression produces a value: `2 + 3`, `len("abc")`, `user_age > 18`. Statements may contain expressions (e.g., `if user_age > 18:`). Breaking complex expressions into parts improves readability.

Operator precedence (high to low, simplified):
1. `**`
2. Unary `+ - not`
3. `* / // %`
4. `+ -`
5. Comparisons
6. `not`
7. `and`
8. `or`
Use parentheses to be explicit.

## 9. Type Conversion (Casting)
Explicit casting functions:
- `int(x)` – to integer (floats truncated, numeric strings accepted)
- `float(x)` – to float
- `str(x)` – to string representation
- `bool(x)` – to boolean (based on truthiness)

Examples:
```python
int("42")        # 42
float("3.5")     # 3.5
str(3.14)         # '3.14'
bool("hello")     # True
bool(0)           # False
```

Failed conversions raise `ValueError`:
```python
int("4.2")   # ValueError (string has decimal point)
```
Workaround: convert to float first or parse differently: `int(float("4.2"))`.

Implicit conversions (coercion) happen in mixed numeric operations:
```python
3 + 4.5    # 7.5 (int promoted to float)
```

## 10. Formatted Strings (f-strings)
Introduced in Python 3.6, f-strings let you embed expressions inside string literals for clean formatting.
```python
name = "Ada"
score = 92.456
print(f"Student {name} scored {score}")
```

Expression support:
```python
print(f"Next year: {2025 - 1 + 1}")
print(f"Upper: {name.upper()}")
```

Formatting specifiers after a colon:
```python
print(f"Score rounded: {score:.2f}")   # 2 decimal places
pi = 3.1415926535
print(f"Pi scientific: {pi:.3e}")
print(f"Pad left: {42:>5}")            # '   42'
print(f"Pad right: {42:<5}")           # '42   '
print(f"Pad center: {42:^5}")          # ' 42  '
```

Debugging helper (Python 3.8+):
```python
value = 123
print(f"{value=}")  # prints 'value=123'
```

Escaping braces:
```python
print(f"{{braces}}")  # {braces}
```

Contrast with older approaches:
```python
"Name: {} Score: {:.2f}".format(name, score)
"Name: %s Score: %.2f" % (name, score)  # %-formatting (legacy)
```

## 11. Common Pitfalls & Best Practices
- Floating point precision surprises: use `round()` or `decimal.Decimal` for currency.
- Integer division confusion: remember `/` vs `//`.
- Using `is` instead of `==` for value comparison (incorrect except for singletons like `None`).
- Shadowing built-ins (`list`, `str`, `id`, `sum`). Pick alternative names like `items_list`, `text_value`.
- Forgetting string immutability: methods return new strings.
- Misusing truthiness: `if len(items) > 0:` can be `if items:`.
- Converting risky input: wrap casts in `try/except` for user input.

Naming & readability:
- Prefer explicit over implicit: `total_price = quantity * unit_price` beats `tp = q * up`.
- Keep expressions small; assign intermediate results to named variables.

## 12. Mini Exercises
Try these in a REPL or script:
1. Create variables `first`, `last`, and combine them with a space using an f-string.
2. Given `radius = 3`, compute area of a circle (`pi * r**2`) showing 3 decimal places.
3. Write an expression that returns `'adult'` if `age >= 18` else `'minor'` using a conditional expression.
4. Safely convert `user_input = "19"` to an int and add 1; handle a failing input like `"19.5"` with a graceful message.
5. Show the difference between `a == b` and `a is b` for two identical lists.
6. Slice the string `s = "unboxed"` to produce `"box"`.
7. Demonstrate truthiness by filtering a list: `values = [0, 1, "", "hi", [], [1]]` keep only truthy values.
8. Format a number `n = 5` as padded to width 4: `'   5'` and centered: `' 5  '`. Use f-strings.
9. Given `temp_c = 23.456`, create `"Temp: 23.46°C"` (rounded) with an f-string.
10. Show why `0.1 + 0.2 != 0.3` and use `round()` to compare.

## 13. Summary & Next Steps
You now understand how Python stores and manipulates basic data. Mastery of these primitives lets you progress to collections (lists, tuples, dicts, sets), control flow (if/for/while), and functions. Practice by rewriting snippets using f-strings, breaking complex expressions, and experimenting with truthiness.

Continue to the next section: Virtual Environments (managing project dependencies) found in `../virtual_environments/README.md`.

---
Revision: 2025-10-29

