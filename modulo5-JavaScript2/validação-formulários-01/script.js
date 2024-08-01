// ---------- VALIDAÇÃO USERNAME ---------- //
//captura de elementos
let usernameInput = document.getElementById("username");
let usernameLabel = document.querySelector('label[for="username"]');
let usernameHelper = document.getElementById("username-helper");
let userEmailInput = document.getElementById("email");
let userEmailLabel = document.getElementById("label[for='email]");
let userEmailHelper = document.getElementById("email-helper");



// Mostrar popup de campo obrigatório
//adicionamos um evento do tipo focus ao campo input do username(focus aciona o evento ao ser selecionado na página)
usernameInput.addEventListener("focus", (e) => {
    //adicionamos uma classe ao elemento label do campo username
    usernameLabel.classList.add("required-popup")
})

// Ocultar popup de campo obrigatório
//adicionamos um evento do tipo blur ao campo do usename(Blur aciona o evento quando o elemento perde o foco)
usernameInput.addEventListener("blur", () => {
    //removemos a classe do elemento label
    usernameLabel.classList.remove("required-popup")
})

//mostrar popup de campo obrigatório
function mostrarPopUp(input, label){
    input.addEventListener("focus", (e) => {
        label.classList.add("required-popup")
    })

    input.addEventListener("blur", () => {
        label.classList.remove("required-popup")
    })
}

// Validar valor do input
usernameInput.addEventListener("input", (e) => {
    console.log(e.target.value)
    let valorIpt = e.target.value
    if(valorIpt.length < 3) {
        usernameInput.classList.remove("correct");
        usernameInput.classList.add("error");
        usernameHelper.innerText = "Seu username deve ter mais que 3 caracteres";
        usernameHelper.classList.add("visible");
    }else {
        usernameInput.classList.remove("error");
        usernameInput.classList.add("correct");
        usernameHelper.classList.remove("visible");
    }
})

//validar email
userEmailInput.addEventListener("input", (e) => {
    let valor = e.target.value
    if(valor.includes("@") && valor.includes(".com")) {
        userEmailInput.classList.remove("error");
        usernameHelper.classList.remove("visible");
        userEmailInput.classList.add("correct");
    }else {
        userEmailInput.classList.remove("correct");
        userEmailInput.classList.add("error");
        userEmailHelper.innerText = "Email inválido";
        usernameHelper.classList.add("visible");
    }
})