import medicore_config as cfg
import medicore_engine
from medicore_engine import (
    sanitize_patient_profile,
    compute_bmi_and_triage,
    audit_prescription_safety,
    find_specialist_escalation,
    process_pharmacy_billing,
    compute_manual_ledger_metrics
)


def render_ward_occupancy_chart():
    print("\n--- ICU 3x3 Bed Matrix & Visual Occupancy Bar Chart ---")
    for ward_idx in range(len(cfg.icu_bed_matrix)):
        row = cfg.icu_bed_matrix[ward_idx]
        occupied_count = 0
        bar_visual = ""
        for bed_state in row:
            if bed_state == 1:
                occupied_count += 1
                bar_visual += "* "
        print(f"\tWard {ward_idx + 1} Beds {row} | Occupied: {occupied_count}/3 | {bar_visual}")


def run_medicore_cli():
    print("==========================================================")
    print("   MEDICORE: SMART CLINIC TRIAGE & PHARMACY ENGINE        ")
    print("==========================================================")

    while True:
        print("\n--- Main Reception & Diagnostic Menu ---")
        print("1. Patient Onboarding, Sanitization & Vital Triage")
        print("2. Allergy Set Algebra & Prescription Safety Auditor")
        print("3. ICU 2D Matrix Manager & Visual Occupancy Monitor")
        print("4. Recursive Specialist Referral Escalation Lookup")
        print("5. Pharmacy GST Pipeline, Callbacks & Cash Breakdown")
        print("6. Day-End Analytics & Queue Sorter")
        print("7. Exit System")

        choice = input("\nSelect operation (1-7): ").strip()

        if not choice:
            continue

        if choice == "1":
            raw_name = input("Enter Patient Full Name: ")
            raw_abha = input("Enter ABHA ID (e.g., ABHA-2026-8841-IN): ")
            raw_notes = input("Enter Diagnostic Notes (mention 'hiv' or 'psychiatric' to test redaction): ")

            try:
                weight = float(input("Enter Weight (kg): "))
                height = float(input("Enter Height (meters, e.g., 1.75): "))
                sys_bp = int(input("Enter Systolic BP (mmHg): "))
                dia_bp = int(input("Enter Diastolic BP (mmHg): "))
                hr = int(input("Enter Heart Rate (bpm): "))
                spo2 = int(input("Enter SpO2 (%): "))
                temp = float(input("Enter Temperature (°F): "))
            except ValueError:
                print("\t[Input Error]: Numeric vitals required. Onboarding aborted.")
                continue

            if height <= 0 or weight <= 0:
                print("\t[Validation Error]: Height and weight must be positive.")
                continue

            token, name, abha_ok, yr, rev_hash, clean_notes, hits = sanitize_patient_profile(
                raw_name, raw_abha, raw_notes
            )
            bmi, vitals_tuple, code, prio_tag = compute_bmi_and_triage(
                weight, height, sys_bp, dia_bp, hr, spo2, temp
            )

            s_bp, d_bp, h_rate, o2_sat, v_flag = vitals_tuple
            entry_str = f"{token} | {name} | {prio_tag}"

            if prio_tag == "CRITICAL":
                cfg.triage_queue.insert(0, entry_str)
            else:
                cfg.triage_queue.append(entry_str)

            served_count, _ = medicore_engine.increment_patient_counter()

            print(f"\n--- Onboarding & Triage Receipt ({token}) ---")
            print(f"\tPatient Name      : \"{name}\"")
            print(f"\tABHA ID Valid     : {abha_ok} (Year: {yr} | RevHash: {rev_hash})")
            print(f"\tSanitized Notes   : {clean_notes} (Redactions: {hits})")
            print(f"\tCalculated BMI    : {bmi}")
            print(f"\tUnpacked Vitals   : BP {s_bp}/{d_bp} | HR {h_rate} | SpO2 {o2_sat}% [{v_flag}]")
            print(f"\tTriage Verdict    : {code} -> Assigned '{prio_tag}'")
            print(f"\tActive Queue      : {cfg.triage_queue}")
            print(f"\tTotal Served Today: {served_count}")

        elif choice == "2":
            raw_allergies = input("Enter known patient allergies (comma-separated, e.g., penicillin,lactose): ")
            allergy_list = [a.strip().lower() for a in raw_allergies.split(",")] if raw_allergies.strip() else []

            print(f"Available Catalog: {list(cfg.pharmacy_catalog.keys())}")
            m1 = input("Enter 1st Medicine to prescribe: ").strip()
            m2 = input("Enter 2nd Medicine to prescribe: ").strip()

            report = audit_prescription_safety(
                allergy_list, "Dr. A. Kulkarni", m1, m2, regimen="Post-Meal", duration_days=5
            )

            print("\n--- Set Algebra Contraindication Report ---")
            print(f"\tPrescribing Doctor : {report['doctor']}")
            print(f"\tMedications (*args): {report['prescribed_tuple']}")
            print(f"\tNotes (**kwargs)   : {report['instructions']}")
            print(f"\tStock Loop Check   : {report['stock_status']}")
            print(f"\tTotal Exposure (|) : {report['total_exposure']}")
            print(f"\tAllergy Clash (&)  : {report['allergy_clashes']}")
            print(f"\tSafe Compounds (-) : {report['safe_compounds']}")
            print(f"\tDispense Approved  : {report['is_safe']}")

        elif choice == "3":
            render_ward_occupancy_chart()
            print(f"Active Tuple-Key Bed Registry: {cfg.bed_assignments}")
            toggle = input("\nDo you want to update a bed status? (yes/no): ").strip().lower()
            if toggle == "yes":
                try:
                    w = int(input("Enter Ward Index (0-2): "))
                    b = int(input("Enter Bed Index (0-2): "))
                    state = int(input("Enter New State (1=Occupied, 0=Empty): "))
                    if 0 <= w <= 2 and 0 <= b <= 2 and state in (0, 1):
                        cfg.icu_bed_matrix[w][b] = state
                        if state == 1:
                            cfg.bed_assignments[(w, b)] = "PT-NEW (Admitted)"
                        else:
                            cfg.bed_assignments.pop((w, b), None)
                        render_ward_occupancy_chart()
                    else:
                        print("\t[Error]: Indices must be 0-2 and state 0 or 1.")
                except ValueError:
                    print("\t[Error]: Invalid integer input.")

        elif choice == "4":
            print("\nSample Conditions: fever, arrhythmia, pacemaker_fault, asthma, acute_hypoxia")
            cond = input("Enter condition for specialist escalation lookup: ").strip().lower()
            dept, doc, depth = find_specialist_escalation(cfg.department_hierarchy, cond)

            if dept is not None:
                print(f"\t[Escalation Match]: '{cond}' routed to {dept}")
                print(f"\t[Specialist Lead] : {doc} (Referral Tree Depth: {depth})")
            else:
                print(f"\t[Escalation Alert]: Condition '{cond}' not found in specialist tree.")

        elif choice == "5":
            print(f"\nAvailable Drugs: {list(cfg.pharmacy_catalog.keys())}")
            m1 = input("Select 1st Drug for Billing: ").strip().lower()
            m2 = input("Select 2nd Drug for Billing: ").strip().lower()
            scheme = input("Select Scheme (cghs / corporate / senior): ").strip().lower()

            bill = process_pharmacy_billing([m1, m2], scheme)
            n500, n100, loose_r, paise_c = bill["currency_breakdown"]

            cfg.daily_invoices.append(bill["net_payable"])

            print("\n--- Functional Pharmacy Invoice & Deepcopy Audit ---")
            print(f"\tBase Prices              : {bill['raw_prices']}")
            print(f"\tPost-12% GST (map+lambda): {bill['gst_prices']}")
            print(f"\tGross Amount             : ₹{bill['gross_total']:.2f}")
            print(f"\tCallback Discount Applied: -₹{bill['discount']:.2f}")
            print(f"\tNet Payable              : ₹{bill['net_payable']:.2f}")
            print(f"\tCash Breakdown (// & %)  : {n500}x₹500, {n100}x₹100, ₹{loose_r} loose, {paise_c} paise")
            print(f"\tLow Stock Alerts (filter): {bill['low_stock_alerts']}")
            print(f"\tDeepcopy Isolated Master : {bill['real_catalog_unchanged']}")

        elif choice == "6":
            gross, peak, low = compute_manual_ledger_metrics(cfg.daily_invoices)
            durations_copy = cfg.consultation_durations.copy()
            durations_copy.sort()
            durations_copy.reverse()

            print("\n=== Day-End Clinic Analytics ===")
            print(f"\tGlobal Patients Served : {cfg.total_patients_served}")
            print(f"\tInvoices Logged        : {len(cfg.daily_invoices)}")
            print(f"\tManual Gross Revenue   : ₹{gross:.2f}")
            print(f"\tPeak / Lowest Invoice  : ₹{peak:.2f} / ₹{low:.2f}")
            print(f"\tSorted Wait Times (Min): {durations_copy} (Mean: {round(sum(durations_copy)/len(durations_copy), 2)})")

        elif choice == "7":
            print("\nShutting down MediCore Engine. Stay healthy!")
            break
        else:
            print("\t[Warning]: Invalid menu option. Choose 1-7.")


if __name__ == "__main__":
    run_medicore_cli()