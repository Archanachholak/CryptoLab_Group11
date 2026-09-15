# Lab Assignment 4 — SAST Security Analysis

## Objective

Perform **Static Application Security Testing (SAST)** on the `CryptoLabX` secure application, identify vulnerabilities, compare findings with Assignment 3, remediate them, and verify the fixes using a second SAST scan.

## SAST Tool

* **Tool:** Flawfinder
* **Language:** C/C++
* **Target:** `secure_application/src/`

## Tasks Performed

* Scanned the complete source code using SAST.
* Saved the original SAST output without modification.
* Analyzed reported vulnerabilities and their severity.
* Compared SAST findings with vulnerabilities introduced in Assignment 3.
* Classified findings as:

  * **TP** — True Positive
  * **FP** — False Positive
  * **MV** — Missed Vulnerability
* Identified and analyzed at least one missed vulnerability.
* Remediated the identified vulnerabilities.
* Performed a second SAST scan to verify the fixes.
* Documented before-and-after results.

## Repository Structure

```text
secure_application/
├── src/                  # Source code
├── reports/              # SAST and remediation reports
├── screenshots/
│   ├── sast_initial/     # Screenshots before fixes
│   └── sast_after_fix/   # Screenshots after fixes
├── sast/
│   ├── config/           # SAST configuration
│   ├── raw_output/       # Original SAST output
│   └── README.md
├── outputs/              # Program outputs
├── testcases/            # Test cases
└── README.md
```

## Analysis Workflow

```text
Source Code
     ↓
Initial SAST Scan
     ↓
Analyze Findings
     ↓
Compare with Assignment 3
     ↓
Identify TP / FP / MV
     ↓
Remediate Vulnerabilities
     ↓
Second SAST Scan
     ↓
Verify Fixes
```

## Reports

* `sast_initial_report.pdf` — Initial SAST findings
* `vulnerability_analysis.pdf` — Analysis and classification of vulnerabilities
* `remediation_report.pdf` — Fixes and before/after comparison

## Conclusion

SAST was used to identify security weaknesses in the application. The findings were manually analyzed, compared with known vulnerabilities, remediated, and verified through a second scan. The exercise demonstrates both the usefulness and limitations of automated static security analysis.
