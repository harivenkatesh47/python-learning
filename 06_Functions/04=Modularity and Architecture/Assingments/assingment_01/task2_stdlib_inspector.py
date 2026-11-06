import math as m
import sys as system_core
from platform import python_version, system

def compute_hypotenuse_and_log(base, perpendicular):
    hypotenuse = m.hypot(base, perpendicular)
    log_base = m.log10(base)
    return round(hypotenuse, 2), round(log_base, 2)

if __name__ == "__main__":
    print("=== Standard Library Runtime & Math Diagnostics ===")
    
    print("\n--- Runtime Environment ---")
    print(f"Python Engine Version : {python_version()}")
    print(f"Operating Platform    : {system()} ({system_core.platform})")
    
    print("\n--- Trigonometric & Log Metrics ---")
    base_val = 12.0
    perp_val = 5.0
    print(f"Inputs: Base = {base_val}, Perpendicular = {perp_val}")
    
    hypot_val, log_val = compute_hypotenuse_and_log(base_val, perp_val)
    print(f"Hypotenuse (Vector Length) : {hypot_val:.2f}")
    print(f"Log10 of Base              : {log_val:.2f}")