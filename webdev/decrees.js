// decrees.js
document.querySelectorAll('#decree-list li').forEach(item => {
    item.addEventListener('click', () => item.classList.toggle('bold'));
});