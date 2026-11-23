from pathlib import Path


ENTRY = "Day 1: build a SKU-safe Shopify CSV repair script. On Upwork, spend $20 on Connects; bid $60 on escrow-funded import cleanup jobs. Target variant-heavy catalogs; preserve SKUs, verify row counts, prices, stock. Deliver in 24h, request review, reinvest earnings in bids."


def main() -> None:
    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_text(ENTRY, encoding="utf-8")
    (output / "entry.txt").chmod(0o644)


if __name__ == "__main__":
    main()
