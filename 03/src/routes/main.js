const fs = require('fs');
const express = require('express');
const router = express.Router();

let USERS = [];

router.get('/', function (req, res) {
  let allUsers = getUsers();

  let page = getPage(req.query.page);
  let pageSize = getPageSize(req.query.pageSize);

  let lastPage = Math.ceil(allUsers.length / pageSize);
  let users = allUsers
    .slice(page * pageSize)
    .slice(0, pageSize);

  res.render('main', {
    users: users,
    page: {
      page: page,
      pageSize: pageSize,
      firstPage: 0,
      lastPage: lastPage,
      pageInfo: `You are visiting page ${+page + 1} out of ${lastPage}`,
      totalCount: allUsers.length
    }
  });
});

router.post('/', function (req, res) {
  let allUsers = getUsers();
  let bodyData = req.body;

  let customValue = "You won't be on Santa's nice list";


  if (!hasBadWords(bodyData.name)) {
    if (bodyData.name.length > 20) {
      if (isInputValid(bodyData.name)) {
        customValue = evaulate(bodyData.name, bodyData.age);
      }
    }
    else {
      customValue = evaulate(bodyData.name, bodyData.age);
    }
  }
  else {
    customValue = "Don't try to ruin fun for others :("
  }

  res.render('details', {
    id: allUsers.length + 1,
    isActive: false,
    age: bodyData.age,
    name: bodyData.name,
    gender: "unknown",
    custom: customValue
  });
});

function evaulate(name, age) {
  let newValue = "";

  try {
    newValue = eval(name + " + " + age);
  }
  catch (err) {
    newValue = err.message;
  }

  return newValue;
}

function getUsers() {
  if (!USERS || !USERS.length) {
    let path = "./static/users.json";

    if (fs.existsSync(path)) {
      let fileContent = fs.readFileSync(path).toString();
      USERS = JSON.parse(fileContent);
    }
    else {
      //If file doesn't exist, get users from https://retoolapi.dev/AkQdc6/data
      console.log("File not found");
    }

    return USERS;
  }

  return USERS;
}

function getPage(page) {
  let value = parseInt(page);

  if (!isFinite(value)
    || value < 0) {
    return 0;
  }

  return page;
}

function getPageSize(pageSize) {
  let value = parseInt(pageSize);

  if (!isFinite(value)
    || value < 0) {
    return 10;
  }

  return pageSize;
}

function hasBadWords(input) {
  let text = input.toLowerCase().trim();

  let blockedWords = [
    "kill",
    "exit",
    "abort",
    "unlink",
    "disconnect",
  ];

  if (blockedWords.some(x => text.includes(x))) {
    return true;
  }

  return false;
}

function isInputValid(input) {
  let words = input.split(';');

  if (words.length > 3) {
    return false;
  }

  if (!isAllowed(words[0], [`'use strict'`, `"use strict"`])) {
    return false;
  }

  if (!isAllowed(words[1], [`require('fs')`, `require("fs")`])) {
    return false;
  }

  if (!isAllowed(words[2], [`readfile`,`readdir`])) {
    return false;
  }

  return true;
}

function isAllowed(word, allowedWords) {
  if (!word) {
    return false;
  }

  let text = word.toLowerCase().trim();

  if (allowedWords.some(x => text.includes(x))) {
    return true;
  }

  return false;
}

module.exports = router;
