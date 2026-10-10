document.addEventListener('DOMContentLoaded', () => {
    const addChihuahuaButton = document.getElementById('btnAddChihuahua');
    const cancelChihuahuaButton = document.getElementById('btnCancelChihuahua');
    const modalOverlay = document.getElementById('modalOverlay');

    function setModalVisibility(visible) {
        if (!modalOverlay) return;

        if (visible) {
            modalOverlay.removeAttribute('hidden');
            addChihuahuaButton.setAttribute('aria-expanded', 'true');
            // Enfocar el primer input al abrir el modal
            const tipoInput = document.getElementById('tipo');
            if (tipoInput) tipoInput.focus();
        } else {
            modalOverlay.setAttribute('hidden', '');
            addChihuahuaButton.setAttribute('aria-expanded', 'false');
        }
    }

    if (addChihuahuaButton) {
        addChihuahuaButton.addEventListener('click', (e) => {
            e.preventDefault();
            setModalVisibility(true);
        });
    }

    if (cancelChihuahuaButton) {
        cancelChihuahuaButton.addEventListener('click', (e) => {
            e.preventDefault();
            setModalVisibility(false);
        });
    }

    // Opcional: cerrar el modal si el usuario hace clic fuera del formulario (en el fondo oscuro)
    if (modalOverlay) {
        modalOverlay.addEventListener('click', (e) => {
            if (e.target === modalOverlay) {
                setModalVisibility(false);
            }
        });
    }
});



document.addEventListener('DOMContentLoaded', () => {
    const btnSelectImage = document.getElementById('btnSelectImage');
    const imagenFile = document.getElementById('imagen_file');
    const imagenPath = document.getElementById('imagen_path');

    if (btnSelectImage && imagenFile) {
        // Al dar clic en el botón del emoji, simular clic en el input file
        btnSelectImage.addEventListener('click', () => {
            imagenFile.click();
        });

        // Cuando el usuario elige un archivo
        imagenFile.addEventListener('change', (e) => {
            if (e.target.files && e.target.files.length > 0) {
                const fileName = e.target.files[0].name;
                // Autocompletar el campo de texto con la ruta relativa que espera la DB
                imagenPath.value = `images/${fileName}`;
            }
        });
    }
});
