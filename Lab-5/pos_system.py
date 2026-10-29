"""Retail Point-of-Sale & Discount Tracker.

A small shop POS system that totals a cart with tax, applies promo
codes via safe parsing, keeps a running sales total, and appends
receipts to pos_log.txt.
"""

import logging
import re

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

# Catalogue & state
PRICE_LIST = {"pen": 10, "notebook": 45, "bag": 799, "bottle": 150}

STATE = {
    "sales_total": 0.0,
    "receipt_lines": [],
    "receipt_counter": 0,
}

PROMO_CODES = {
    "SAVE10": lambda total: total * 0.9,
    "FLAT50": lambda total: max(0.0, total - 50.0),
    "HALF": lambda total: total * 0.5,
}


def process_checkout(cart_items, tax_rate=0.05, receipts=None):
    """Calculate total for cart_items, apply tax_rate, and record it.

    Parameters:
        cart_items (list): Sequence of (item_name, quantity) tuples.
        tax_rate (float): Tax percentage to apply (default 0.05).
        receipts (list, optional): Accumulator list for receipt totals.

    Returns:
        float: Final total for the transaction.
    """
    if receipts is None:
        receipts = []

    subtotal = 0.0
    for item_name, quantity in cart_items:
        if item_name not in PRICE_LIST:
            LOGGER.warning("Unknown item '%s' — skipped.", item_name)
            continue
        if not isinstance(quantity, int) or quantity <= 0:
            LOGGER.warning(
                "Invalid quantity %r for '%s' — skipped.",
                quantity,
                item_name,
            )
            continue
        subtotal += PRICE_LIST[item_name] * quantity

    if tax_rate < 0:
        LOGGER.warning("Negative tax rate %s treated as 0.", tax_rate)
        tax_rate = 0.0

    total = subtotal + (subtotal * tax_rate)
    receipts.append(total)
    STATE["sales_total"] += total

    STATE["receipt_counter"] += 1
    receipt_no = STATE["receipt_counter"]
    STATE["receipt_lines"].append(
        f"Receipt #{receipt_no:04d} total={total:.2f}"
    )
    return total


def apply_promo_code(code_str):
    """Apply a promo code safely without eval.

    Supports whitelisted promo codes (e.g., 'SAVE10', 'FLAT50') and
    safe arithmetic expressions like 'total * 0.9' or 'total - 50'.

    Parameters:
        code_str (str): Promo code or arithmetic formula.

    Returns:
        float or None: Discounted sales total or None if code is invalid.
    """
    total = STATE["sales_total"]
    cleaned = code_str.strip()

    # Check uppercase named promo codes
    if cleaned.upper() in PROMO_CODES:
        return PROMO_CODES[cleaned.upper()](total)

    # Safely parse patterns like "total * 0.9" or "total - 50"
    match = re.match(r"^total\s*([*+-])\s*(\d+(?:\.\d+)?)$", cleaned.lower())
    if match:
        operator, operand_str = match.group(1), match.group(2)
        operand = float(operand_str)
        if operator == "*":
            return total * operand
        if operator == "-":
            return max(0.0, total - operand)
        if operator == "+":
            return total + operand

    LOGGER.warning("Unknown or unsupported promo code '%s'.", code_str)
    return None


def update_stock(item, qty):
    """Log a stock-level change for item with catalogue validation.

    Parameters:
        item (str): Item identifier.
        qty (int): Quantity to adjust.
    """
    if item not in PRICE_LIST:
        LOGGER.warning("Cannot update stock: '%s' not in catalogue.", item)
        return
    LOGGER.info("Stock updated for %s by %d.", item, qty)


def save_receipt_log(filepath="pos_log.txt"):
    """Append all accumulated receipt lines to filepath with UTF-8 encoding.

    Parameters:
        filepath (str): Destination path for the receipt log.
    """
    with open(filepath, "a", encoding="utf-8") as file_handle:
        for line in STATE["receipt_lines"]:
            file_handle.write(line + "\n")


def print_sales():
    """Print the running sales total to stdout."""
    print(f"Sales so far: {STATE['sales_total']:.2f}")


def main():
    """Demonstrate point-of-sale workflow and test cases."""
    print("Bill 1:", process_checkout([("pen", 3), ("notebook", 2)]))
    print("Bill 2:", process_checkout([("bag", 1), ("laptop", 1)]))
    print("Bill 3:", process_checkout([("bottle", 4)]))
    print("Bill 4:", process_checkout([("pen", 2)], tax_rate=0.05))

    update_stock("laptop", 5)

    print("After promo:", apply_promo_code("total * 0.9"))
    code = (
        input("Enter promo code (e.g. total - 50): ").strip() or "total - 50"
    )
    print("After your promo:", apply_promo_code(code))

    save_receipt_log()
    print_sales()


if __name__ == "__main__":
    main()
