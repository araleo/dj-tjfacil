window.addEventListener("load", checkJSLoaded);

function checkJSLoaded() {
  let linkMenu = document.getElementById("link-menu");
  linkMenu.addEventListener("click", toggleDivMenu);

  const button = document.getElementById("button-change-details");
  if (button) {
    button.addEventListener("click", toggleUpdateForm);
  }
}

function toggleUpdateForm() {
    let divForm = document.getElementById("update-task-div");
    if (divForm.style.display != "block") {
        divForm.style.display = "block";
    } else {
        divForm.style.display = "none";
    }
}

function toggleDivMenu() {

    console.log("aaa")

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
