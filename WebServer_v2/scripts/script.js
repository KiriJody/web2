window.onload = () => {

    const cards = document.querySelectorAll('.card');

    cards.forEach(element => {
        element.addEventListener('transitionend', function() {
            if (element.style.maxHeight === '0px') {
                element.classList.add("hidden-obj");

                window.location.assign("/");
            }
        });
    });
}

async function RemoveCard(element) {
    await fetch('/remove?' + element.id)
    .then(response => {
        if (!response.ok) {
          throw new Error('Ошибка сети');
        }
        return response.text();
      })
      .then(data => {
        // Обработка полученных данных
        console.log(data);
      })
      .catch(error => {
        // Обработка ошибок
        console.error(error);
      });
}

function removeCard(e) {
    e.parentNode.style.maxHeight = '0';
    RemoveCard(e.parentNode)
}