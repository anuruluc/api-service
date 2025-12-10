const { createInterface } = require('readline');
const { parse } = require('csv-parser');
const fs = require('fs');
const config = require('./config.json');

const csvToJSON = (filePath) => {
  return new Promise((resolve, reject) => {
    const readInterface = createInterface({
      input: fs.createReadStream(filePath),
      crlfDelay: Infinity
    });

    const data = [];
    readInterface.on('line', (line) => {
      data.push(line.split(','));
    });

    readInterface.on('close', () => {
      const csv = data.map((row, index) => {
        if (index === 0) return row;
        const obj = {};
        for (let i = 0; i < row.length; i++) {
          const key = data[0][i];
          obj[key] = row[i];
        }
        return obj;
      });
      resolve(csv);
    });

    readInterface.on('error', (err) => {
      reject(err);
    });
  });
};

const csvToJson = async () => {
  const filePath = config.csvFilePath;
  try {
    const csvData = await csvToJSON(filePath);
    const result = csvData.map((row) => {
      const { apiName, apiPath, description, method, status } = row;
      return {
        api: {
          name: apiName,
          path: apiPath,
          description: description,
          method: method,
          status: status
        }
      };
    });
    return result;
  } catch (error) {
    console.error(error);
    return [];
  }
};

module.exports = csvToJson;