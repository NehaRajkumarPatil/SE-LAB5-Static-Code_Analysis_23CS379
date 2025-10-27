# 🧩 Lab 5: Static Code Analysis

**Name:** Neha Rajkumar Patil  
**Course:** Software Engineering Laboratory  
**Lab Title:** Static Code Analysis using Pylint, Bandit, and Flake8  

---

##  Objective
To enhance Python code quality, security, and maintainability by using static analysis tools — **Pylint**, **Bandit**, and **Flake8** — to identify, document, and fix issues in `inventory_system.py`.

---

## Learning Outcomes
By completing this lab, I was able to:
- Understand the role of static analysis in detecting bugs and vulnerabilities.  
- Identify and fix common Python issues such as mutable default arguments, insecure functions, and poor exception handling.  
- Use **Pylint**, **Bandit**, and **Flake8** effectively to analyze and improve code quality.  
- Interpret static analysis reports and apply appropriate fixes.  
- Reflect on the impact of static analysis in improving software reliability.

---

## Verification Summary

| **Tool** | **Result** | **Status** |
|-----------|-------------|------------|
| **Pylint** | 10.00 / 10 | All issues resolved |
| **Bandit** | No issues identified | Secure |
| **Flake8** | No warnings or errors | Style compliant |

---

## Reflection Questions

### 1. Which issues were the easiest to fix, and which were the hardest?
The **easiest fixes** were PEP 8 style violations, such as adding blank lines, renaming functions, and removing unused imports.  
The **hardest fix** was replacing `eval()` safely without losing functionality. I resolved it using `ast.literal_eval()` after researching its behavior.

---

### 2. Did the static analysis tools report any false positives?
No major false positives were found.  
Some warnings like “missing docstrings” or “global variable usage” were intentional during development but valid improvements later, enhancing code readability and structure.

---

### 3. How would you integrate static analysis tools into your actual development workflow?
I would integrate **Pylint**, **Bandit**, and **Flake8** into a **Continuous Integration (CI)** pipeline (e.g., GitHub Actions).  
Each commit or pull request would automatically run these tools, ensuring:
- Consistent code style (Flake8)  
- Secure coding (Bandit)  
- Logical and maintainable design (Pylint)

This automation maintains team-wide quality standards before deployment.

---

### 4. What improvements did you observe after applying the fixes?
After applying all fixes:
- The code became **cleaner, safer, and more readable**.  
- **Logging** improved traceability and debugging.  
- **Input validation** and **specific exception handling** made the program robust.  
- The program achieved **Pylint 10/10**, **no Bandit issues**, and **PEP 8 compliance** — reflecting high-quality, production-ready code.

---

## Final Outcome
All static analysis checks passed successfully.  
The final version of `inventory_system.py` is:
- **Secure**
- **Readable**
- **Fully PEP 8 compliant**
- **Free from common Python code smells**
