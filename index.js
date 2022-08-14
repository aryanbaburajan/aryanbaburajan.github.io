let menu = document.getElementById("menu");
let selectMenu = document.getElementById("select-menu");
menu.style.display = "none";
selectMenu.style.display = "none";

document.addEventListener(
  "contextmenu",
  function (e) {
    e.preventDefault();
    menu.style.display = "block";
    menu.style.left = e.pageX + "px";
    menu.style.top = e.pageY + "px";
  },
  false
);

function getSelectedText() {
  var text = "";
  if (typeof window.getSelection != "undefined") {
    text = window.getSelection().toString();
  } else if (
    typeof document.selection != "undefined" &&
    document.selection.type == "Text"
  ) {
    text = document.selection.createRange().text;
  }
  return text;
}

function textSelected(e) {
  var selectedText = getSelectedText();
  if (selectedText) {
    selectMenu.style.display = "block";
    selectMenu.style.left = e.pageX + "px";
    selectMenu.style.top = e.pageY + "px";
  } else {
    selectMenu.style.display = "none";
  }
}

document.onmouseup = function (e) {
  textSelected(e);
  menu.style.display = "none";
};

document.onmousedown = function (e) {};

function copyLinkToHighlight() {
  navigator.clipboard.writeText(
    location.href +
      "#:~:text=" +
      encodeURIComponent(window.getSelection().getRangeAt(0).toString())
  );
}

function openSource() {
  let url =
    "https://github.com/aryanbaburajan/aryanbaburajan.github.io/blob/main/";

  if (window.location.pathname == "/") {
    url += "index.html";
  } else {
    url += window.location.pathname;
  }

  console.log(url);
  window.open(url, "_blank").focus();
}
