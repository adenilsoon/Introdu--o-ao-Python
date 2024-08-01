console.log("Conexão feita com perfil-dados.js");

document.addEventListener('keydown', function(event) {
    // Verifica se a tecla pressionada é o Backspace
    if (event.key === "Backspace") {
        // Previne a ação padrão do Backspace (por exemplo, navegar para trás ao usar um campo de entrada)
        event.preventDefault();
        // Redireciona para a página index.html
        window.location.href = 'index.html';
    }
});
 