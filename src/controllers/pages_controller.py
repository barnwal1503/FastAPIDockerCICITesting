from pathlib import Path

PORTFOLIO_FILE = Path(__file__).resolve().parents[2] / "portfolio" / "index.html"


def root() -> dict[str, str]:
    return {"message": "Hello from EC2"}


def portfolio() -> str:
    return PORTFOLIO_FILE.read_text(encoding="utf-8")
