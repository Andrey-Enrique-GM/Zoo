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
