# Migration Map (Legacy -> New)

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
