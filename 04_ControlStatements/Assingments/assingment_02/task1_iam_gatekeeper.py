def main():
    # Hardcoded database credentials
    CORRECT_USER = "admin_hari"
    CORRECT_TOKEN = "sec-token-2026"
    ALLOWED_ROLE = "DevOpsEngineer"

    print("=== Cloud IAM Gateway ===")
    username = input("Enter Username       : ").strip()
    token = input("Enter Security Token : ").strip()
    role = input("Enter System Role    : ").strip()

    print("\n--- Gatekeeper Authorization ---")

    access_granted = False
    verdict = ""

    # Nested Validation Logic
    if username != CORRECT_USER:
        verdict = "Access Denied: Invalid Username"
    else:
        if token != CORRECT_TOKEN:
            verdict = "Access Denied: Security Token Rejected"
        else:
            if role == ALLOWED_ROLE or role == "SuperAdmin":
                access_granted = True
                verdict = "Authorization Successful - Environment Unlocked"
            else:
                verdict = "Access Denied: Insufficient Role Privileges"

    # Ternary operator for session tag
    session_status = "SECURE" if access_granted else "BREACH_ATTEMPT"

    print(f"User Authenticated  : {username == CORRECT_USER}")
    print(f"Token Validated     : {token == CORRECT_TOKEN}")
    print(f"Role Access Granted : {access_granted}")
    print(f"Session Audit Tag   : [{session_status}]")
    print(f"Gateway Verdict     : {verdict}")

if __name__ == "__main__":
    main()