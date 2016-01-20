"use strict"

var express = require("express");
var bodyParser = require("body-parser");
var app = express();
var dbItems = require('./databaseItems.js');

app.use(logRequest);
app.use(express.static("public"));
app.use(bodyParser.json());

app.get("/todos", function (req, res) {
  dbItems.getAllItem(function(result) {
    res.json(result);
  });
});

app.post("/todos", function (req, res) {
  dbItems.addItem(req.body);
});

app.get("/todos/:id", function (req, res) {
  findItem(req, res, function (item) { res.json(item); });
});

app.put("/todos/:id", function (req, res) {
  dbItems.completeItem(req.params.id);
});

app.delete("/todos/:id", function (req, res) {
  dbItems.deleteItem(req.params.id);
});

app.listen(3000, function () {
  console.log("Listening on port 3000...")
});


function logRequest(req, res, next) {
  var parts = [new Date(), req.method, req.originalUrl];
  console.log(parts.join(" "));
  next();
}
