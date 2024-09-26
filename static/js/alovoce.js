/*

O DOM é uma interface de programação que os navegadores usam para
interpretar e manipular documentos HTML e XML. 
Ele representa o documento como uma árvore de nós, onde cada nó é
um objeto que representa uma parte do documento (como elementos, atributos e texto).

*/

const frm = document.querySelector("form");
const resp = document.querySelector("h3");

// criando um ouvinte
frm.addEventListener('submit', (e) => {
    const nome = frm.nome.value; // Declare 'nome' com 'const' ou 'let'
    resp.innerText = `Olá ${nome}`;
    console.log("passou por aqui");
    e.preventDefault(); // evita o envio do form
});


