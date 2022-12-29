"use strict";

if (!localStorage.getItem('counter')) {
  localStorage.setItem('counter', 0);
}

var counter = 0;

function count() {
  var counter = localStorage.getItem('counter');
  counter++;
  document.querySelector('h1').innerHTML = counter;
  localStorage.setItem('counter', counter);
}

document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('h1').innerHTML = localStorage.getItem('counter');
  document.querySelector('button').addEventListener('click', count);
});
//# sourceMappingURL=counter.dev.js.map
