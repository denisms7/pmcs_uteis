document.addEventListener("DOMContentLoaded", () => {
  const botoes = document.querySelectorAll(".alerta-btn");
  const classes = ["btn-danger", "btn-success"];
  let indice = 0;

  if (botoes.length === 0) {
    console.warn("Nenhum botão com a classe .alerta-btn encontrado.");
    return;
  }

  setInterval(() => {
    botoes.forEach((botao) => {
      botao.classList.remove(classes[indice]);
      botao.classList.add(classes[(indice + 1) % classes.length]);
    });
    indice = (indice + 1) % classes.length;
  }, 500);
});
