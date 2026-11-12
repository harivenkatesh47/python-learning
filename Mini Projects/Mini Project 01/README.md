# MediCore — Smart Clinic Triage & Pharmacy Billing Engine

## 1. Overview & Problem Statement
Hospitals and clinics often struggle with disconnected workflows between patient registration, vital-sign triage, doctor consultation hierarchies, and pharmacy billing[cite: 1]. Staff frequently encounter unstructured patient text, duplicate allergy records that create severe medication risks, emergency cases stuck behind routine checkups, and complex pharmacy invoices requiring GST, insurance callbacks, and exact cash-change calculations[cite: 1].

**MediCore** is a modular, multi-file Python console application that solves these operational bottlenecks[cite: 1]. Designed strictly using core procedural Python (Modules 01 through 09—without OOP, file I/O, or comprehensions), it sanitizes patient records, audits drug allergies using mathematical set algebra, prioritizes emergency queues using multi-factor telemetry, traverses specialist referral trees recursively, and processes pharmacy invoices with functional callbacks and deep-copied inventory simulations[cite: 1].

---

## 2. Project Architecture & File Structure
To enforce strict separation of concerns and namespace isolation, the project is architected across three distinct Python modules[cite: 1]:

```text
medicore_project/
├── medicore_config.py   # Database, baseline dictionaries, matrices, & constants
├── medicore_engine.py   # Core business logic, algorithms, & functional pipelines
├── medicore_cli.py      # Interactive terminal driver & visual display engine
└── README.md            # Project documentation
```

### Module Breakdown
1. **`medicore_config.py` (Database & Constants Module):**
   * Stores mutable operational state (`total_patients_served`, `triage_queue`, `daily_invoices`, `consultation_durations`)[cite: 1].
   * Defines the $3 \times 3$ 2D ICU bed matrix (`icu_bed_matrix`) and tuple-keyed bed registry (`bed_assignments`)[cite: 1].
   * Holds the `pharmacy_catalog` dictionary, `frozenset` insurance tier rules, and nested `department_hierarchy` referral tree[cite: 1].
   * Includes an isolated unit self-test block guarded by `if __name__ == "__main__":`[cite: 1].
2. **`medicore_engine.py` (Core Business Logic Module):**
   * Houses UI-agnostic processing functions for text redaction, BMI and triage evaluation, set-based allergy cross-checking, recursive specialist lookup, and higher-order billing[cite: 1].
3. **`medicore_cli.py` (Interactive Driver Script):**
   * Demonstrates all three Python import styles (`import ... as ...`, `from ... import ...`, and standard `import`)[cite: 1].
   * Runs a persistent `while True` reception menu with defensive `try-except ValueError` input validation and visual ASCII bar charts[cite: 1].

---

## 3. Core Features & Interactive Workflows
Running `medicore_cli.py` launches an interactive 7-option terminal menu covering six core clinical workflows[cite: 1]:

1. **Patient Onboarding, Sanitization & Vital Triage:**
   * Cleans raw patient names and validates Government Health IDs (`ABHA-YYYY-XXXX-IN`) using prefix/suffix checks, string slicing, and string reversal hashes[cite: 1].
   * Scans clinical notes for confidential terms (`hiv`, `psychiatric`), counts occurrences, and redacts them with `[REDACTED-PHI]`[cite: 1].
   * Computes Body Mass Index (BMI) and routes patients into `CODE RED`, `CODE YELLOW`, or `CODE GREEN` tiers, pushing `CRITICAL` cases to index `0` of the triage queue[cite: 1].
2. **Allergy Set Algebra & Prescription Safety Auditor:**
   * Ingests arbitrary medication lists via `*args` and custom regimen instructions via `**kwargs`[cite: 1].
   * Uses a `for-else` loop to verify stock levels across the pharmacy catalog[cite: 1].
   * Applies mathematical set operations (`&` Intersection, `|` Union, `-` Difference) between patient allergies and drug ingredients to detect life-threatening contraindications[cite: 1].
3. **ICU 2D Matrix Manager & Visual Occupancy Monitor:**
   * Displays the $3 \times 3$ nested list representing 3 ICU wards and 3 beds per ward (`1` = Occupied, `0` = Empty)[cite: 1].
   * Renders a nested-loop `*` bar chart of ward occupancy and allows live admission/discharge state updates using tuple coordinates `(ward, bed)`[cite: 1].
4. **Recursive Specialist Referral Escalation Lookup:**
   * Recursively traverses the nested `department_hierarchy` dictionary tree to locate the exact medical unit and lead specialist for a given condition while tracking call-stack referral depth[cite: 1].
5. **Pharmacy GST Pipeline, Callbacks & Cash Breakdown:**
   * Clones the master `pharmacy_catalog` using `copy.deepcopy()` so simulated stock deductions do not corrupt live inventory[cite: 1].
   * Applies a `map()` + `lambda` pipeline to compute 12% Medical GST and a `filter()` + `lambda` check to flag low-stock drugs ($\le 5$ units)[cite: 1].
   * Dispatches first-class insurance callback functions (`govt_cghs_discount`, `corporate_insurance_discount`, `senior_citizen_discount`)[cite: 1].
   * Uses floor division (`//`) and modulus (`%`) to break down the final payable amount into exact ₹500 notes, ₹100 notes, loose rupees, and paise[cite: 1].
6. **Day-End Analytics & Queue Sorter:**
   * Displays the `global` patient counter, computes gross revenue and invoice extremes manually via loop accumulators, and sorts consultation wait times in descending order[cite: 1].

---

## 4. Python Concepts Mapped (Modules 01 – 09)
* **Module 01–03 (Basics & Math):** Type casting (`int`, `float`), exponentiation (`**`), floor division (`//`), modulus (`%`), `round()`, `math`, and `random.randint()`[cite: 1].
* **Module 04 (Strings):** `.strip()`, `.title()`, `.lower()`, `.upper()`, `.startswith()`, `.endswith()`, `.count()`, `.replace()`, slicing (`[5:9]`, `[::-1]`), f-strings, and escape sequences (`\n`, `\t`, `\"`)[cite: 1].
* **Module 05 (Lists & 2D Grids):** `.append()`, `.insert(0, ...)`, `.copy()`, `.sort()`, `.reverse()`, `sum()`, `len()`, and $3 \times 3$ nested list indexing (`icu_bed_matrix[w][b]`)[cite: 1].
* **Module 06 (Tuples, Sets & Dicts):** Tuple packing/unpacking, single-element tuple concatenation (`("VERIFIED",)`), tuple dictionary keys, set algebra (`&`, `|`, `-`), `.add()`, `.discard()`, `frozenset()`, dictionary `.get()`, `.pop()`, `.keys()`, and `copy.deepcopy()`[cite: 1].
* **Module 07 (Control Flow):** Multi-tier `if-elif-else` triage ladders, compound boolean precedence, nested validation checks, and single-line ternary operators[cite: 1].
* **Module 08 (Loops):** Persistent `while True` CLI menu, `continue` / `break` flow control, `for-else` stock verification loops, manual min/max loop accumulators, and nested loops for visual charts[cite: 1].
* **Module 09 (Functions & Modules):** Modular 3-file separation, `global` state tracking, multiple tuple returns, `*args` & `**kwargs`, recursion with depth tracking, first-class function callbacks, `lambda` with `map()` / `filter()`, and `if __name__ == "__main__":` entry-point guards[cite: 1].

---

## 5. How to Run Locally
1. Ensure all three project files (`medicore_config.py`, `medicore_engine.py`, and `medicore_cli.py`) are saved inside the same directory[cite: 1].
2. Open your terminal and navigate to the project folder[cite: 1]:
   ```bash
   cd path/to/medicore_project
   ```
3. *(Optional)* Run the configuration module directly to verify its standalone self-test guard[cite: 1]:
   ```bash
   python medicore_config.py
   ```
4. Launch the main interactive clinic application[cite: 1]:
   ```bash
   python medicore_cli.py
   ```