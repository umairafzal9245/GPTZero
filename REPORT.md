# Report

On using CodeQL analysis on our Github reopsitory, the output summary metric inclded:

- Lines of code in the codebase (used as a baseline), before creation and extraction of the CodeQL database
- Lines of code in the CodeQL database extracted from the code, including external libraries and auto-generated files
- Lines of code in the CodeQL database excluding auto-generated files and external libraries

---

The first thing to be seen was a log of **Extracting python** that gives a very large result of python files and packacges being checked.

Then **Finalizing pyhton** , **Running quesries for pyhton** and finally **Interpreting results for python**

The metric data produced by analysis was:

| Metric                                                  | Value       |
| ------------------------------------------------------- | ----------- |
| Total lines of Python code in the database              | **1480899** |
| Total lines of user written Python code in the database | **298**     |

<br>

Counted a baseline of **297** lines of code for python.

![Output 1](https://drive.google.com/uc?id=18h2Z2JDnDLbwY8UW0h6_SgxwmBSx2nug)

<br>

## Conclusion

The cinclusion of thr analysis is that there is no such vulnerability in the code present in out repository.

<br>

![Example Image](https://drive.google.com/uc?id=11Wr5bkwKlYT75LI_ZBKMk7HHuVMh9k7z)
