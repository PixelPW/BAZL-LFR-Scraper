var fs = require('fs');

var data = JSON.parse(fs.readFileSync('lfr.all.json'));

var consolidated = {};
var na = [];

data.forEach(function(aircraft) {
  var hex = aircraft.details.aircraftAddresses.hex;
  var prefix = hex.substr(0, 2);
  var suffix = hex.substr(2);

  if (prefix === 'N/') {
    na.push(aircraft);
    return;
  }

  if (!(prefix in consolidated)) {
    consolidated[prefix] = {}
  };

  consolidated[prefix][suffix.toUpperCase()] = {
    r: aircraft.registration,
    t: aircraft.icaoCode
  };
});

Object.keys(consolidated).forEach(function(prefix) {
  fs.writeFileSync(prefix.toUpperCase() + ".json", JSON.stringify(consolidated[prefix]));
});

fs.writeFileSync('na.json', JSON.stringify(na));
