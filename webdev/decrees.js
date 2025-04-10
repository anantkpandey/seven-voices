// decrees.js - Interactive Decrees and Gains Filtering with Reset
// For King Bran Stark, crafted by Tyrion, Hand of the King, April 10, 2025

// Toggle bold on decree click
document.querySelectorAll('#decree-list li').forEach(item => {
    item.addEventListener('click', () => {
        item.classList.toggle('bold');
    });
});

// Filter gains by day on click
document.querySelectorAll('.gain').forEach(gain => {
    gain.addEventListener('click', () => {
        const dayText = gain.textContent.match(/Day \d+/)[0]; // "Day 3"
        const dayNum = parseInt(dayText.split(' ')[1]); // 3
        const allGains = document.querySelectorAll('.gain');
        
        if (gain.classList.contains('filtered')) {
            allGains.forEach(g => {
                g.style.display = 'list-item';
                g.classList.remove('filtered');
            });
        } else {
            allGains.forEach(g => {
                const gDayText = g.textContent.match(/Day \d+/)[0];
                const gDayNum = parseInt(gDayText.split(' ')[1]);
                if (gDayNum === dayNum) {
                    g.style.display = 'list-item';
                    g.classList.add('filtered');
                } else {
                    g.style.display = 'none';
                }
            });
        }
    });
});

// Reset all gains on button click
document.getElementById('reset-gains').addEventListener('click', () => {
    const allGains = document.querySelectorAll('.gain');
    allGains.forEach(gain => {
        gain.style.display = 'list-item'; // Show all
        gain.classList.remove('filtered'); // Clear filter state
    });
});