// Reviewer log for tauhidnabi.github.io/projects/signalsense
// 1. Create a Google Sheet. 2. Extensions > Apps Script, paste this, save.
// 3. Deploy > New deployment > Web app: Execute as "Me", Who has access "Anyone".
// 4. Paste the web-app URL into docs/signalsense/assets/config.js (window.SS_LOG_URL) and push.
function doPost(e) {
  var d = JSON.parse(e.postData.contents);
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName('Reviews') || ss.insertSheet('Reviews');
  if (sh.getLastRow() === 0) { sh.appendRow(['Time', 'Name', 'Page']); sh.setFrozenRows(1); }
  sh.appendRow([new Date(), String(d.name || '').slice(0, 100), String(d.page || '').slice(0, 80)]);
  return ContentService.createTextOutput('ok');
}
