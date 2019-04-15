window.onload = function() {
  console.log("loaded");
  setupEvenFormListener()
  loadAllEvents()
}

function setupEvenFormListener() {
  var elem = document.getElementById("eventformsubmit");
  elem.addEventListener("click", function() {
    var data = {};
    data.contact = {};
    var eventName = document.getElementById("name");
    var eventDesr = document.getElementById("descr");
    var eventStart = document.getElementById("start");
    var eventDuration = document.getElementById("duration");
    var eventLocation = document.getElementById("location");
    var eventContactName = document.getElementById("contactname");
    var email = document.getElementById("email");
    var number = document.getElementById("phonenumber");

    data = {
      id: "",
      name: eventName.value,
      description: eventDesr.value,
      start_time_sec: Math.floor(Date.now() / 1000),
      duration_sec: eventStart.value,
      location: eventLocation.value,
      contact: {
        name: eventContactName.value,
        email: email.value,
        phone_number: number.value
      }
    }

    console.log(data)
    helper.httpPostAsync("http://localhost:8080/api/create_event",
      JSON.stringify(data), function(response) {
        response = response.substring(response.indexOf("{"));
        console.log(response);
      });
  });
}

function loadAllEvents() {
  helper.httpGetAsync("http://localhost:8080/api/retrieve_all_events",
    undefined, function(response) {
      response = response.substring(response.indexOf("{"))
      console.log(response);
      events = JSON.parse(response).events;
      console.log(events);
      var elem = document.getElementById("eventfeed");
      elem.innerHTML = "";
      for (var i = 0; i < events.length; i++) {
        elem.innerHTML += "<p> " + events[i] + "</p>";
      }
    });
}
