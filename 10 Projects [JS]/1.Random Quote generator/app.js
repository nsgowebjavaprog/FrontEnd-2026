const quotes = [
    'sdads',
    'asdds',
    'tyjjtrt',
    'sdads',
    'asdds',
    'tyjjtrt',
    'sdads',
    'asdds',
    'tyjjtrt',
    'sdads',
    'asdds',
    'tyjjtrt',
    'sdads',
    'asdds',
    'tyjjtrt',
    'sdads',
    'asdds',
    'tyjjtrt',
    'sdads',
    'asdds',
    'tyjjtrt'
]

const button = document.querySelector('button');
const quote = document.querySelector('h1');

button.addEventListener('click', ()=>{
    const index = Math.floor(Math.random()*20);
    quote.textContent = quotes[index];
})