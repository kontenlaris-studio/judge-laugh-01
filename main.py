"""Write one funny line to /output/entry.txt.

Make the AI Judge Laugh (make.fun) — one line, at most 200 characters.
"""

import os

LINE = (
    "My password manager forgot my master password, then emailed me a reset "
    "link, then locked me out for clicking it too many times. "
    "It now manages my anxiety instead."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
