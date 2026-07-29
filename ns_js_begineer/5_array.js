/*
In JavaScript, arrays are implemented as 
specialized objects under the hood, 
where numeric indices act as 
property keys that can reference values 
of any data type because the language 
is dynamically typed rather than statically typed.
*/

/*

let arr = [100, 10, "Looni", true]
console.log(arr)
console.log(typeof arr)

*/

// for loop 

/*
let arr = [1,2,3,4,5]

// FOR
for(let i=0; i<=arr.length; i++){
    console.log(i)
}

// FOR-OF
for(let i of arr){
    console.log(i)
}



const arr = [10, 20,30,40,50]
arr[2] = 20;

console.log(arr)

console.log(arr.slice(2,5));



const arr1 = [10, 20,30,40,50]
const arr2 = ["LONI", 11, true]
const arr3 = ["11,12,13,134"]
/// arr1.push(arr2)
// const arr3 = arr1.concat(arr2) // console.log(arr1) // [ 10, 20, 30, 40, 50, [ 'LONI', 11, true ] ]
/*[
  10, 20,   30,
  40, 50,   'LONI',
  11, true
]*/

// const arr4 = [arr1, arr2, arr3]
/*
[ [ 10, 20, 30, 40, 50 ],
  [ 'LONI', 11, true ],
  [ '11,12,13,134' ]
]
*/
/*
const arr5 = [...arr1, ...arr2, ...arr3]

console.log(arr5)  // [ 10, 20, 30, 40, 50, 'LONI', 11, true, '11,12,13,134' ]

*/

const names = ["Allian", "Bab", "cat", "Dog", "Cat", "cat"];

/*
console.log(names)
console.log(names.toString())
console.log(names.join("--"))
console.log(names.includes("cat"))
console.log(names.indexOf("cat"))
console.log(names.lastIndexOf("cat"))


[ 'Allian', 'Bab', 'cat', 'Dog', 'Cat', 'cat' ]
Allian,Bab,cat,Dog,Cat,cat
Allian--Bab--cat--Dog--Cat--cat
true
2
5

*/

// names.sort();  // [ 'Allian', 'Bab', 'Cat', 'Dog', 'cat', 'cat' ]
// names.reverse(); // [ 'cat', 'Cat', 'Dog', 'cat', 'Bab', 'Allian' ]
// console.log(names)


// const nums = [56,34,56,7,67,5,89,45,789,12]
// console.log(nums)
/*
nums.sort((a,b) => a-b);
console.log(nums) // [5, 7, 12, 34,  45, 56, 56, 67, 89, 789 ]

const nums = [56,34,[56,7,789], 12]
console.log(nums[2]) // [ 56, 7, 789 ]

*/
/*

let arr = [100, 10, "Looni", true]
console.log(arr)
console.log(typeof arr)

*/