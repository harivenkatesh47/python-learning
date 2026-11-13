import math as m
import random
import copy
import medicore_config as cfg


def increment_patient_counter():
    global total_patients_served
    cfg.total_patients_served += 1
    local_status = "PROCESSING_PATIENT"
    return cfg.total_patients_served, local_status


def sanitize_patient_profile(raw_name, raw_abha_id, raw_notes):
    clean_name = raw_name.strip().title()
    clean_abha = raw_abha_id.strip().upper()

    is_valid_abha = clean_abha.startswith("ABHA-") and clean_abha.endswith("-IN")
    reg_year = clean_abha[5:9] if len(clean_abha) >= 12 else "0000"
    security_hash = clean_abha[::-1]

    normalized_notes = raw_notes.strip().lower()
    confidential_hits = normalized_notes.count("hiv") + normalized_notes.count("psychiatric")
    sanitized_notes = normalized_notes.replace("hiv", "[REDACTED-PHI]").replace("psychiatric", "[REDACTED-PHI]")

    token_id = f"PT-{random.randint(1000, 9999)}"
    return token_id, clean_name, is_valid_abha, reg_year, security_hash, sanitized_notes, confidential_hits


def compute_bmi_and_triage(weight_kg, height_m, sys_bp, dia_bp, heart_rate, spo2, temp_f):
    bmi_val = round(weight_kg / (height_m ** 2), 2)
    base_vitals = (sys_bp, dia_bp, heart_rate, spo2)
    verified_vitals = base_vitals + ("VERIFIED",)

    is_critical = (spo2 < 90) or (sys_bp > 180 and heart_rate > 120)
    is_urgent = (temp_f >= 102.0) or (sys_bp >= 140)

    if is_critical:
        triage_code = "CODE RED (Emergency)"
    elif is_urgent:
        triage_code = "CODE YELLOW (Urgent)"
    else:
        triage_code = "CODE GREEN (Standard)"

    priority_tag = "CRITICAL" if is_critical else "ROUTINE"
    return bmi_val, verified_vitals, triage_code, priority_tag


def audit_prescription_safety(patient_allergies_list, doctor="Dr. Sharma", *med_names, **instructions):
    patient_allergens = set(patient_allergies_list)
    patient_allergens.add("sulfa_trace")
    patient_allergens.discard("none")

    total_chemical_exposure = set()
    conflict_detected = set()
    stock_verified = True

    for med in med_names:
        med_key = med.strip().lower()
        if med_key not in cfg.pharmacy_catalog or cfg.pharmacy_catalog[med_key]["stock"] <= 0:
            stock_verified = False
            break
        drug_ingredients = cfg.pharmacy_catalog[med_key]["ingredients"]
        total_chemical_exposure = total_chemical_exposure | drug_ingredients
        clash = patient_allergens & drug_ingredients
        if clash:
            conflict_detected = conflict_detected | clash
    else:
        stock_msg = "All prescribed medicines verified in stock."

    if not stock_verified:
        stock_msg = "Dispensing halted: One or more medicines out of stock or missing."

    safe_compounds = total_chemical_exposure - patient_allergens
    is_safe = (len(conflict_detected) == 0) and stock_verified

    audit_summary = {
        "doctor": doctor,
        "prescribed_tuple": med_names,
        "instructions": instructions,
        "is_safe": is_safe,
        "stock_status": stock_msg,
        "allergy_clashes": conflict_detected,
        "total_exposure": total_chemical_exposure,
        "safe_compounds": safe_compounds
    }
    return audit_summary


def find_specialist_escalation(dept_node, target_condition, current_depth=0):
    if target_condition in dept_node["conditions"]:
        return dept_node["dept"], dept_node["lead"], current_depth

    for sub_unit in dept_node["sub_units"]:
        found_dept, found_lead, depth = find_specialist_escalation(
            sub_unit, target_condition, current_depth + 1
        )
        if found_dept is not None:
            return found_dept, found_lead, depth

    return None, None, -1


def govt_cghs_discount(amount):
    return round(amount * 0.30, 2)


def corporate_insurance_discount(amount):
    return round(amount * 0.15 + 50.0, 2)


def senior_citizen_discount(amount):
    return round(amount * 0.10, 2)


discount_strategies = {
    "cghs": govt_cghs_discount,
    "corporate": corporate_insurance_discount,
    "senior": senior_citizen_discount
}


def process_pharmacy_billing(med_list, scheme_key):
    Simulated_catalog = copy.deepcopy(cfg.pharmacy_catalog)

    raw_prices = []
    for med in med_list:
        med_key = med.strip().lower()
        if med_key in Simulated_catalog:
            raw_prices.append(Simulated_catalog[med_key]["price"])
            Simulated_catalog[med_key]["stock"] -= 1

    gst_prices = list(map(lambda p: round(p * 1.12, 2), raw_prices))
    low_stock_keys = list(filter(
        lambda k: cfg.pharmacy_catalog[k]["stock"] <= 5,
        cfg.pharmacy_catalog.keys()
    ))

    gross_total = round(sum(gst_prices), 2)
    callback_func = discount_strategies.get(scheme_key, senior_citizen_discount)
    discount_amt = callback_func(gross_total)
    net_payable = round(max(0.0, gross_total - discount_amt), 2)

    whole_rupees = int(net_payable // 1)
    paise = int(round((net_payable % 1) * 100))
    notes_500 = whole_rupees // 500
    rem_after_500 = whole_rupees % 500
    notes_100 = rem_after_500 // 100
    loose_rupees = rem_after_500 % 100

    return {
        "raw_prices": raw_prices,
        "gst_prices": gst_prices,
        "gross_total": gross_total,
        "discount": discount_amt,
        "net_payable": net_payable,
        "currency_breakdown": (notes_500, notes_100, loose_rupees, paise),
        "low_stock_alerts": low_stock_keys,
        "real_catalog_unchanged": cfg.pharmacy_catalog[med_list[0].lower()]["stock"] != Simulated_catalog[med_list[0].lower()]["stock"] if med_list and med_list[0].lower() in cfg.pharmacy_catalog else True
    }


def compute_manual_ledger_metrics(invoices):
    if not invoices:
        return 0.0, 0.0, 0.0
    gross_rev = 0.0
    peak_inv = invoices[0]
    low_inv = invoices[0]

    for val in invoices:
        gross_rev += val
        if val > peak_inv:
            peak_inv = val
        if val < low_inv:
            low_inv = val

    return round(gross_rev, 2), peak_inv, low_inv