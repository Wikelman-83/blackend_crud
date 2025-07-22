document.getElementById('user-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const datos = {
    nombre:  document.getElementById('nombre').value,
    edad:    document.getElementById('edad').value,
    correo:  document.getElementById('correo').value,
    clasificacion: document.getElementById('clasificacion').value
  };

  try {
    const res = await fetch('/submit', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(datos)
    });
    const body = await res.json();
    document.getElementById('mensaje').textContent = body.message;
  } catch (err) {
    document.getElementById('mensaje').textContent = 'Error al enviar datos.';
    console.error(err);
  }
});
