function buttonClicked(event) {
  scroll = event.target.getAttribute("data-scrollto");
  smoothScroll.animateScroll(scroll);
}

window.onload = function() {
  var scrollButtons = document.querySelectorAll("[data-scrollto]");
  for (var i=0; i<scrollButtons.length; i++) {
    scrollButtons[i].onclick = buttonClicked;
  }
};
