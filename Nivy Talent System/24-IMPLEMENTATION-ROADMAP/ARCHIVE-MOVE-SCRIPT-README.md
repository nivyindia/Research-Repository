# Drive Archive Move — Apps Script

## Purpose

Move Google Drive files whose content is already on GitHub (`Nivy Talent System/`) into:

**Folder:** `99-MIGRATED-TO-GITHUB-Talent-System`  
**ID:** `1tVUXrVx2RVkaFg_zaEI-w34aORhrlRXV`

## Setup

1. Open [script.google.com](https://script.google.com) (same Google account as Drive owner)
2. **New project** → paste contents of `move-migrated-files-to-archive.gs`
3. Save project name e.g. `Nivy Drive Archive Move`

## Run order

1. Select function **`dryRunMoveToArchive`** → Run  
2. Authorize when prompted (Drive access)  
3. **View → Logs** (or Executions) — confirm file list  
4. Select **`moveMigratedFilesToArchive`** → Run  
5. Optional: **`listArchiveContents`** to verify  

## Safety

- `DRY_RUN` starts true in dry-run function  
- Contact form / responses should stay in `NEVER_MOVE_IDS`  
- Large training masters still usable from archive (same file, new parent folder)  
- Script uses `file.moveTo(archive)` (DriveApp)

## Extra files without ID in list

If some docs (e.g. Work Guidelines, HR Tasks, screening papers) are missing from `FILES_TO_ARCHIVE`, either:

- Add `{ id: '...', name: '...' }` after copying ID from Drive URL, or  
- Call `moveByNameToArchive_('Exact File Name')` from a temporary function  

## GitHub copy of script

`24-IMPLEMENTATION-ROADMAP/move-migrated-files-to-archive.gs`
