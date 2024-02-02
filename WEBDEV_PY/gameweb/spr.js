// Get references to the HTML elements
const userChoiceDisplay = document.getElementById('head');
const resultDisplay = document.getElementById('head1');

// Function to generate the computer's choice (rock, paper, or scissors)
function getComputerChoice() {
    const choices = ['rock', 'paper', 'scissor'];
    const randomIndex = Math.floor(Math.random() * 3);
    return choices[randomIndex];
}

// Function to determine the winner of the game
function determineWinner(userChoice, computerChoice) {
    if (userChoice === computerChoice) {
        return 'draw';
    } else if (
        (userChoice === 'rock' && computerChoice === 'scissor') ||
        (userChoice === 'paper' && computerChoice === 'rock') ||
        (userChoice === 'scissor' && computerChoice === 'paper')
    ) {
        return 'win';
    } else {
        return 'lose';
    }
}

// Function to update the result display based on the game outcome
function updateResultDisplay(outcome, computerChoice) {
    switch (outcome) {
        case 'win':
            resultDisplay.textContent = `You won! Computer chose ${computerChoice}.`;
            break;
        case 'draw':
            resultDisplay.textContent = `It's a draw! Computer also chose ${computerChoice}.`;
            break;
        case 'lose':
            resultDisplay.textContent = `You lost! Computer chose ${computerChoice}.`;
            break;
    }
}

// Functions for user choices
function rock() {
    const userChoice = 'rock';
    const computerChoice = getComputerChoice();
    const outcome = determineWinner(userChoice, computerChoice);
    userChoiceDisplay.textContent = `Your Move: ${userChoice}`;
    updateResultDisplay(outcome, computerChoice);
}

function paper() {
    const userChoice = 'paper';
    const computerChoice = getComputerChoice();
    const outcome = determineWinner(userChoice, computerChoice);
    userChoiceDisplay.textContent = `Your Move: ${userChoice}`;
    updateResultDisplay(outcome, computerChoice);
}

function scissor() {
    const userChoice = 'scissor';
    const computerChoice = getComputerChoice();
    const outcome = determineWinner(userChoice, computerChoice);
    userChoiceDisplay.textContent = `Your Move: ${userChoice}`;
    updateResultDisplay(outcome, computerChoice);
}
