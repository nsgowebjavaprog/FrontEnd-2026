const parent = document.getElementById('parent');

parent.addEventListener('click',(e)=>{
    const chils = e.target;
    const body = document.querySelector('body');
    body.style.backgroundColor = chils.id;
})