function doGet(e) {
  const url = "*******";
  const ss = SpreadsheetApp.openByUrl(url);
  const sheet = ss.getSheets()[0];
  const params = {
    "timestamp": new Date(),
    "temperature": e.parameter.temperature,
    "humidity": e.parameter.humidity,
    "pressure": e.parameter.pressure
  };
  sheet.appendRow(Object.values(params));
  return ContentService.createTextOutput('sccess');
}