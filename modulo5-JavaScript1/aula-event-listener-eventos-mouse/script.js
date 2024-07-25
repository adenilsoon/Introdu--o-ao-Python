let quantidadeSubtotal = document.getElementById("quantidade-subtotal");
let valorSubtotal = document.getElementById("valor-subtotal");

let subtotalInfo = {
  quantidade: 1,
  valor: 11.66,
};

quantidadeSubtotal.innerText = subtotalInfo.quantidade + " itens";
valorSubtotal.innerText = subtotalInfo.valor;
 

//variaveis
const valorOriginal = subtotalInfo.valor;
const inptQtd = document.getElementById("quantidade-produto-01");
const btnAdd = document.getElementById("btn-adicionar-produto-01");
const subQtd = document.getElementById("quantidade-produto-01");
const btnSub = document.getElementById("btn-subtrair-produto-01");
 
 
//criar uma função
 
function adicionarUm() {
  inptQtd.value = Number(inptQtd.value) + 1
  subtotalInfo.quantidade = inptQtd.value
  subtotalInfo.valor = valorOriginal * inptQtd.value;
  atualizarSubtotal()
}

function subtrairUm() {
  subQtd.value = Number(subQtd.value) - 1
  subtotalInfo.quantidade = subQtd.value
  subtotalInfo.valor = valorOriginal * inptQtd.value;
  atualizarSubtotal()
}

function atualizarSubtotal() {
  quantidadeSubtotal.innerText = subtotalInfo.quantidade + " itens";
  valorSubtotal.innerText = subtotalInfo.valor;

}


//adicionar evento
btnAdd.addEventListener("click", adicionarUm);
btnSub.addEventListener("click", subtrairUm);