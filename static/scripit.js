function openModal(tipo) {
    const modal = document.getElementById("infoModal");
    const body = document.getElementById("modalBody");
    
    let conteudo = "";

    if(tipo === 'enem') {
        conteudo = `
            <h2><i class="fas fa-book"></i> Estratégia ENEM 2026</h2>
            <p style="margin-top:15px">Nathália, preparamos um cronograma de estudos focado nas suas maiores dificuldades em Estatística e Linguagens.</p>
            <ul style="margin: 20px 0; padding-left: 20px;">
                <li>Revisão de Redação: Nota 1000</li>
                <li>Matemática Financeira aplicada</li>
            </ul>
            <button class="btn-main" onclick="addPoints(50)">Marcar como lido (+50 pts)</button>
        `;
    } else if (tipo === 'sisu') {
        conteudo = `
            <h2><i class="fas fa-university"></i> Simulador SISU</h2>
            <p>Com base no seu perfil, aqui estão as faculdades mais buscadas pela VortexTech na sua região.</p>
            <canvas id="myChart" style="width:100%; height:200px; background:#f0f0f0; margin-top:10px"></canvas>
        `;
    }

    body.innerHTML = conteudo;
    modal.style.display = "block";
}

function closeModal() {
    document.getElementById("infoModal").style.display = "none";
}

function addPoints(pts) {
    let current = parseInt(document.getElementById("userPoints").innerText);
    document.getElementById("userPoints").innerText = current + pts;
    alert("Parabéns, Nathália! Você ganhou pontos Vortex!");
    closeModal();
}

if(topic === 'vestibular') {
    html = "<h2>🎓 Vestibulares 2026</h2><p>As inscrições para a Fuvest e Unicamp começam em breve. Fique atento aos prazos de isenção!</p>";
} else if(topic === 'processos') {
    html = "<h2>📋 Processos Seletivos</h2><p>Existem 5 novos editais para cursos técnicos gratuitos na sua região. Confira os pré-requisitos.</p>";
}

window.onclick = function(event) {
    let modal = document.getElementById("infoModal");
    if (event.target == modal) closeModal();
}

let usuarioLogado = false; 

function acessarConteudo(trilha) {
    if (!usuarioLogado) {
        alert("Ops! Nathália, você precisa estar logada para acessar essa trilha da VortexTech.");
        window.location.href = "cadastro.html"; 
    } else {
        openModal(trilha); 
    }
}

function salvarPerfil() {
    const nome = document.getElementById('nomePerfil').value;
    alert("Parabéns, Nathália! Suas informações da VortexTech foram atualizadas com sucesso para: " + nome);
    
}

function logout() {
    if(confirm("Deseja realmente sair da conta?")) {
        window.location.href = "index.html";
    }
}


function previewFoto(event) {
    const reader = new FileReader();
    const fotoExibicao = document.getElementById('fotoExibicao');
    const avatarLetra = document.getElementById('avatarLetra');

    reader.onload = function() {
        if (reader.readyState === 2) {
            fotoExibicao.src = reader.result;
            fotoExibicao.style.display = "block"; 
            avatarLetra.style.display = "none";
        }
    }

    if (event.target.files[0]) {
        reader.readAsDataURL(event.target.files[0]);
    }
}


function salvarPerfil() {
    const nome = document.getElementById('nomePerfil').value;
    alert("VortexTech: Alterações salvas para " + nome + "!");
}


function logout() {
    if(confirm("Deseja sair do Horizonte?")) {
        window.location.href = "index.html";
    }
}

function finalizarCadastro() {
    const nome = document.getElementById('cadNome').value;
    

    alert("Bem-vinda à VortexTech, " + nome + "! Sua conta foi criada com sucesso.");
    
   
    window.location.href = "index.html";
}