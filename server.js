var path = require('path');
var express = require('express');
var app = express();
var PORT = process.env.PORT || 9090

app.use(express.static(__dirname));

app.listen(PORT, function(error) {
  if (error) {
    console.error(error);
  } else {
    console.info("==> 🌎  Listening on port %s. Visit http://localhost:%s/ in your browser.", PORT, PORT);
  }
});
