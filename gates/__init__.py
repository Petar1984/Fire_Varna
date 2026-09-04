"""Fire_Varna gates — objective, machine-checkable checks that run before a push.

The package is deliberately dependency-free (standard library only, Python 3.10)
and never imports from `tests/`: a gate that shares code with the suite it guards
cannot fail independently of it.
"""
