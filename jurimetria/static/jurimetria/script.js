window.addEventListener("load", checkJSLoaded);

function checkJSLoaded() {
  let linkMenu = document.getElementById("link-menu");
  linkMenu.addEventListener("click", toggleDivMenu);
}

function toggleDivMenu() {
    let divMenu = document.getElementById("divMenu");
    let linkMenu = document.getElementById("link-menu");
    let divLogo = document.getElementById("divLogo");

    if (divMenu.style.display == "none") {
        divMenu.style.display = "block";
        linkMenu.innerHTML = "Fechar menu";
    } else {
        divMenu.style.display = "none";
        linkMenu.innerHTML = "Menu";
    }
}
