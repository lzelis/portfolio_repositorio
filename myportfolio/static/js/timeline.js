document.addEventListener('DOMContentLoaded', function () {
    const timelinePoints = document.querySelectorAll('.timeline-point');
    const rocket = document.getElementById('rocket');
    const timelineLine = document.querySelector('.timeline-line');

    // Asegura que el cohete se posicione inicialmente sobre el primer punto
    rocket.style.position = 'absolute'; // Necesario para moverlo
    rocket.style.transition = 'transform 0.3s ease-in-out'; // Movimiento suave

    // Función para mover el cohete
    function moveRocketToPoint(point) {
        const pointRect = point.getBoundingClientRect();
        const lineRect = timelineLine.getBoundingClientRect();

        // Calculamos la posición horizontal central del punto
        const pointCenter = pointRect.left + pointRect.width / 2;
        const relativeLeft = pointCenter - lineRect.left;

        // Movemos el cohete en el eje X
        rocket.style.transform = `translateX(${relativeLeft}px) translateX(-50%)`; // Centrado sobre el punto

        // No modificamos la posición vertical para que se quede sobre la línea
    }

    // Cuando el ratón entra sobre un punto, movemos el cohete
    timelinePoints.forEach(point => {
        point.addEventListener('mouseenter', () => {
            moveRocketToPoint(point);
        });
    });

    // Inicializamos el cohete en el primer punto
    if (timelinePoints.length > 0) {
        moveRocketToPoint(timelinePoints[0]);
    }
});