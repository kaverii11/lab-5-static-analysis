# Lab 5: Static Code Analysis Report

This repository contains the work for Lab 5, demonstrating the use of Pylint, Bandit, and Flake8 to analyze and improve a Python application.

## Deliverables

* **Original Code:** `inventory_system.py`
* **Cleaned Code:** `inventory_system_fixed.py`
* **Analysis Reports:**
    * `pylint_report.txt`
    * `bandit_report.txt`
    * `flake8_report.txt`

---

## [cite_start]Issue Identification Table [cite: 35]

Here is a summary of the major issues identified and fixed (at least 4 are required).

| Issue | Tool(s) | Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- |
| **Mutable Default Argument** | Pylint | `12` | The `logs=[]` argument is mutable and shared across all function calls, causing logs to merge. | Changed default to `logs=None` and initialized a new list `[]` inside the function if `logs` is `None`. |
| **Use of `eval`** | Bandit | `62` | `eval()` is a high-risk security vulnerability (B307) that allows arbitrary code execution. | Replaced the `eval()` call with a standard `print()` function to achieve the same output safely. |
| **Broad Exception Clause** | Pylint | `21` | `except:` catches all errors, hiding bugs and preventing clean exits. | Replaced the bare `except:` with `except KeyError:` to specifically handle cases where a non-existent item is removed. |
| **Missing Context Manager** | Pylint | `28, 33` | Files were opened with `open()` but not `close()`. Using `with open(...)` ensures files are closed automatically. | Refactored `loadData` and `saveData` to use the `with open(...) as f:` syntax. |
| **Multiple Imports on One Line** | Flake8 | `1` | `import json, logging, datetime` violates PEP 8 (E401). | Split each import onto its own line. |
| **Missing `if __name__ == "__main__"`** | Pylint | `64` | The script executes `main()` when imported as a module. | Wrapped the `main()` call in an `if __name__ == "__main__":` block. |

---

## Reflection Questions [cite: 36, 83]

(Add your answers here)

**1. Which issues were the easiest to fix, and which were the hardest? [cite_start]Why?** [cite: 85]
> *Your answer here. (e.g., The Flake8 style issues like imports were easiest. The mutable default argument was hardest because it's a logical bug, not just syntax.)*

**2. [cite_start]Did the static analysis tools report any false positives?** [cite: 86]
> *Your answer here. (e.g., Pylint might flag variable names as 'invalid-name' if they are short, but sometimes short names like 'qty' are acceptable.)*

**3. [cite_start]How would you integrate static analysis tools into your actual software development workflow?** [cite: 87, 88]
> *Your answer here. (e.g., I would use them as a pre-commit hook to check my code before I even commit it. I would also add them to a CI/CD pipeline, like GitHub Actions, to automatically fail any build that introduces new high-severity issues.)*

**4. [cite_start]What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?** [cite: 89]
> *Your answer here. (e.g., The code is now safer (no `eval`), more robust (no bare `except`), and more predictable (fixed the `logs=[]` bug). It's also cleaner and easier to read.)*