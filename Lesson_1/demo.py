from pathlib import Path


def collect_files(folder: Path) -> dict[str, dict[str, int]]:
    files: dict[str, dict[str, int]] = {}

    for file in folder.iterdir():
        if file.is_dir():
            child_files = collect_files(file)

            for ext, stats in child_files.items():
                if ext in files:
                    files[ext]["size"] += stats["size"]
                    files[ext]["count"] += stats["count"]
                else:
                    files[ext] = stats

        if file.is_file():
            if file.suffix in files:
                files[file.suffix]["size"] += file.stat().st_size
                files[file.suffix]["count"] += 1
            else:
                files[file.suffix] = {"size": file.stat().st_size, "count": 1}
    return files

def calculate_total_size(files: dict) -> int:
    total_size: int = 0
    for k, v in files.items():
        total_size += v["size"]

    return total_size

def calculate_contribution(total_size: int, files: dict) -> None:
    for k, v in files.items():
        files[k]["contribution"] = round((v["size"] / total_size) * 100)

def show_files(files: dict) -> None:
    print("Files Type Stats:")
    for k, v in sorted(files.items(), key=lambda x: x[1]["contribution"], reverse=True):
        print(f"{k} - {v['count']} files - {v['size'] / (1024 * 1024):.2f} MB ({v['contribution']}%)")

def main(folder: Path) -> None:
    files = collect_files(folder)
    total_size = calculate_total_size(files)
    calculate_contribution(total_size, files)
    show_files(files)

if __name__ == "__main__":
    downloads_dir = Path.home() / "Downloads"

    main(downloads_dir)