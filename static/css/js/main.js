document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('driverSearch');
    
    if (searchInput) {
        searchInput.addEventListener('keyup', function() {
            const value = this.value.toLowerCase();
            const cards = document.querySelectorAll('.col');

            cards.forEach(card => {
                const name = card.querySelector('.card-title').textContent.toLowerCase();
                if (name.includes(value)) {
                    card.style.display = "block";
                } else {
                    card.style.display = "none";
                }
            });
        });
    }
});