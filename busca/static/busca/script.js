window.addEventListener("load", checkJSLoaded);

function checkJSLoaded() {
  let form = document.getElementById("formBusca");
  let linkComoUsar = document.getElementById("link-instrucoes");
  let linkMenu = document.getElementById("link-menu");
  form.addEventListener("submit", controlC);
  linkComoUsar.addEventListener("click", toggleDivComoUsar);
  linkMenu.addEventListener("click", toggleDivMenu);
}

function controlC() {
    var copyText = document.getElementById("barraBusca");
    copyText.select();
    document.execCommand("copy");
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

function toggleDivComoUsar() {
    let divComoUsar = document.getElementById("divComoUsar")
    let linkInstrucoes = document.getElementById("link-instrucoes")
    let divLogo = document.getElementById("divLogo")

    if (divComoUsar.style.display == "none") {
        divComoUsar.style.display = "block"
        linkInstrucoes.innerHTML = "Fechar instruções"
        divLogo.style.height = "20vh";
    } else {
        divComoUsar.style.display = "none";
        linkInstrucoes.innerHTML = "Como utilizar"
        divLogo.style.height = "30vh";
    }
}

function preparaNumero(input) {
    input = input.replace(/\D/g,'');
    if (input.length > 20) {
        input = input.slice(-20);
    }
    let numero = input.padStart(20, "0");
    let codTribunal = numero.slice(13, -4);
    let codRegiao = numero.slice(-4);

    let numObj = {
        cnj: numero,
        tribunal: codTribunal,
        regiao: codRegiao
    };

    if (numObj.tribunal.charAt(0) == "4") {
        numObj.tribunal += numObj.regiao.charAt(0) + numObj.regiao.charAt(1);
    };

    if (numObj.tribunal.charAt(0) == "6") {
        numObj.tribunal = "600";
    }

    if (numObj.tribunal.charAt(0) == "7") {
        numObj.tribunal = "700";
    }

    return numObj;
}
