function doGet() {
  const url = "*********";
  const ss = SpreadsheetApp.openByUrl(url);
  const sheet = ss.getSheets()[0];

  var last_row = sheet.getLastRow();
  var env = sheet.getRange(last_row, 1, 1, 4).getValues();

  return ContentService.createTextOutput(env);
}
