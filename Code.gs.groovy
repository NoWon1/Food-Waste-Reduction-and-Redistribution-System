function sendToAPI() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Receiver");
  const data = sheet.getDataRange().getValues();

  const chunkSize = 100; // Adjust based on API limits
  for (let i = 1; i < data.length; i += chunkSize) {
    const chunk = data.slice(i, i + chunkSize);

    const payload = {
      Email_ID: row[0],
      Recipient_ID: row[1],
      NGO_name: row[2],
      Phone_number: row[3],
      Address: row[4],
      City: row[5],
      State: row[6],
      Pincode: row[7],
      Quantity_required_in_grams: row[8],
      Redistribution_time_span_in_hours: row[9]
    };

    const options = {
      method: "POST",
      contentType: "application/json",
      payload: JSON.stringify(payload)
    };

    const response = UrlFetchApp.fetch("https://api.nal.usda.gov/fdc/v1/foods/search?api_key=VqcdzP2y0qFebjCJQHstclChaaVR4699e1K97JbQ", options);
    Logger.log(response.getContentText());
  }
}