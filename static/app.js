const API_URL = '/api/v1/play';

async function fetchClips() {
    try {
        const response = await fetch(API_URL + '/');
        const clips = await response.json();
        renderClips(clips);
    } catch (error) {
        console.error('Error fetching clips:', error);
    }
}

function renderClips(clips) {
    const container = document.getElementById('clip-list');
    container.innerHTML = '';

    clips.forEach(clip => {
        const card = document.createElement('div');
        card.className = 'clip-card';

        card.innerHTML = `
            <div class="clip-title">${clip.title}</div>
            <div class="clip-meta">
                <span>${clip.genre}</span>
                <span>${clip.duration}s</span>
            </div>
            <p>${clip.description}</p>
            <div class="clip-meta">
                <span>Plays: <span id="plays-${clip.id}">${clip.play_count}</span></span>
            </div>
            <button class="play-btn" onclick="playClip(${clip.id}, this)">Play Preview</button>
        `;
        container.appendChild(card);
    });
}

async function playClip(id, btn) {
    // Create audio element if not exists or replace
    let audio = btn.parentElement.querySelector('audio');

    if (!audio) {
        audio = document.createElement('audio');
        audio.controls = true;
        audio.autoplay = true;

        // Use the stream endpoint
        audio.src = `${API_URL}/${id}/stream`;

        // Replace button with audio player
        btn.replaceWith(audio);

        // Update stats after a short delay to reflect the play
        setTimeout(() => updateStats(id), 1000);
    }
}

async function updateStats(id) {
    try {
        const response = await fetch(`${API_URL}/${id}/stats`);
        const stats = await response.json();
        const playsElement = document.getElementById(`plays-${id}`);
        if (playsElement) {
            playsElement.textContent = stats.play_count;
        }
    } catch (error) {
        console.error('Error updating stats:', error);
    }
}

document.addEventListener('DOMContentLoaded', fetchClips);
