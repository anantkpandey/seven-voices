// decrees.js - Interactive Decrees and Gains Filtering
// For King Bran Stark, crafted by Tyrion, Hand of the King, April 10, 2025

// Toggle bold on decree click (existing)
document.querySelectorAll('#decree-list li').forEach(item => {
    item.addEventListener('click', () => {
        item.classList.toggle('bold');
    });
});

// Filter gains by day on click
document.querySelectorAll('.gain').forEach(gain => {
    gain.addEventListener('click', () => {
        // Extract day from text (e.g., "Day 3: ...")
        const dayText = gain.textContent.match(/Day \d+/)[0]; // "Day 3"
        const dayNum = parseInt(dayText.split(' ')[1]); // 3

        // Get all gains
        const allGains = document.querySelectorAll('.gain');
        
        // If already filtered to this day, reset to show all
        if (gain.classList.contains('filtered')) {
            allGains.forEach(g => {
                g.style.display = 'list-item'; // Show all
                g.classList.remove('filtered');
            });
        } else {
            // Filter: Show only gains with same day
            allGains.forEach(g => {
                const gDayText = g.textContent.match(/Day \d+/)[0];
                const gDayNum = parseInt(gDayText.split(' ')[1]);
                if (gDayNum === dayNum) {
                    g.style.display = 'list-item'; // Show match
                    g.classList.add('filtered');
                } else {
                    g.style.display = 'none'; // Hide non-match
                }
            });
        }
    });
});