
document.addEventListener('DOMContentLoaded', () => {
  const paisSelect = document.getElementById('pais');
  const ciudadSelect = document.getElementById('ciudad');
  const form = document.getElementById('form-paquetes');
  const tablaPaquetes = document.querySelector('#tabla-paquetes tbody');

  fetch('/api/paises')
      .then(response => response.json())
      .then(data => {
          data.forEach(pais => {
              const option = document.createElement('option');
              option.value = pais.id;
              option.textContent = pais.nombre;
              paisSelect.appendChild(option);
          });
      })
      .catch(err => console.error('Error al cargar países:', err));

  paisSelect.addEventListener('change', () => {
      const paisId = paisSelect.value;
      ciudadSelect.innerHTML = '';
      ciudadSelect.disabled = true;

      if (paisId) {
          fetch(`/api/paises/${paisId}/ciudades`)
              .then(response => response.json())
              .then(data => {
                  data.forEach(ciudad => {
                      const option = document.createElement('option');
                      option.value = ciudad.id;
                      option.textContent = ciudad.nombre;
                      ciudadSelect.appendChild(option);
                  });
                  ciudadSelect.disabled = false;
              })
              .catch(err => console.error('Error al cargar ciudades:', err));
      }
  });

  form.addEventListener('submit', (e) => {
      e.preventDefault();

      const datos = {
          pais: paisSelect.options[paisSelect.selectedIndex].text,
          ciudad: ciudadSelect.options[ciudadSelect.selectedIndex]?.text,
          fechaIda: document.getElementById('fechaIda').value,
          fechaRegreso: document.getElementById('fechaRegreso').value,
          tipoPaquete: document.getElementById('tipoPaquete').value,
      };

      fetch('/api/generar-paquetes', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(datos),
      })
          .then(response => response.json())
          .then(data => {
              tablaPaquetes.innerHTML = '';
              data.paquetes.forEach(paquete => {
                  const row = tablaPaquetes.insertRow();
                  row.innerHTML = `
                      <td>${paquete.Destino}</td>
                      <td>${paquete.descripcion}</td>
                      <td>${paquete.precio}</td>
                      <td>${paquete.fecha_salida}</td>
                      <td>${paquete.fecha_regreso}</td>
                  `;
              });
          })
          .catch(err => console.error('Error al generar paquetes:', err));
  });
});
