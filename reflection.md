
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
