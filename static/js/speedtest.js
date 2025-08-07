const detectSpeedBtn = document.getElementById('detect-speed');
const resultsEl = document.getElementById('network-speeds');
detectSpeedBtn.addEventListener('click', async () => {
    detectSpeedBtn.disabled = true;
    StartSpeed(true)
    try {
        const response = await fetch('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/132C_trans.gif/230px-132C_trans.gif?time=' + (new Date().getTime()));
        const fileSize = response.headers.get('content-length');
        const startTime = performance.now();
        await response.blob();
        const endTime = performance.now();
        const duration = (endTime - startTime) / 1000; // Em segundos
        const speedMbps = (fileSize * 8) / (duration * 1024 * 1024); // Em Mbps
        const uploadSize = 1024 * 1024; // Tamanho do arquivo de upload em bytes (1MB)
        const uploadSpeedMbps = (uploadSize * 8) / (duration * 1024 * 1024); // Em Mbps
        resultsEl.innerHTML = `Download: ${speedMbps.toFixed(2)} Mbps<br>Upload: ${uploadSpeedMbps.toFixed(2)} Mbps`;
        StartSpeed(false)
    } catch (error) {
        resultsEl.innerHTML = 'Ocorreu um erro ao realizar o teste de velocidade.';
        StartSpeed(false)
        console.error(error);
    }
    detectSpeedBtn.disabled = false;
});

function StartSpeed(condicao) {
    const spinner = document.getElementById('spinner-id');
    const botao = document.getElementById('detect-speed');
    const toastLiveExample = document.getElementById('Toast-SpeedTest');
    const toastBootstrap = new bootstrap.Toast(toastLiveExample);
    if (condicao) {
        spinner.classList.add('d-block');
        spinner.classList.remove('d-none');
        botao.disabled = true;
    } else {
        spinner.classList.remove('d-block');
        spinner.classList.add('d-none');
        botao.disabled = false;
        atualizarHoraAtual()
        toastBootstrap.show();
    }
}

function atualizarHoraAtual() {
    const horaElement = document.getElementById('Toast-SpeedTest-hora');
    function formatarHora(hora) {
        return hora.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }
    // Obter a hora atual
    const horaAtual = new Date();
    // Formatar a hora atual
    const horaFormatada = formatarHora(horaAtual);
    // Atualizar o conteúdo do elemento com a hora atual formatada
    horaElement.textContent = horaFormatada;
}
