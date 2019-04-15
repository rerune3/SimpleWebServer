var helper = {};

helper.httpGetAsync = function(theUrl, callback, data) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
          callback(xmlHttp.responseText);
  }
  xmlHttp.open("GET", theUrl, true); // true for asynchronous
  xmlHttp.send(null);
}

helper.httpPostAsync = function(theUrl, callback, data) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
          callback(xmlHttp.responseText);
  }
  xmlHttp.open("POST", theUrl, true); // true for asynchronous
  xmlHttp.send(data);
}

data = {
  id: "",
  name: "tech talk",
  description: "a talk",
  start_time_sec: Math.floor(Date.now() / 1000),
  duration_sec: 2 * 3600,
  location: "LKD",
  contact: {
    name: "Chuck",
    email: "onwuzuruike@gmail.com",
    phone_number: "1234567890"
  }
}
function callback(response) {
  json_str = response.substring(response.indexOf("{"))
  console.log(JSON.parse(json_str));
}
console.log("helo")
helper.httpPostAsync("http://localhost:8080/api/create_event", callback, JSON.stringify(data))
console.log("happened")
