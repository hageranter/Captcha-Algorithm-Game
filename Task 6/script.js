// Game Data: Images and Categories
const images = [
    {"url": "lOIP - Copy - Copy.jpeg", "category": "history"},
    {"url": "lOIP - Copy - Copy.jpeg", "category": "history"},
    {"url": "lOIP - Copy - Copy.jpeg", "category": "history"},
    {"url": "R - Copy (2) - Copy.jpeg", "category": "sea"},
    {"url": "R - Copy (2) - Copy.jpeg", "category": "sea"},
    {"url": "R - Copy (2) - Copy.jpeg", "category": "sea"},
    {"url": "hi - Copy - Copy.jpg", "category": "Pyramids"},
    {"url": "hi - Copy - Copy.jpg", "category": "Pyramids"},
    {"url": "hi - Copy - Copy.jpg", "category": "Pyramids"},
    ];
    // Game Data: Images and Categories

// Get a random target category
const categories = ['history', 'sea', 'Pyramids'];
const targetCategory = categories[Math.floor(Math.random() * categories.length)];
document.getElementById('target-category').innerText = targetCategory;

// DOM Elements
const gridContainer = document.getElementById('grid');
const checkButton = document.getElementById('check-button');
const feedback = document.getElementById('feedback');

// Track selected cells
let selectedCells = [];

// Generate the grid
function createGrid() {
    images.forEach((image, index) => {
        const cell = document.createElement('div');
        cell.classList.add('image-cell');
        cell.dataset.index = index;

        const img = document.createElement('img');
        img.src = image.url;
        img.alt = image.category;
        cell.appendChild(img);

        cell.addEventListener('click', () => toggleSelection(cell, index));
        gridContainer.appendChild(cell);
    });
}

// Toggle the selection state of a cell
function toggleSelection(cell, index) {
    if (selectedCells.includes(index)) {
        cell.classList.remove('selected');
        selectedCells = selectedCells.filter(i => i !== index);
    } else {
        cell.classList.add('selected');
        selectedCells.push(index);
    }
}

// Check if the selected cells are correct
function checkSelections() {
    const correctSelections = images
        .map((image, index) => (image.category === targetCategory ? index : null))
        .filter(index => index !== null);

    const sortedSelected = [...selectedCells].sort((a, b) => a - b);
    const sortedCorrect = [...correctSelections].sort((a, b) => a - b);

    if (arraysAreEqual(sortedSelected, sortedCorrect)) {
        feedback.textContent = 'Correct! 🎉';
        feedback.style.color = 'green';
    } else {
        feedback.textContent = 'Incorrect. Try Again!';
        feedback.style.color = 'red';
    }
}

// Helper function to compare arrays
function arraysAreEqual(arr1, arr2) {
    return (
        arr1.length === arr2.length &&
        arr1.every((value, index) => value === arr2[index])
    );
}

// Reset feedback and selections
function resetGame() {
    selectedCells = [];
    const cells = document.querySelectorAll('.image-cell');
    cells.forEach(cell => cell.classList.remove('selected'));
    feedback.textContent = '';
}

// Event listener for the "Check Selections" button
checkButton.addEventListener('click', checkSelections);

// Initialize the game
createGrid();
