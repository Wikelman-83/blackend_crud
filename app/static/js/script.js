document.getElementById('user-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const datos = {
    nombre: document.getElementById('nombre').value,
    edad: document.getElementById('edad').value,
    correo: document.getElementById('correo').value,
    clasificacion: document.getElementById('clasificacion').value
  };

  try {
    const res = await fetch('/submit', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(datos)
    });
    const body = await res.json();
    
    // Mostrar el mensaje de éxito
    document.getElementById('mensaje').textContent = body.message;
    
    // Limpiar los campos del formulario si la respuesta es exitosa
    if (res.ok) {
      document.getElementById('user-form').reset();  // Esto limpia los campos
    }

  } catch (err) {
    document.getElementById('mensaje').textContent = 'Error al enviar datos.';
    console.error(err);
  }
});
