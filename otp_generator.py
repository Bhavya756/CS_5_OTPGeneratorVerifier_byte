import hashlib
import hmac
import json
import secrets
import struct
import time


OTP_LENGTH = 6
VALIDITY_WINDOW = 30


def generate_secret():
    """Generate a random hexadecimal secret key."""
    return secrets.token_hex(16)


def generate_otp(secret, timestamp=None):
    """Generate a 6-digit time-based OTP."""
    if timestamp is None:
        timestamp = int(time.time())

    counter = timestamp // VALIDITY_WINDOW

    key = bytes.fromhex(secret)
    message = struct.pack(">Q", counter)

    digest = hmac.new(key, message, hashlib.sha1).digest()

    offset = digest[-1] & 0x0F

    binary_code = (
        ((digest[offset] & 0x7F) << 24)
        | ((digest[offset + 1] & 0xFF) << 16)
        | ((digest[offset + 2] & 0xFF) << 8)
        | (digest[offset + 3] & 0xFF)
    )

    otp = binary_code % (10 ** OTP_LENGTH)

    return f"{otp:0{OTP_LENGTH}d}"


def verify_otp(secret, submitted_otp, timestamp=None):
    """Verify an OTP within the allowed validity window."""
    if timestamp is None:
        timestamp = int(time.time())

    submitted_otp = str(submitted_otp).strip()

    if len(submitted_otp) != OTP_LENGTH or not submitted_otp.isdigit():
        return False

    # Allow the current, previous, and next 30-second windows
    # to account for small clock differences.
    for offset in (-1, 0, 1):
        check_time = timestamp + (offset * VALIDITY_WINDOW)
        expected_otp = generate_otp(secret, check_time)

        if hmac.compare_digest(expected_otp, submitted_otp):
            return True

    return False


def run_test_vectors():
    """Run predefined test vectors from test_vectors.json."""
    try:
        with open("test_vectors.json", "r") as file:
            test_vectors = json.load(file)
    except FileNotFoundError:
        print("[-] test_vectors.json not found.")
        return

    print("\n" + "=" * 55)
    print("             TEST VECTOR VERIFICATION")
    print("=" * 55)

    passed = 0

    for index, test in enumerate(test_vectors, start=1):
        secret = test["secret"]
        timestamp = test["timestamp"]
        submitted_otp = test["submitted_otp"]
        expected_result = test["expected_result"]

        result = verify_otp(secret, submitted_otp, timestamp)
        actual_result = "valid" if result else "invalid"

        if actual_result == expected_result:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"

        print(f"\nTest {index}: {test['description']}")
        print(f"Timestamp: {timestamp}")
        print(f"Submitted OTP: {submitted_otp}")
        print(f"Expected: {expected_result}")
        print(f"Result: {actual_result}")
        print(f"Status: {status}")

    print("\n---------------------------------------------")
    print(f"[+] Tests Passed: {passed}/{len(test_vectors)}")


def main():
    print("=" * 55)
    print("        OTP GENERATOR & VERIFIER")
    print("        Time-Based One-Time Password")
    print("=" * 55)

    secret = generate_secret()

    print(f"\nSecret Key: {secret}")

    current_time = int(time.time())
    otp = generate_otp(secret, current_time)

    print(f"Current OTP: {otp}")
    print(f"Validity Window: {VALIDITY_WINDOW} seconds")

    print("\n---------------------------------------------")
    user_input = input("Enter OTP to verify: ")

    if verify_otp(secret, user_input, current_time):
        print("[+] OTP Verified Successfully")
    else:
        print("[-] Invalid or Expired OTP")

    print("\n[+] Verification completed.")

    run_test_vectors()


if __name__ == "__main__":
    main()