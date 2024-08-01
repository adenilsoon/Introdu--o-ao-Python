const linkPerfil = document.getElementById("link-perfil");
const navPerfil = document.getElementById("nav-perfil");

linkPerfil.addEventListener("mouseover", ()=> {
  navPerfil.style.display = "block"
})

/*window.addEventListener("keydown", (e) => {
  console.log(e.code)
  console.log(e.key)
  if(e.key === "1") {
    navPerfil.style.display = "block"
  }else if(e.key === "Escape"){
    navPerfil.style.display = "none"
  }
})
*/

// capturamos o elemento meus dados do html
const linkMeusDados = document.getElementById("link-perfil-dados");

const linkIndex = document.getElementById("link-index")
//adicionamos um evento de teclado na janela do navegador e pegamos o evento através do parâmetro (e)
window.addEventListener("keyup", (e) => {
  console.log(e.code)
  console.log(e.key)
  if(e.key === "1") {
    if(navPerfil.style.display === "block") {
      linkMeusDados.click()
      console.log(e.key)
      if(e.key === "Backspace"){
        linkIndex.click()
      }
    }else {
      navPerfil.style.display = "block"
    }
  }

  if(e.key === "Escape"){
    navPerfil.style.display = "none"
  }
})


