window.addEventListener("load", checkJSLoaded);

function checkJSLoaded() {
  let linkMenu = document.getElementById("link-menu");
  let linkBusca = document.getElementById("link-busca");
  linkMenu.addEventListener("click", toggleDivMenu);
  linkBusca.addEventListener("click", toggleDivBusca);
}

function toggleDivMenu() {
  toggleDiv("divMenu", "link-menu", "block", "Menu");
}

function toggleDivBusca() {
  toggleDiv("divBusca", "link-busca", "block", "Busca");
}

function toggleDiv(divId, linkId, display, linkNome) {
  let div = document.getElementById(divId);
  let link = document.getElementById(linkId);
  if (div.style.display == "none") {
    div.style.display = display;
    link.innerHTML = "Fechar";
  } else {
    div.style.display = "none";
    link.innerHTML = linkNome;
  }
}
