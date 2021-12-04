# raise.py

# raise
try:
    raise ValueError
except Exception as e:
    raise IndexError
"""
Traceback (most recent call last):
  File "raise.py", line 3, in <module>
    raise ValueError
ValueError

# 在处理上面的异常时，发生了另外一个异常：
During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "raise.py", line 5, in <module>
    raise IndexError
IndexError
"""

# raisefrom.py

# raise/from
try:
    raise ValueError
except Exception as e:
    raise IndexError from e
"""
Traceback (most recent call last):
  File "raisefrom.py", line 3, in <module>
    raise ValueError
ValueError

# 上面的异常是接下来的异常的直接原因：
The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "raisefrom.py", line 5, in <module>
    raise IndexError from e
IndexError
"""

# raise 会设置后面异常的 __context__ 属性为前面的异常。
# raise A异常 from B异常 会把 A异常 的 __cause__ 属性设置为 B异常。
# raise A异常 from None 会设置 A异常 的 __suppress_context__ 属性为 True，这样会忽略它的 __context__ 属性，不会自动显示异常上下文信息。