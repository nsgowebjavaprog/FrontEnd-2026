// 1.ADD 

/*
// how to add "H2" text in screen
const new_element_h2 =  document.createElement("h2");

// Enter text
new_element_h2.textContent = "H2 Element added by JS"
// add ID
new_element_h2.id = "second"

// print inscreen after "H1"

// select element
const element_h1 = document.getElementById("first")

// Add "after H1" on screen after/before [any-one]
element_h1.after(new_element_h2)
// element_h1.before(new_element_h2)

// 2
const new_element_h3 = document.createElement('h3')
new_element_h3.textContent = 'H3 content by using JS'
new_element_h3.id = "third"
new_element_h3.className = 'diwali'
// add - remove using classList.add/remove

// CSS
new_element_h3.style.backgroundColor = 'blue'
new_element_h3.style.fontSize = '30px'

new_element_h2.after(new_element_h3)
console.log(new_element_h2.getAttribute('id'))

new_element_h2.setAttribute("hello", "hello-ji-it setattribute")




// List-in HTML code

const list1 = document.createElement("li");
list1.textContent = "Milk"

const list2 = document.createElement("li");
list2.textContent = "Cake"

const list3 = document.createElement("li");
list3.textContent = "Cola"

const unorderElement = document.getElementById("listing");
unorderElement.append(list1);
unorderElement.append(list2);  // append  

// unorderElement.append(list1, list2); 

unorderElement.prepend(list3);  // prepend
*/
// NOT-OPTIMIZED METHOD FOR UI
/*
const arr = ["milk", "halw","panner", "tofu", "Tea"]

const unorderElement = document.getElementById("listing");

for(let food of arr){
    const list = document.createElement("li");
    list.textContent = food;
    unorderElement.append(list);
}
*/

// MOST OPTIMAL WAY TO CREATE UI/FRONTEND USiNG JavaScript

const arr = ["ABCD", "EFGH", "IJKLM", "NOPQ", "WXYZ"];

const unorderElement = document.getElementById("listing");

// Create a DocumentFragment
const fragment = document.createDocumentFragment();

for (let food of arr) {
    const list = document.createElement("li");
    list.textContent = food;
    fragment.append(list);
}

// Append all list items to the <ul> at once
unorderElement.append(fragment);

// 2. DELETE 
/*
const s1 = document.getElementById("first");
s1.remove();
*/