"""
Migration script: encrypts the existing plaintext settings.json in-place.
Run ONCE: python migrate_encrypt_settings.py
"""
import json
from pathlib import Path
from cryptography.fernet import Fernet

BASE = Path(r"C:\F- Drive\MYWORK-Research1")
SETTINGS_F = BASE / "99-SYSTEM-BACKEND" / "settings.json"
KEY_FILE = BASE / "99-SYSTEM-BACKEND" / ".settings_key"


def get_fernet() -> Fernet:
    if not KEY_FILE.exists():
        KEY_FILE.write_text(Fernet.generate_key().decode())
        print(f"[+] Generated new key: {KEY_FILE}")
    return Fernet(KEY_FILE.read_text().strip().encode())


def encrypt_val(f: Fernet, val: str) -> str:
    if not val:
        return val
    try:
        f.decrypt(val.encode())
        return val
    except Exception:
        return f.encrypt(val.encode()).decode()


def main():
    if not SETTINGS_F.exists():
        print(f"[!] {SETTINGS_F} not found, nothing to migrate")
        return

    f = get_fernet()
    raw = json.loads(SETTINGS_F.read_text(encoding="utf-8"))
    engines = raw.get("ai_engines", [])
    encrypted = 0
    for eng in engines:
        key = eng.get("api_key", "")
        if key and not key.startswith("gAAAAA"):
            eng["api_key"] = encrypt_val(f, key)
            encrypted += 1
    SETTINGS_F.write_text(json.dumps(raw, indent=2), encoding="utf-8")
    print(f"[OK] Encrypted {encrypted} API key(s) in {SETTINGS_F}")


if __name__ == "__main__":
    main()
