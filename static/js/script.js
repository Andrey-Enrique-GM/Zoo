const addChihuahuaButton = document.getElementById('btnAddChihuahua');
const cancelChihuahuaButton = document.getElementById('btnCancelChihuahua');
const chihuahuaForm = document.getElementById('chihuahuaForm');

function setFormVisibility(visible) {
    chihuahuaForm.hidden = !visible;
    addChihuahuaButton.setAttribute('aria-expanded', String(visible));
    if (visible) {
        document.getElementById('tipo').focus();
    }
}

addChihuahuaButton.addEventListener('click', () => {
    setFormVisibility(chihuahuaForm.hidden);
});

cancelChihuahuaButton.addEventListener('click', () => setFormVisibility(false));