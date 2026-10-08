# OTP Generator & Verifier

A Python-based **Time-Based One-Time Password (TOTP) Generator and Verifier** that generates a 6-digit OTP and validates it within a **30-second validity window**.

## Features

* Generates a secure 6-digit Time-Based One-Time Password (TOTP)
* OTP remains valid for 30 seconds
* Verifies user-entered OTP
* Displays the secret key and current OTP
* Handles invalid OTP input
* Includes test cases to verify OTP generation and verification
* Simple command-line interface

## Technologies Used

* **Python 3**
* **PyOTP** — for TOTP generation and verification

## Project Structure

```text
OTP-Generator-Verifier/
│
├── otp_generator.py
├── README.md
├── requirements.txt
└── screenshots/
    └── demo_screenshot.png
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/OTP-Generator-Verifier.git
cd OTP-Generator-Verifier
```

### 2. Install the required dependency

```bash
pip install -r requirements.txt
```

## Usage

Run the Python program using:

```bash
python otp_generator.py
```

The program generates a secret key and a current 6-digit OTP.

### Sample Execution

```text
=======================================================
        OTP GENERATOR & VERIFIER
        Time-Based One-Time Password
=======================================================

Secret Key: 800d7876a7d6c4b97022658728921d68
Current OTP: 250681
Validity Window: 30 seconds

---------------------------------------------
Enter OTP to verify: 250681

Verification Successful!
```

## Testing

The implementation was tested using valid and invalid OTP test vectors.

### Test Results

```text
Test 1 → PASS
Test 2 → PASS

Tests Passed: 2/2
```

The test cases confirm that the OTP verification logic works correctly for the implemented scenarios.

## Security Note

The OTP is time-based and changes automatically after the validity period. The secret key should be kept confidential and should **not be shared publicly** in a real-world authentication system.

> **Note:** The secret key and OTP shown above are sample values for demonstration purposes only.

## Learning Outcome

Through this task, I learned about:

* Time-Based One-Time Password (TOTP) authentication
* OTP generation and verification
* Validity windows in authentication systems
* Python-based security implementations
* Testing authentication logic using test cases

## Author

**Bhavya**

---

⭐ If you found this project useful, consider giving the repository a star!
