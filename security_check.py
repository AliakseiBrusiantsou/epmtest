#!/usr/bin/env python3
"""Daily security check script for epmtest project."""

import os
import subprocess
import smtplib
import sys
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_TO = os.environ.get("SECURITY_REPORT_TO", "brusentsov@gmail.com")
SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")


def run_cmd(cmd, cwd=None):
    result = subprocess.run(
        cmd, capture_output=True, text=True, cwd=cwd or PROJECT_DIR
    )
    return result.stdout + result.stderr, result.returncode


def check_bandit():
    """Run bandit static analysis on Python files."""
    output, code = run_cmd(
        ["bandit", "-r", ".", "-f", "txt", "--exit-zero"]
    )
    return output, code


def check_outdated_packages():
    """Check for outdated packages with pip."""
    output, code = run_cmd(["pip", "list", "--outdated", "--format=columns"])
    if not output.strip():
        output = "All packages are up to date."
    return output, code


def check_file_permissions():
    """Check for sensitive files with overly broad permissions."""
    issues = []
    sensitive_patterns = [".env", "*.key", "*.pem", "*.crt", "*.secret"]
    for fname in os.listdir(PROJECT_DIR):
        fpath = os.path.join(PROJECT_DIR, fname)
        if not os.path.isfile(fpath):
            continue
        mode = oct(os.stat(fpath).st_mode)[-3:]
        # Warn if world-readable sensitive files
        if any(fname.endswith(p.lstrip("*")) or fname == p for p in sensitive_patterns):
            if int(mode[2]) > 0:
                issues.append(f"  {fname}: permissions {mode} (world-readable!)")
    if not issues:
        return "No sensitive files with overly broad permissions found.", 0
    return "\n".join(issues), 1


def check_env_file():
    """Check .env file exists and has restricted permissions."""
    env_path = os.path.join(PROJECT_DIR, ".env")
    if not os.path.exists(env_path):
        return ".env file not found (no secrets file present).", 0
    mode = oct(os.stat(env_path).st_mode)[-3:]
    if int(mode[1]) > 0 or int(mode[2]) > 0:
        return f".env file permissions {mode} — should be 600 (owner read/write only)!", 1
    return f".env file permissions {mode} — OK.", 0


def send_email(subject, body):
    if not SMTP_USER or not SMTP_PASSWORD:
        print("SMTP credentials not configured. Report:\n")
        print(body)
        return False
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = REPORT_TO
    msg.attach(MIMEText(body, "plain"))
    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, REPORT_TO, msg.as_string())
        print(f"Report sent to {REPORT_TO}")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}", file=sys.stderr)
        return False


def main():
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"Security Check Report — {date_str}",
        f"Project: {PROJECT_DIR}",
        "=" * 60,
        "",
    ]
    overall_ok = True

    # Bandit static analysis
    lines.append("[ 1 ] Bandit Static Code Analysis")
    lines.append("-" * 40)
    out, code = check_bandit()
    lines.append(out.strip() or "(no output)")
    if "Issue" in out:
        overall_ok = False
    lines.append("")

    # Outdated packages
    lines.append("[ 2 ] Outdated Python Packages")
    lines.append("-" * 40)
    out, code = check_outdated_packages()
    lines.append(out.strip())
    if code != 0 or ("Package" in out and "Version" in out and "Latest" in out and "All packages" not in out):
        overall_ok = False
    lines.append("")

    # File permissions
    lines.append("[ 3 ] Sensitive File Permissions")
    lines.append("-" * 40)
    out, code = check_file_permissions()
    lines.append(out.strip())
    if code != 0:
        overall_ok = False
    lines.append("")

    # .env check
    lines.append("[ 4 ] .env File Security")
    lines.append("-" * 40)
    out, code = check_env_file()
    lines.append(out.strip())
    if code != 0:
        overall_ok = False
    lines.append("")

    lines.append("=" * 60)
    status = "PASSED" if overall_ok else "ISSUES FOUND"
    lines.append(f"Overall status: {status}")

    report = "\n".join(lines)
    print(report)

    subject = f"[epmtest] Daily Security Check — {status} — {date_str}"
    send_email(subject, report)


if __name__ == "__main__":
    main()
