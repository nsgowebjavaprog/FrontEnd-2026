const form = document.querySelector('form');
const allTask = document.querySelector('#allTask');
const input = document.querySelector('input');

form.addEventListener('sibmit', (e)=>{
    e.preventDefault();

    const text = input.value.trim();
    
    if(text == "")
        return;

    const parent = document.createElement('div');

    const task = document.createElement('span');
    task.textContent = text


    const deletebutton = document.createElement('button');
    deletebutton.textContent = "Delete";

    const donebutton = document.createElement('button');
    donebutton.textContent = "done";


})