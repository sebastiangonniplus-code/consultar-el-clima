async function consultarClima() {
    const ciudad = document.getElementById('ciudadInput').value.trim();
    const divResultado = document.getElementById('resultado');
    const divError = document.getElementById('errorMsg');

    // Limpiar estados anteriores
    divResultado.classList.add('d-none');
    divError.classList.add('d-none');

    if (!ciudad) {
        divError.textContent = "Por favor, ingresa el nombre de una ciudad.";
        divError.classList.remove('d-none');
        return;
    }

    try {
        // Petición a tu API de FastAPI corriendo localmente
        const response = await fetch(`http://127.0.0.1:8000/api/weather/${encodeURIComponent(ciudad)}`);
        
        if (!response.ok) {
            throw new Error("Ciudad no encontrada o error en el servidor.");
        }

        const data = await response.json();

        // Mostrar datos en el HTML
        document.getElementById('resCiudad').textContent = data.ciudad;
        document.getElementById('resTemp').textContent = data.temperatura;
        document.getElementById('resSensacion').textContent = data.sensacion_termica;
        document.getElementById('resHumedad').textContent = data.humedad;
        document.getElementById('resDesc').textContent = data.descripcion;

        divResultado.classList.remove('d-none');

    } catch (error) {
        divError.textContent = error.message;
        divError.classList.remove('d-none');
    }
}