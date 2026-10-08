#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import argparse

PROJECT_ROOT = Path(__file__).resolve().parents[1]

CORE_TOP_LEVEL = [
    "00_INBOX",
    "01_SCHOOL_AND_STUDY",
    "02_WORK_AND_CAREER",
    "03_IDENTITY_LEGAL_ADMIN",
    "04_HEALTH_AND_WELLBEING",
    "05_PHOTOS_AND_VIDEOS",
    "06_HOBBIES_AND_LEARNING",
    "07_TRAVEL_AND_MOVING",
    "08_TEMPLATES_AND_RESOURCES",
    "09_ARCHIVE",
]

FORBIDDEN_LEGACY_TOP_LEVEL = [
    "03_PERSONAL_DOCUMENTS",
    "04_FINANCE_AND_ADMIN",
    "07_AUDIO_AND_MUSIC",
    "10_SOCIAL_MEDIA_AND_BRANDING",
    "11_TEMPLATES_AND_RESOURCES",
    "12_TEMP_UNSORTED",
    "13_ARCHIVE",
    "99_SYSTEM_METADATA",
]

FORBIDDEN_LEGACY_PATHS = [
    "01_SCHOOL_AND_STUDY/Current_Semester",
    "01_SCHOOL_AND_STUDY/Previous_Semesters",
    "01_SCHOOL_AND_STUDY/Thesis_or_Dissertation",
    "01_SCHOOL_AND_STUDY/Extracurricular_Academic",
    "01_SCHOOL_AND_STUDY/Applications",
    "02_WORK_AND_CAREER/CV_and_Resume",
    "02_WORK_AND_CAREER/Internships",
    "02_WORK_AND_CAREER/Jobs",
    "02_WORK_AND_CAREER/Side_Projects",
    "02_WORK_AND_CAREER/References_and_Letters",
]

CORE_LEAF_DIRS = [
    "00_INBOX/To_Sort",
    "00_INBOX/Processing_Now",
    "01_SCHOOL_AND_STUDY/Current_Term/_EXAMPLE_COURSE",
    "01_SCHOOL_AND_STUDY/Past_Terms/_EXAMPLE_YEAR_TERM",
    "01_SCHOOL_AND_STUDY/Thesis_and_Research/Literature",
    "01_SCHOOL_AND_STUDY/Thesis_and_Research/Data",
    "01_SCHOOL_AND_STUDY/Thesis_and_Research/Analysis",
    "01_SCHOOL_AND_STUDY/Thesis_and_Research/Drafts",
    "01_SCHOOL_AND_STUDY/Certificates_and_Transcripts/Degree_Certificates",
    "01_SCHOOL_AND_STUDY/Certificates_and_Transcripts/Course_Certificates",
    "01_SCHOOL_AND_STUDY/Certificates_and_Transcripts/Language_Certificates",
    "01_SCHOOL_AND_STUDY/Certificates_and_Transcripts/Official_Transcripts",
    "01_SCHOOL_AND_STUDY/Applications_and_Funding/University_Applications",
    "01_SCHOOL_AND_STUDY/Applications_and_Funding/Scholarship_Applications",
    "01_SCHOOL_AND_STUDY/Applications_and_Funding/Exchange_Programs",
    "01_SCHOOL_AND_STUDY/Academic_Activities/Conferences_and_Competitions",
    "02_WORK_AND_CAREER/CV_and_Resumes/Current_Version",
    "02_WORK_AND_CAREER/CV_and_Resumes/Previous_Versions",
    "02_WORK_AND_CAREER/CV_and_Resumes/Cover_Letters",
    "02_WORK_AND_CAREER/Employment/_EXAMPLE_EMPLOYER_ROLE",
    "02_WORK_AND_CAREER/Employment/References_and_Recommendations",
    "02_WORK_AND_CAREER/Projects/_EXAMPLE_PROJECT",
    "02_WORK_AND_CAREER/Portfolio/Technical",
    "02_WORK_AND_CAREER/Portfolio/Research",
    "02_WORK_AND_CAREER/Portfolio/Creative",
    "02_WORK_AND_CAREER/Job_Search/Applications",
    "02_WORK_AND_CAREER/Job_Search/Interview_Preparation",
    "02_WORK_AND_CAREER/Professional_Development/Certifications",
    "03_IDENTITY_LEGAL_ADMIN/Identity/Passport",
    "03_IDENTITY_LEGAL_ADMIN/Identity/National_ID",
    "03_IDENTITY_LEGAL_ADMIN/Identity/Birth_Certificate",
    "03_IDENTITY_LEGAL_ADMIN/Identity/Driver_License",
    "03_IDENTITY_LEGAL_ADMIN/Immigration_and_Residence/Visas",
    "03_IDENTITY_LEGAL_ADMIN/Immigration_and_Residence/Residence_Permits",
    "03_IDENTITY_LEGAL_ADMIN/Housing_and_Utilities/Rental_Agreements",
    "03_IDENTITY_LEGAL_ADMIN/Housing_and_Utilities/Utility_Bills",
    "03_IDENTITY_LEGAL_ADMIN/Legal_and_Insurance/Contracts",
    "03_IDENTITY_LEGAL_ADMIN/Legal_and_Insurance/Insurance_Policies",
    "03_IDENTITY_LEGAL_ADMIN/Banking_and_Payments/Bank_Statements",
    "03_IDENTITY_LEGAL_ADMIN/Banking_and_Payments/Payment_Confirmations",
    "03_IDENTITY_LEGAL_ADMIN/Taxes_and_Compliance/_EXAMPLE_COUNTRY_YEAR",
    "03_IDENTITY_LEGAL_ADMIN/Receipts_and_Invoices/Education_and_Scholarship",
    "03_IDENTITY_LEGAL_ADMIN/Receipts_and_Invoices/Travel",
    "03_IDENTITY_LEGAL_ADMIN/Receipts_and_Invoices/Home_and_Living",
    "03_IDENTITY_LEGAL_ADMIN/Subscriptions_and_Services/Software_Licenses",
    "03_IDENTITY_LEGAL_ADMIN/Government_and_Admin/Official_Correspondence",
    "04_HEALTH_AND_WELLBEING/Medical_Records/Primary_Care",
    "04_HEALTH_AND_WELLBEING/Medical_Records/Specialists",
    "04_HEALTH_AND_WELLBEING/Medical_Records/Lab_Results",
    "04_HEALTH_AND_WELLBEING/Insurance/Policy_Documents",
    "04_HEALTH_AND_WELLBEING/Insurance/Claims",
    "04_HEALTH_AND_WELLBEING/Prescriptions_and_Medications/Active",
    "04_HEALTH_AND_WELLBEING/Vaccinations/Certificates",
    "04_HEALTH_AND_WELLBEING/Wellbeing_and_Fitness/Plans",
    "04_HEALTH_AND_WELLBEING/Mental_Health/Resources",
    "04_HEALTH_AND_WELLBEING/Emergency_Contacts/List",
    "05_PHOTOS_AND_VIDEOS/Camera_Imports/Phone_Backups",
    "05_PHOTOS_AND_VIDEOS/Camera_Imports/Camera_Dumps",
    "05_PHOTOS_AND_VIDEOS/Personal_Photos/Family_and_Friends",
    "05_PHOTOS_AND_VIDEOS/Personal_Photos/Portraits",
    "05_PHOTOS_AND_VIDEOS/Personal_Photos/Events",
    "05_PHOTOS_AND_VIDEOS/Travel_Photos/_EXAMPLE_TRIP",
    "05_PHOTOS_AND_VIDEOS/Videos/Personal_Clips",
    "05_PHOTOS_AND_VIDEOS/Videos/Event_Videos",
    "05_PHOTOS_AND_VIDEOS/Videos/Travel_Videos",
    "05_PHOTOS_AND_VIDEOS/Edited_Media/Final_Exports",
    "05_PHOTOS_AND_VIDEOS/Edited_Media/Work_In_Progress",
    "06_HOBBIES_AND_LEARNING/Reading_and_Notes/Fiction_and_Non_Fiction",
    "06_HOBBIES_AND_LEARNING/Reading_and_Notes/Reference",
    "06_HOBBIES_AND_LEARNING/Language_Learning/_EXAMPLE_LANGUAGE",
    "06_HOBBIES_AND_LEARNING/Courses_and_Certifications/_EXAMPLE_COURSE",
    "06_HOBBIES_AND_LEARNING/Creative_Hobbies/Art_and_Writing",
    "06_HOBBIES_AND_LEARNING/Creative_Hobbies/DIY_and_Maker",
    "06_HOBBIES_AND_LEARNING/Music_Listening/Albums_and_Playlists",
    "06_HOBBIES_AND_LEARNING/Music_Practice/Sheet_Music",
    "06_HOBBIES_AND_LEARNING/Music_Practice/Practice_Recordings",
    "06_HOBBIES_AND_LEARNING/Podcasts_and_Audiobooks/Saved_Episodes",
    "06_HOBBIES_AND_LEARNING/Recipes_and_Food/Collections",
    "07_TRAVEL_AND_MOVING/Trip_Planning/Upcoming_Trips/_EXAMPLE_TRIP",
    "07_TRAVEL_AND_MOVING/Trip_Planning/Past_Trips/_EXAMPLE_TRIP",
    "07_TRAVEL_AND_MOVING/Trip_Planning/Itinerary_Templates",
    "07_TRAVEL_AND_MOVING/Transport_and_Bookings/Flights",
    "07_TRAVEL_AND_MOVING/Transport_and_Bookings/Trains_and_Buses",
    "07_TRAVEL_AND_MOVING/Transport_and_Bookings/Accommodation",
    "07_TRAVEL_AND_MOVING/International_Move/Pre_Departure",
    "07_TRAVEL_AND_MOVING/International_Move/Arrival_and_Registration",
    "07_TRAVEL_AND_MOVING/International_Move/Housing_Setup",
    "07_TRAVEL_AND_MOVING/Travel_Admin/Insurance_and_Visas",
    "07_TRAVEL_AND_MOVING/Memories_and_Logs/Trip_Notes",
    "08_TEMPLATES_AND_RESOURCES/Document_Templates/CV_and_Resume",
    "08_TEMPLATES_AND_RESOURCES/Document_Templates/Cover_Letter",
    "08_TEMPLATES_AND_RESOURCES/Document_Templates/Reports",
    "08_TEMPLATES_AND_RESOURCES/Document_Templates/Presentations",
    "08_TEMPLATES_AND_RESOURCES/Project_Templates/Research_Project",
    "08_TEMPLATES_AND_RESOURCES/Project_Templates/Side_Project",
    "08_TEMPLATES_AND_RESOURCES/Media_Templates/Thumbnails_and_Banners",
    "08_TEMPLATES_AND_RESOURCES/Media_Templates/Captions_and_Copy",
    "08_TEMPLATES_AND_RESOURCES/Reference_Assets/Fonts_and_Icons",
    "08_TEMPLATES_AND_RESOURCES/Automation_and_Scripts/_EXAMPLE_SCRIPT_PROJECT",
    "09_ARCHIVE/Yearly_Archive/_EXAMPLE_YEAR",
    "09_ARCHIVE/Inactive_Projects/_EXAMPLE_PROJECT",
    "09_ARCHIVE/Old_Courses/_EXAMPLE_COURSE",
    "09_ARCHIVE/Legacy_Documents/Expired",
    "09_ARCHIVE/Legacy_Documents/Superseded",
    "09_ARCHIVE/To_Delete_After_Review",
]

EXTRA_LEAF_DIRS = [
    "extras/OPTIONAL_MUSIC_PRODUCTION/DAW_Projects/_EXAMPLE_TRACK",
    "extras/OPTIONAL_MUSIC_PRODUCTION/Sample_Libraries",
    "extras/OPTIONAL_MUSIC_PRODUCTION/MIDI_and_Presets",
    "extras/OPTIONAL_MUSIC_PRODUCTION/Mastered_Exports",
    "extras/OPTIONAL_MUSIC_PRODUCTION/Plugin_Setups",
    "extras/OPTIONAL_CREATOR_WORKFLOWS/Content_Ideation",
    "extras/OPTIONAL_CREATOR_WORKFLOWS/Production_Pipeline",
    "extras/OPTIONAL_CREATOR_WORKFLOWS/Publishing_Queue",
    "extras/OPTIONAL_CREATOR_WORKFLOWS/Analytics_and_Reports",
    "extras/OPTIONAL_CREATOR_WORKFLOWS/Account_Exports",
]

README_LINK_TARGETS = [
    "docs/README.md",
    "docs/folder_map.md",
    "docs/naming_conventions.md",
    "docs/maintenance_checklist.md",
    "docs/migration_map.md",
    "TEMPLATE_TREE.txt",
]


@dataclass(frozen=True)
class TemplateSpec:
    core_dirs: tuple[Path, ...]
    core_leaf_dirs: tuple[Path, ...]
    extra_dirs: tuple[Path, ...]
    extra_leaf_dirs: tuple[Path, ...]


def _all_dirs(paths: list[str]) -> list[Path]:
    dirs: set[Path] = set()
    for item in paths:
        p = Path(item)
        dirs.add(p)
        for parent in p.parents:
            if parent == Path("."):
                break
            dirs.add(parent)
    return sorted(dirs, key=lambda p: p.as_posix())


def build_spec() -> TemplateSpec:
    core_dirs = set(_all_dirs(CORE_LEAF_DIRS))
    core_dirs.update(Path(name) for name in CORE_TOP_LEVEL)
    extra_dirs = set(_all_dirs(EXTRA_LEAF_DIRS))
    return TemplateSpec(
        core_dirs=tuple(sorted(core_dirs, key=lambda p: p.as_posix())),
        core_leaf_dirs=tuple(sorted(Path(p) for p in CORE_LEAF_DIRS)),
        extra_dirs=tuple(sorted(extra_dirs, key=lambda p: p.as_posix())),
        extra_leaf_dirs=tuple(sorted(Path(p) for p in EXTRA_LEAF_DIRS)),
    )


def _to_tree(paths: list[Path]) -> dict[str, dict]:
    tree: dict[str, dict] = {}
    for path in sorted(paths, key=lambda p: p.as_posix()):
        node = tree
        for part in path.parts:
            node = node.setdefault(part, {})
    return tree


def _render_tree(tree: dict[str, dict], root_label: str = "ROOT/") -> list[str]:
    lines = [root_label]

    def walk(node: dict[str, dict], prefix: str) -> None:
        names = sorted(node)
        for idx, name in enumerate(names):
            is_last = idx == len(names) - 1
            connector = "└── " if is_last else "├── "
            lines.append(f"{prefix}{connector}{name}/")
            extension = "    " if is_last else "│   "
            walk(node[name], prefix + extension)

    walk(tree, "")
    return lines


def render_template_tree(spec: TemplateSpec) -> str:
    core_tree = _render_tree(_to_tree(list(spec.core_dirs)))
    extra_relative = [
        path.relative_to("extras")
        for path in spec.extra_dirs
        if path != Path("extras")
    ]
    extra_tree = _render_tree(_to_tree(extra_relative), "OPTIONAL_EXTRAS/")
    return (
        "# Universal GDrive Folder Template (Generated)\n\n"
        "## Core folders (upload only these ten folders)\n"
        + "\n".join(core_tree)
        + "\n\n## Optional extras (opt-in, upload only if needed)\n"
        + "\n".join(extra_tree)
        + "\n"
    )


def render_readme(spec: TemplateSpec) -> str:
    core_list = "\n".join(f"- `{name}/`" for name in CORE_TOP_LEVEL)
    return f"""# Universal Google Drive Folder Template

Concise, reviewable folder template for Google Drive with a stable generated structure.

## Upload instructions

Upload **only** these ten core folders to Google Drive:

{core_list}

Do **not** upload repository helper paths: `docs/`, `extras/`, `scripts/`, `README.md`, `TEMPLATE_TREE.txt`.

`extras/` is optional and should be uploaded only when you need those specialized workflows.

## References

- Full generated tree: [`TEMPLATE_TREE.txt`](TEMPLATE_TREE.txt)
- Documentation index: [`docs/README.md`](docs/README.md)
- Folder map and canonical homes: [`docs/folder_map.md`](docs/folder_map.md)
- Naming conventions: [`docs/naming_conventions.md`](docs/naming_conventions.md)
- Maintenance checklist: [`docs/maintenance_checklist.md`](docs/maintenance_checklist.md)
- Legacy-to-new migration map: [`docs/migration_map.md`](docs/migration_map.md)

Generated by [`scripts/generate_template.py`](scripts/generate_template.py).
"""


def render_docs_readme(core_count: int, extras_count: int) -> str:
    return f"""# Documentation

This directory contains generated usage and maintenance documentation for the universal folder template.

## What is generated

- [`folder_map.md`](folder_map.md): Core folder intent and canonical homes.
- [`naming_conventions.md`](naming_conventions.md): File naming rules.
- [`maintenance_checklist.md`](maintenance_checklist.md): Recurring cleanup guidance.
- [`migration_map.md`](migration_map.md): Legacy-to-new mapping for this restructure.

## Directory counts

- Core directories: **{core_count}**
- Optional extras directories: **{extras_count}**

Counting method: counted leaf directories only (the `_EXAMPLE_*` endpoints and terminal storage folders that carry placeholders).

---

Created by **[Nhat Le Vo](https://github.com/vntle)** — Doctoral researcher in Germany.

License language preserved from repository root: **Free to use, adapt, and share. Credit appreciated but not required.**
"""


def render_folder_map() -> str:
    return """# Folder Map

## Core top-level folders

- `00_INBOX`: temporary intake before sorting.
- `01_SCHOOL_AND_STUDY`: coursework, research, transcripts, applications, and scholarships.
- `02_WORK_AND_CAREER`: CV, employment, portfolio, and job-search materials.
- `03_IDENTITY_LEGAL_ADMIN`: merged personal + finance admin (identity, legal, tax, receipts, banking).
- `04_HEALTH_AND_WELLBEING`: medical, insurance, prescriptions, fitness, and wellbeing.
- `05_PHOTOS_AND_VIDEOS`: personal media including **all travel photos**.
- `06_HOBBIES_AND_LEARNING`: hobbies, courses, language learning, and ordinary music listening/practice.
- `07_TRAVEL_AND_MOVING`: trip logistics and relocation administration (not travel photos).
- `08_TEMPLATES_AND_RESOURCES`: reusable templates, assets, and script skeletons.
- `09_ARCHIVE`: inactive materials and long-term retention.

## Canonical homes (single source)

- CV files: `02_WORK_AND_CAREER/CV_and_Resumes/`
- Scholarship files: `01_SCHOOL_AND_STUDY/Applications_and_Funding/Scholarship_Applications/`
- Travel photos and videos: `05_PHOTOS_AND_VIDEOS/Travel_Photos/` and `05_PHOTOS_AND_VIDEOS/Videos/Travel_Videos/`

## Optional extras

- `extras/OPTIONAL_MUSIC_PRODUCTION`: specialized production workflows.
- `extras/OPTIONAL_CREATOR_WORKFLOWS`: non-platform-specific creator/social workflows.

## Pattern guidance

Use one `_EXAMPLE_*` folder per repeating pattern (courses, employers, projects, trips, years, countries, scripts, languages).
Duplicate the example folder when needed instead of pre-creating many year/platform-specific folders.
"""


def render_naming_conventions() -> str:
    return """# Naming Conventions

Use hyphens or underscores consistently.

## Recommended pattern

```text
YYYY-MM-DD-Category-Description-Version.ext
```

## Examples

- `2026-06-01-Exam-Maths-Revision-v1.pdf`
- `2025-10-12-Visa-Appointment-Germany.pdf`
- `2024-03-15-Portrait-Studio-Bremen-v1.jpg`
- `2023-07-20-Travel-Arctic-Cruise-v1.mp4`

## Rules

- Put the date first when relevant.
- Avoid spaces.
- Avoid special characters.
- Use short but clear descriptions.
- Use version tags such as `v1`, `v2`, or `FINAL`.
- Be consistent across folders.
"""


def render_maintenance_checklist() -> str:
    return """# Maintenance Checklist

## Weekly

- Sort files from `00_INBOX/To_Sort`.
- Rename badly named files.
- Remove obvious duplicates.

## Monthly

- Review new media imports and screenshots.
- Move finished work from in-progress folders to long-term homes.
- Archive inactive material to `09_ARCHIVE`.

## Semesterly or yearly

- Move completed courses to `09_ARCHIVE/Old_Courses`.
- Back up critical identity and legal records.
- Review subscriptions, receipts, and tax folders.
- Update CV and key career documents.
"""


def render_migration_map() -> str:
    return """# Migration Map (Legacy -> New)

## Top-level replacement

- `12_TEMP_UNSORTED` -> `00_INBOX`
- `01_SCHOOL_AND_STUDY` -> `01_SCHOOL_AND_STUDY`
- `02_WORK_AND_CAREER` -> `02_WORK_AND_CAREER`
- `03_PERSONAL_DOCUMENTS` + `04_FINANCE_AND_ADMIN` -> `03_IDENTITY_LEGAL_ADMIN`
- `05_HEALTH_AND_WELLBEING` -> `04_HEALTH_AND_WELLBEING`
- `06_PHOTOS_AND_VIDEOS` -> `05_PHOTOS_AND_VIDEOS`
- `07_AUDIO_AND_MUSIC` + portions of `08_HOBBIES_AND_LEARNING` -> `06_HOBBIES_AND_LEARNING`
- `09_TRAVEL_AND_MOVING` -> `07_TRAVEL_AND_MOVING`
- `11_TEMPLATES_AND_RESOURCES` -> `08_TEMPLATES_AND_RESOURCES`
- `13_ARCHIVE` -> `09_ARCHIVE`
- `10_SOCIAL_MEDIA_AND_BRANDING` -> `extras/OPTIONAL_CREATOR_WORKFLOWS`
- `99_SYSTEM_METADATA` -> `docs/`

## Notable removals and consolidations

- Removed prefilled year trees and broad `By_Year` media hierarchy.
- Removed gaming and platform-named social/course folder presets.
- Consolidated duplicates into one canonical home each for CV, scholarships, and travel photos.
"""


def render_files(spec: TemplateSpec) -> dict[Path, str]:
    core_count = len(spec.core_leaf_dirs)
    extras_count = len(spec.extra_leaf_dirs)
    return {
        PROJECT_ROOT / "README.md": render_readme(spec),
        PROJECT_ROOT / "TEMPLATE_TREE.txt": render_template_tree(spec),
        PROJECT_ROOT / "docs/README.md": render_docs_readme(core_count, extras_count),
        PROJECT_ROOT / "docs/folder_map.md": render_folder_map(),
        PROJECT_ROOT / "docs/naming_conventions.md": render_naming_conventions(),
        PROJECT_ROOT / "docs/maintenance_checklist.md": render_maintenance_checklist(),
        PROJECT_ROOT / "docs/migration_map.md": render_migration_map(),
    }


def write_text_if_needed(path: Path, content: str) -> None:
    normalized = content.replace("\r\n", "\n")
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == normalized:
        return
    path.write_text(normalized, encoding="utf-8")


def verify_file(path: Path, expected: str) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        errors.append(f"Missing file: {path.relative_to(PROJECT_ROOT)}")
        return errors
    actual = path.read_text(encoding="utf-8")
    if actual != expected:
        errors.append(f"Content mismatch: {path.relative_to(PROJECT_ROOT)}")
    return errors


def check_readme_links() -> list[str]:
    errors: list[str] = []
    readme = PROJECT_ROOT / "README.md"
    text = readme.read_text(encoding="utf-8") if readme.exists() else ""
    for target in README_LINK_TARGETS:
        marker = f"({target})"
        if marker not in text:
            errors.append(f"Missing README link: {target}")
        if not (PROJECT_ROOT / target).exists():
            errors.append(f"Broken README link target: {target}")
    return errors


def check_no_legacy_roots() -> list[str]:
    errors: list[str] = []
    for name in FORBIDDEN_LEGACY_TOP_LEVEL:
        if (PROJECT_ROOT / name).exists():
            errors.append(f"Legacy root still present: {name}")
    for relative_path in FORBIDDEN_LEGACY_PATHS:
        if (PROJECT_ROOT / relative_path).exists():
            errors.append(f"Legacy subtree still present: {relative_path}")
    return errors


def ensure_directories(paths: tuple[Path, ...]) -> None:
    for relative_path in paths:
        (PROJECT_ROOT / relative_path).mkdir(parents=True, exist_ok=True)


def ensure_leaf_placeholders(paths: tuple[Path, ...]) -> None:
    for relative_path in paths:
        keep = PROJECT_ROOT / relative_path / ".gitkeep"
        keep.parent.mkdir(parents=True, exist_ok=True)
        if not keep.exists():
            keep.write_text("", encoding="utf-8")


def run_generate(spec: TemplateSpec) -> None:
    ensure_directories(spec.core_dirs)
    ensure_directories(spec.extra_dirs)
    ensure_leaf_placeholders(spec.core_leaf_dirs)
    ensure_leaf_placeholders(spec.extra_leaf_dirs)
    for file_path, content in render_files(spec).items():
        write_text_if_needed(file_path, content)


def run_check(spec: TemplateSpec) -> int:
    errors: list[str] = []
    expected_files = render_files(spec)

    for d in list(spec.core_dirs) + list(spec.extra_dirs):
        if not (PROJECT_ROOT / d).is_dir():
            errors.append(f"Missing directory: {d.as_posix()}")

    for leaf in list(spec.core_leaf_dirs) + list(spec.extra_leaf_dirs):
        keep = PROJECT_ROOT / leaf / ".gitkeep"
        if not keep.exists():
            errors.append(f"Missing placeholder: {keep.relative_to(PROJECT_ROOT)}")

    for file_path, content in expected_files.items():
        errors.extend(verify_file(file_path, content))

    errors.extend(check_no_legacy_roots())
    errors.extend(check_readme_links())

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed: generated structure, files, links, and legacy removals are consistent.")
    print(f"Core directory count (leaf method): {len(spec.core_leaf_dirs)}")
    print(f"Optional extras directory count (leaf method): {len(spec.extra_leaf_dirs)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate folder template, tree, and docs.")
    parser.add_argument("--check", action="store_true", help="Validate generated output without writing.")
    args = parser.parse_args()

    spec = build_spec()

    if args.check:
        return run_check(spec)

    run_generate(spec)
    print("Generated folder template from declarative spec.")
    print(f"Core directory count (leaf method): {len(spec.core_leaf_dirs)}")
    print(f"Optional extras directory count (leaf method): {len(spec.extra_leaf_dirs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
