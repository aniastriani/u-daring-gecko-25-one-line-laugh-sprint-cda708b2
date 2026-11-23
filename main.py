import os

# One original line: a smartwatch's praise is the only applause a quiet
# everyday life ever gets. Written fresh for this sprint.
LINE = "My smartwatch congratulated me for standing up, which is the only standing ovation my life will ever get."


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
