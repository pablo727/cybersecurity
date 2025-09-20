import sys
import os
import argparse
from pathlib import Path
import pwd
import spwd


parser = argparse.ArgumentParser(
    description="Combine /etc/passwd and /etc/shadow into John-the-Ripper format (requires root)."
)
parser.add_argument(
    "-o",
    "--out",
    type=Path,
    default=Path.home() / "john-lab/mypasswd",
    help="Output file for combined passwd+shadow (default: ~/john-lab/mypasswd)",
)


def combine_passwd_shadow(out_path: Path):
    # Must be root
    if os.geteuid() != 0:
        print("Run with sudo: sudo python3 combine_passwd_shadow.py")
        sys.exit(1)

    # Grab shadow and passwd entries
    shadow_entries = spwd.getspall()
    passwd_entries = pwd.getpwall()

    invalid = ["", "!", "*", "!!", "*NP*"]

    shadow_dict = {entry.sp_nam: entry.sp_pwd for entry in shadow_entries}
    passwd_dict = {
        entry.pw_name: (
            entry.pw_uid,
            entry.pw_gid,
            entry.pw_gecos,
            entry.pw_dir,
            entry.pw_shell,
        )
        for entry in passwd_entries
    }

    # Ensure outfolder exists
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Write combined lines
    with out_path.open("w", newline="\n") as fh:
        for username, password in shadow_dict.items():
            if password not in invalid and username in passwd_dict:
                uid, gid, gecos, home, shell = passwd_dict[username]
                line = f"{username}:{password}:{uid}:{gid}:{gecos}:{home}:{shell}"
                fh.write(line + "\n")

    # After the file is closed, set strict permissions and optionally chown
    out_path.chmod(0o600)
    sudo_user = os.environ.get("SUDO_USER")
    if sudo_user:
        pw = pwd.getpwnam(sudo_user)
        os.chown(out_path, pw.pw_uid, pw.pw_gid)

    print(f"[+] Combined passwd+shadow saved to {out_path}")


def main():
    args = parser.parse_args()
    combine_passwd_shadow(args.out)


if __name__ == "__main__":
    main()
