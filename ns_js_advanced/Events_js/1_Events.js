// WAY-1  [Event]
/*
function handleClick(){
    const element = document.getElementById('first');
    element.textContent = "Change to Loni Bhai";
}
*/

// WAY-2 [Event]
/*
const element= document.getElementById('first');
element.onclick = function handleClick(){
    element.textContent = "Change to Loni Bhai - 1st time";
}
// Overriding Then.......?
element.onclick = function handleClick(){
    element.textContent = "Change to Loni Bhai - 2nd time";
}
*/

// WAY-3 [EventListener]
/*
const element= document.getElementById('first');
element.addEventListener('click', () =>{
    element.textContent = "Change to Loni Bhai";
    // No-Overriding
    element.style.backgroundColor = 'pink';
})

*/

// WAY-4 [EventListener-DOUBLE-CLIICK]
/*
const element= document.getElementById('first');
element.addEventListener('dblclick', () =>{
    element.textContent = "Change to Loni Bhai";
    // No-Overriding
    element.style.backgroundColor = 'pink';
})
*/

// WAY-5 [EventListener-mouseenter]
/*
const element= document.getElementById('first');
element.addEventListener('mouseenter', () =>{
    element.textContent = "Change to Loni Bhai";
    // No-Overriding
    element.style.backgroundColor = 'pink';
})
*/

// WAY-6 [EventListener-mouseleave]
/*
const element= document.getElementById('first');
element.addEventListener('mouseleave', () =>{
    element.textContent = "Change to Loni Bhai";
    // No-Overriding
    element.style.backgroundColor = 'pink';
})
*/

/*
// DiV Project 

// id="child1" class="child" 

const child1 = document.getElementById('child1');
child1.addEventListener('click', () => {
    child1.textContent = "It's Clicked"
})

// For all 5-Div @ 1's

const parent = document.getElementById('parent');
// using for-loop

for(let child of parent.children){
    child.addEventListener('click',() =>{
        child.textContent = "I am child a clicked now";
    })
}
*/

// grandparent Covers all 3
// parent Covers all 2 [parent, child]
/* 
const grandparent = document.getElementById("grandparent");
grandparent.addEventListener('click', ()=>{
    // grandparent.textContent='grandparent is clicked';
    console.log('grandparent is clicked');
})

const parent = document.getElementById("parent");
parent.addEventListener('click', ()=>{
    // parent.textContent='parent is clicked';
    console.log('parent is clicked');
})

const child = document.getElementById("child");
child.addEventListener('click', ()=>{
    // child.textContent='child is clicked';
    console.log('child is clicked');
})
*/
/*

const grandparent = document.getElementById("grandparent");
grandparent.addEventListener('click', ()=>{
    // grandparent.textContent='grandparent is clicked';
    console.log('grandparent is clicked');
},true)

const parent = document.getElementById("parent");
parent.addEventListener('click', ()=>{
    // parent.textContent='parent is clicked';
    console.log('parent is clicked');
},true)

const child = document.getElementById("child");
child.addEventListener('click', ()=>{
    // child.textContent='child is clicked';
    console.log('child is clicked');
},true)
*/

/*
true---> from grad-->parent--->child
true---> from grad-->parent
true---> from grad

*/

// ---------------------------------------------

const grandparent = document.getElementById("grandparent");
grandparent.addEventListener('click', ()=>{
    // grandparent.textContent='grandparent is clicked';
    console.log('grandparent is clicked');
},false)

const parent = document.getElementById("parent");
parent.addEventListener('click', ()=>{
    // parent.textContent='parent is clicked';
    console.log('parent is clicked');
},false)

const child = document.getElementById("child");
child.addEventListener('click', ()=>{
    // child.textContent='child is clicked';
    console.log('child is clicked');
},false)

/*
false --> child --> parent --> grandparent
false --> child --> parent
false --> child 

*/
