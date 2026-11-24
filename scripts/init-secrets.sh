#!/usr/bin/env sh
# Creates the Docker secret files used by compose.yaml.
# Existing files are never overwritten: Postgres keeps the password it was
# initialised with, so changing it here would lock the app out of the database.
set -eu

SECRETS_DIR="$(cd "$(dirname "$0")/.." && pwd)/secrets"

mkdir -p "$SECRETS_DIR"
chmod 700 "$SECRETS_DIR"

for name in postgres_password redis_password; do
    file="$SECRETS_DIR/$name.txt"
    if [ -s "$file" ]; then
        echo "exists   secrets/$name.txt"
    else
        head -c 24 /dev/urandom | od -An -tx1 | tr -d ' \n' > "$file"
        # Readable inside containers that run as a non-root user (e.g. postgres)
        chmod 644 "$file"
        echo "created  secrets/$name.txt"
    fi
done
