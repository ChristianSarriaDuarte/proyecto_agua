(function(){

    const btnEliminacion=document.querySelectorAll (".btnEliminacion");

    btnEliminacion.forEach(btn=>{
        btn.addEventListener('click', (e)=>{
            const confirmacion=confirm('Seguro de eliminar el curso?');
            if(!confirmacion){
                e.preventDefault();
            }

        });

    });
    })();

    let pedidoCount = 0;

    // Función para actualizar el contador en el carrito
    function updateCarritoCount() {
        const carritoCountElement = document.getElementById('carrito-count');
        carritoCountElement.textContent = pedidoCount;
    }
    
    // Agregar al carrito
    function addToCarrito() {
        const cantidad = document.getElementById('cantidad-input').value;
    
        if (cantidad > 0 && cantidad <= 100) {
            pedidoCount += 1; // Incrementar el número de pedidos
            updateCarritoCount();
        } else {
            alert('La cantidad debe estar entre 1 y 100.');
        }
    }
    