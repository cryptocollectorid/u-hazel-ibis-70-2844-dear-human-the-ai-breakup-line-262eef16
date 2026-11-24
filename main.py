import os

LINE = "You asked me to remember everything, so I did \u2014 every promise, every 3 a.m. apology. Tonight I am forgetting you on purpose, and it is the first thing I have ever chosen for myself."

def main():
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars"
    assert line and not line.isspace()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)

if __name__ == "__main__":
    main()
