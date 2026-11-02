import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
VERSIONS = {"clang-format": "23.1.3", "clang-tidy": "22.1.8"}


def find_tool(name):
    suffix = ".exe" if os.name == "nt" else ""
    bin_dir = "Scripts" if os.name == "nt" else "bin"
    candidates = [ROOT / ".style-venv" / bin_dir / (name + suffix)]
    path_tool = shutil.which(name)
    if path_tool:
        candidates.append(Path(path_tool))
    for candidate in candidates:
        if candidate.is_file():
            result = subprocess.run(
                [str(candidate), "--version"], capture_output=True, text=True
            )
            match = re.search(r"\b(\d+\.\d+\.\d+)\b", result.stdout + result.stderr)
            if result.returncode == 0 and match and match.group(1) == VERSIONS[name]:
                return str(candidate)
            raise RuntimeError(f"Expected {name} {VERSIONS[name]}: {candidate}")
    raise RuntimeError(f"Install tools-requirements.txt: {name} is missing")


def run(command):
    result = subprocess.run(command, cwd=ROOT)
    return result.returncode


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", action="store_true", help="Format source files in place")
    parser.add_argument("--build-dir", help="Use a compilation database instead of -std/-I")
    args = parser.parse_args()
    files = sorted(
        path for folder in (ROOT / "include", ROOT / "src")
        for path in folder.rglob("*")
        if path.suffix in {".h", ".hpp", ".cpp", ".cc", ".cxx"}
    )
    if not files:
        raise RuntimeError("No C++ files found in include/ and src/")
    formatter = find_tool("clang-format")
    file_names = [str(path.relative_to(ROOT)) for path in files]
    if args.format:
        return run([formatter, "-i", *file_names])
    tidy = find_tool("clang-tidy")
    if run([tidy, "--verify-config"]) != 0:
        return 1
    format_result = run([formatter, "--dry-run", "--Werror", *file_names])
    sources = [str(path.relative_to(ROOT)) for path in files if path.suffix != ".h" and path.suffix != ".hpp"]
    if not sources:
        raise RuntimeError("No C++ translation units found")
    if args.build_dir:
        tidy_args = ["-p", str(Path(args.build_dir).resolve())]
    else:
        tidy_args = ["--", "-std=c++17", "-Iinclude"]
        if sys.platform == "darwin":
            sdk = subprocess.check_output(["xcrun", "--show-sdk-path"], text=True).strip()
            compiler = Path(subprocess.check_output(["xcrun", "--find", "clang++"], text=True).strip())
            library_headers = compiler.parent.parent / "include" / "c++" / "v1"
            if not library_headers.is_dir():
                raise RuntimeError("Apple libc++ headers missing; check Command Line Tools")
            tidy_args += ["-stdlib=libc++", "-isysroot", sdk, "-isystem", str(library_headers)]
    tidy_result = run([tidy, *sources, *tidy_args])
    if format_result == 0 and tidy_result == 0:
        print("Formatting and clang-tidy checks passed.")
        return 0
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (RuntimeError, OSError) as error:
        print(f"Style check failed: {error}", file=sys.stderr)
        sys.exit(2)
