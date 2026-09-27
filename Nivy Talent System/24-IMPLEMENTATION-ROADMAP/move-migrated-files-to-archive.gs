/**
 * Nivy — Move migrated Drive files into archive folder
 * =====================================================
 * HOW TO USE
 * 1. drive.google.com → New → More → Google Apps Script
 *    OR script.google.com → New project
 * 2. Paste this entire file, Save
 * 3. First run: dryRunMoveToArchive()     ← only logs, no move
 * 4. Review Execution log
 * 5. Then run: moveMigratedFilesToArchive()
 *
 * Needs: user must own files (or have edit access)
 * Archive folder must exist and be accessible.
 */

// ========== CONFIG ==========
var ARCHIVE_FOLDER_ID = '1tVUXrVx2RVkaFg_zaEI-w34aORhrlRXV';

/** true = log only, do not move */
var DRY_RUN = true;

/**
 * Files already extracted to GitHub (Nivy Talent System).
 * Add/remove IDs as needed.
 * DO NOT put Contact Information form or response sheets here.
 */
var FILES_TO_ARCHIVE = [
  // Policies
  { id: '1aHFhB1fXfZM0VQJebShbzk1WR0B2YX2xcYrsWRQzShs', name: 'HR Policies' },
  { id: '1il8a1nwm3j1F76ZOC6fcq-VfITLtfspfGjOAtq_uksA', name: 'Human Resources (HR) Department Policies' },
  { id: '1g4HRBbnE5dx-scC3XxOBcsXp5Ac0I6hJfbeeHxoDPts', name: 'Master Company Policies & Procedures Manual' },
  { id: '1iWZI1-5RApnHI9tFfDL-KGYpCyl5Jqf8pOk17QlajWg', name: 'Sales Marketing & Customer Support Policies' },
  { id: '19D6VWYNyFT6joMoxOco_uhdwMA8zxP7RPsufckQUQns', name: 'Administration & Management Department Rules & Policies' },
  { id: '15bVKTBtIyScmMuh-cbUoYGmlHL69lIzaxLeVR2Gm_no', name: 'Purchase / Procurement Department Policies & Rules' },
  { id: '1FhgjqaY6rQznRqr1FbHDUTQq_oxiD7N2zHyzvAGvGt0', name: 'Operations Department Policies' },
  { id: '1sXJZ594yE3N-jcw6VMVmzUC4VfAAHwo2WfUzviOMhlA', name: 'Employee Policies Handbook' },

  // Training
  { id: '1aiSoTa4AXEsiMpGvgafs9Apssio7Lu0jJtuki3WWLVk', name: 'VA Basic Training' },
  { id: '1GN5IN6kT-TqIsXHTx6hErpqa3iqBpwGM-ex4XxwGXHU', name: 'VA Advance Training' },
  { id: '1HNBOwEVekzn_K0s4Rxwscl0dIJ24_aLSp6vM_IihQqM', name: 'HR Training' },
  { id: '1fIrpoKwbyh_882nc4GEppgRsMUYBVSKcOIr8mUItFJQ', name: 'Sales Training Schedule' },
  { id: '1XODyuyKEJY9Br_JpPIvVVBpDIXHf-7OR4p2lPc-K3H0', name: 'Basic Training MCQ' },
  { id: '1VF_uy84M-K0eU2vbaiUONYnKH9bkS_MwSnIxOW_ZEig', name: 'Advanced Training MCQ' },
  { id: '1YHTmUwfs3Lq1W-KEW6k-JI8cMiuo3ts25NYjGZqGRdA', name: 'Digital Marketing, Sales Training Manual' },
  { id: '1IyQ-pRQy7tE15SjkgqHFRW5Omq9Bp8pyocogG6RHeV4', name: 'Orientation' },

  // Roles / ranking
  { id: '1MV7s19DV7lM2Zyd-BDn1_J-njl9vighQ6Gn6_eVUcZA', name: 'Ranking System for Employees' },
  { id: '14Xh6Ihjpl5xyfwRoQpnqJeGGoAXZHhlpgKMzjTlTgGU', name: 'Organization_HR_Document_Roles_and_Responsibilities_Matrix' }
];

/**
 * NEVER move these (live hiring / PII).
 * Add Contact form ID and response sheet IDs if you know them.
 */
var NEVER_MOVE_IDS = [
  // 'PASTE_CONTACT_FORM_ID_HERE',
  // 'PASTE_RESPONSES_SHEET_ID_HERE'
];

// ========== ENTRY POINTS ==========

/** Step 1: safe preview */
function dryRunMoveToArchive() {
  DRY_RUN = true;
  moveMigratedFilesToArchive_();
}

/** Step 2: actually move */
function moveMigratedFilesToArchive() {
  DRY_RUN = false;
  moveMigratedFilesToArchive_();
}

// ========== CORE ==========

function moveMigratedFilesToArchive_() {
  var archive = DriveApp.getFolderById(ARCHIVE_FOLDER_ID);
  Logger.log('Archive folder: %s', archive.getName());
  Logger.log('DRY_RUN = %s', DRY_RUN);
  Logger.log('---');

  var ok = 0, skip = 0, fail = 0;

  FILES_TO_ARCHIVE.forEach(function (item) {
    if (NEVER_MOVE_IDS.indexOf(item.id) !== -1) {
      Logger.log('SKIP (never-move list): %s', item.name);
      skip++;
      return;
    }

    try {
      var file = DriveApp.getFileById(item.id);
      var name = file.getName();

      if (isInFolder_(file, ARCHIVE_FOLDER_ID)) {
        Logger.log('SKIP (already in archive): %s', name);
        skip++;
        return;
      }

      if (DRY_RUN) {
        Logger.log('DRY-RUN would move: %s (%s)', name, item.id);
        ok++;
        return;
      }

      file.moveTo(archive);
      Logger.log('MOVED: %s', name);
      ok++;
    } catch (e) {
      Logger.log('FAIL: %s | %s | %s', item.name, item.id, e.message);
      fail++;
    }
  });

  Logger.log('---');
  Logger.log('Done. ok=%s skip=%s fail=%s', ok, skip, fail);
}

function isInFolder_(file, folderId) {
  var parents = file.getParents();
  while (parents.hasNext()) {
    if (parents.next().getId() === folderId) return true;
  }
  return false;
}

/**
 * Optional: move by exact name search (if ID unknown).
 * Example: moveByNameToArchive_('Work Guidelines');
 */
function moveByNameToArchive_(exactName) {
  var archive = DriveApp.getFolderById(ARCHIVE_FOLDER_ID);
  var files = DriveApp.getFilesByName(exactName);
  var n = 0;
  while (files.hasNext()) {
    var f = files.next();
    if (NEVER_MOVE_IDS.indexOf(f.getId()) !== -1) continue;
    if (isInFolder_(f, ARCHIVE_FOLDER_ID)) continue;
    if (DRY_RUN) {
      Logger.log('DRY-RUN by name: %s (%s)', f.getName(), f.getId());
    } else {
      f.moveTo(archive);
      Logger.log('MOVED by name: %s', f.getName());
    }
    n++;
  }
  Logger.log('Name match count: %s', n);
}

/** Helper: list files currently in archive (verify). */
function listArchiveContents() {
  var archive = DriveApp.getFolderById(ARCHIVE_FOLDER_ID);
  var files = archive.getFiles();
  Logger.log('Files in archive "%s":', archive.getName());
  while (files.hasNext()) {
    var f = files.next();
    Logger.log(' - %s | %s', f.getName(), f.getId());
  }
}
