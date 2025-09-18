from pathlib import Path
import argparse
import shutil

def parse_args():
    parser = argparse.ArgumentParser(description = "Copy files with sorting by extension.")
    parser.add_argument("--source", "-s",  type = Path, required = True, help = "Path to source directory.")
    parser.add_argument("--dest", "-d", type = Path, default = Path("dest"), help = "Path to destination directory.")
    return parser.parse_args()

def copy_files(src: Path, dest: Path) -> None:
    try:
        for element in src.iterdir():
            if element.is_dir():
                copy_files(element, dest)
            else:
                ext = element.suffix.lstrip(".") or "no_extension"
                folder = dest / ext
                folder.mkdir(exist_ok = True, parents = True)

                target = folder / element.name
                counter = 1
                while target.exists():
                    stem = element.stem
                    suffix = element.suffix
                    target = folder / f"{stem}_{counter}{suffix}"
                    counter += 1

                shutil.copy(element, target)
                print(f"Copied {element} → {target}")

    except Exception as e:
        print(f"Error while copying {element}: {e}")

def main():
    args = parse_args()

    if not args.source.exists() or not args.source.is_dir():
        print(f"Source directory {args.source} does not exist or is not a directory.")
        return

    print(f"Copying files from {args.source} to {args.dest}...")
    copy_files(args.source, args.dest)
    print("Done.")

if __name__ == "__main__":
    main()
