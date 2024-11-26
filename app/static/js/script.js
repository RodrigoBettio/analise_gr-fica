document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("toggle-btn").addEventListener("click", function () {
        var sidebar = document.querySelector(".sidebar");
        var content = document.querySelector(".content");
        var toggleBtn = document.getElementById("toggle-btn");

        // Alterna a classe 'open' na sidebar e no botão
        sidebar.classList.toggle("open");
        content.classList.toggle("shifted");
        toggleBtn.classList.toggle("open");

        if (sidebar.classList.contains("open")) {
            toggleBtn.style.left = "50px"; // Movimenta a flecha 
        } else {
            toggleBtn.style.left = "10px"; // Retorna à posição inicial
        }
    });

    let scrollPosition = 0;
    
    window.addEventListener("load", function() {
        setTimeout(function() {
            window.scrollTo(0, document.body.scrollHeight);
        }, 100); // Delay de 100ms para garantir que a página tenha sido renderizada
    });
});
