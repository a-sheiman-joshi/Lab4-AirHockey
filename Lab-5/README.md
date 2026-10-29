# Lab 5: Static Code Analysis — Retail Point of Sale & Discount Tracker

**Student:** A Sheiman Joshi  
**SRN:** PES2UG24CS003  
**Source Repository:** https://github.com/SETAPESU26/L5_02_retail_pos  

---

## Deliverables Checklist

- [x] **`pos_system.py`**: Cleaned, production-ready POS script with all security, style, and logic issues resolved.
- [x] **`issues.md`**: Completed issue documentation table (High/Medium severity first) with detailed fix approaches.
- [x] **`reflection.md`**: Detailed answers to the four reflection questions on static analysis tools, Python anti-patterns, security vulnerabilities, and CI/CD integration.
- [x] **`pos_system_original.py`**: Original starter script for side-by-side comparison.
- [x] **Static Analysis Reports**:
  - `pylint_report.txt` (Final score: **10.00 / 10.00**)
  - `bandit_report.txt` (Final: **0 issues identified**)
  - `flake8_report.txt` (Final: **0 style violations / Clean**)
  - Initial before-fix reports: `pylint_report_before.txt` (5.65/10), `bandit_report_before.txt` (3 issues), `flake8_report_before.txt` (12 errors).

---

## Verification & Tool Scores

| Tool | Before Refactor | After Refactor | Target | Status |
|---|---|---|---|---|
| **Pylint** | 5.65 / 10.00 | **10.00 / 10.00** | > 9.50 | **Exceeded (Perfect Score)** |
| **Bandit** | 3 Issues (Medium: `eval`, Low: `pass`, `random`) | **0 Issues** | 0 Security Flaws | **Passed** |
| **Flake8** | 12 Errors (bare except, lines > 79, unused imports) | **0 Errors** | Clean PEP 8 | **Passed** |

---

## How to Run & Verify

1. **Activate virtual environment & install tools:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install pylint bandit flake8
   ```

2. **Execute the POS system:**
   ```bash
   python pos_system.py
   ```

3. **Run Static Analysis:**
   ```bash
   pylint pos_system.py
   bandit -r pos_system.py
   flake8 pos_system.py
   ```
