import os

EXCLUDE_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules", ".github"}
EXCLUDE_FILES = {".DS_Store"}

README_FILE = "README.md"


def generate_tree(startpath: str) -> str:
    tree_lines = []

    def _tree(dir_path: str, prefix: str = ""):
        entries = sorted([
            e for e in os.listdir(dir_path)
            if e not in EXCLUDE_DIRS and e not in EXCLUDE_FILES
        ])

        for index, entry in enumerate(entries):
            path = os.path.join(dir_path, entry)
            is_last = index == len(entries) - 1

            connector = "└── " if is_last else "├── "
            tree_lines.append(prefix + connector + entry)

            if os.path.isdir(path):
                extension = "    " if is_last else "│   "
                _tree(path, prefix + extension)

    tree_lines.append(startpath)
    _tree(startpath)

    return "\n".join(tree_lines)


def update_readme(tree_str: str):
    if not os.path.exists(README_FILE):
        print("❌ README.md 없음")
        return

    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    start_tag = "<!-- START_TREE -->"
    end_tag = "<!-- END_TREE -->"

    if start_tag not in content or end_tag not in content:
        print("❌ README에 START/END 태그 없음")
        return

    before = content.split(start_tag)[0]
    after = content.split(end_tag)[1]

    new_section = f"""{start_tag}
{tree_str}
{end_tag}"""

    new_content = before + new_section + after

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("✅ README.md 업데이트 완료")


if __name__ == "__main__":
    tree = generate_tree("app")  # 필요하면 "."로 변경 가능
    update_readme(tree)