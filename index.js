const button = document.querySelector('button');
const outerWheel = document.querySelector('#outer-wheel-2');
const ballContainer = document.querySelector('#ball-container');
const ball = document.querySelector('#ball');
let firstSpin = true;
let spinFinished = true;

const root = document.querySelector(':root');

const categories = [
  "Liqueurs", "Cider", "Cocktails", 
  "Beer (bottle)", "Real Ale", "Beer (draught)", 
  "Gin", "Shots and Bombs", "Beer (craft)", "Vodka", 
  "Wine", "Tequila", "Rum", 
  "Pre-mixed drinks", "Whiskey"
]

// Liqueurs
// Cider
// Cocktails
// Beer (bottle)
// Real Ale
// Beer (draught)
// Gin
// Shots and Bombs
// Beer (craft)
// Vodka
// Wine
// Tequila
// Rum
// Pre-mixed drinks
// Whiskey


function setVariable(key, value) {
  root.style.setProperty(key, value);
}

button.addEventListener('click', roulette)

function roulette() {
  if (firstSpin && spinFinished) {
    firstSpin = false;
    spinBall();
  } else if (spinFinished) {
    spinFinished = false;      
    resetBall()
  }
}

function spinBall() {
  spinFinished = false;

  const ranInt1 = Math.floor(Math.random() * 14)
  const ranInt2 = Math.floor(Math.random() * 14)
  const ballSpin = - (ranInt1 * 24) - 6490
  const wheelSpin = (ranInt2 * 24) + 3240

  const index =  13 - ranInt1;

  console.log(categories[index]);

  setVariable('--num-of-spins', `${wheelSpin}deg`)
  setVariable('--ball-spins', `${ballSpin}deg`)
  
  outerWheel.style.animationName = 'spin';
  ballContainer.style.animationName = 'ball-spin';
  ball.style.animationName = 'ball';
  setTimeout(() => {
    spinFinished = true;
  }, 16000)
}

function resetBall() {
  ballContainer.style.animationName = 'move-ball';
  ballContainer.style.animationDuration = '1s';
  outerWheel.style.animationName = 'move-wheel';
  outerWheel.style.animationDuration = '1s';
  ball.style.animationName = 'move-ball-container';
  ball.style.animationDuration = '1s';
  setTimeout(() => {
    outerWheel.style.animationDuration = '16s';
    ballContainer.style.animationDuration = '16s';
    ball.style.animationDuration = '16s';
    ball.style.animationName = '';
    outerWheel.style.animationName = '';
    ballContainer.style.animationName = '';
    spinBall();
  }, 2000)
}