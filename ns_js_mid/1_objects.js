// Object:- key value

const user = {
    name: "Loni",
    age: 23,
    emailID: "loni123@.gmail.com",
    amount: 4000,
    "home adr": "Bengalore",
    greeting: function(){
        console.log(`I'm comming now: ${this.name}`);
        return 30;
    }
}

const this_key = user.greeting();
console.log(this_key)

// For-Of

/*
for (let [key, val] of Object.entries(user)){
    console.log(key, val)
}
name Loni
age 23
emailID loni123@.gmail.com
amount 4000
home adr Bengalore
*/

/*
for (let key_val of Object.entries(user)){
    console.log(key_val)
}
[ 'name', 'Loni' ]
[ 'age', 23 ]
[ 'emailID', 'loni123@.gmail.com' ]
[ 'amount', 4000 ]
[ 'home adr', 'Bengalore' ]
*/



// For-Of Loop [not-use-direct]
// then using keys,value,key:vaalue

/*
const temp_arr = Object.keys(user)
console.log(temp_arr) // [ 'name', 'age', 'emailID', 'amount', 'home adr' ]

for (keys of Object.keys(user)){
    console.log(keys)
}
name
age
emailID
amount
home adr
*/


// Obj destruture

/*
const {name, age} = user;
console.log(name, age)  // loni, 23
*/

/*
const name = user.name
const age = user.age
console.log(name, age)
*/

// Better-obj-destruture
/*
const {name, age} = user;
console.log(name, age)
*/

// ARRAY-destruture
/*
const arr = [1,2,3,4,5]
const [first, sec] = arr;
console.log(first, sec)  //  1,2
*/

// Loops

// 1.For in KEYS
/*
for(let keys in user){
    console.log(i)
}
name
age
emailID
amount
home adr
*/

// 2. For in VALUES
/*
for(let keys in user){
    console.log(user[keys])
}
Loni
23
loni123@.gmail.com
4000
Bengalore
*/

/*
console.log(Object.keys(user)) // [ 'name', 'age', 'emailID', 'amount', 'home adr' ]

console.log(Object.values(user)) // [ 'Loni', 23, 'loni123@.gmail.com', 4000, 'Bengalore' ]

console.log(Object.entries(user))
 
[
  [ 'name', 'Loni' ],
  [ 'age', 23 ],
  [ 'emailID', 'loni123@.gmail.com' ],
  [ 'amount', 4000 ],
  [ 'home adr', 'Bengalore' ]
]
*/

// Same refere then both will same value
/*
const user2 = user
user2.age = 100

console.log(user)  // age = 100
console.log(user2)  // age = 100
*/

// Specing in var name "a b"
// console.log(user)

/*
console.log(user["age"])  // 23
console.log(user.age)  // 23
*/


/*
console.log(user) // { name: 'Loni', age: 23, emailID: 'loni123@.gmail.com', amount: 4000 }
console.log(typeof user) // object
console.log(user.age) // 23
*/

// CURD Operation

// Read
// console.log(user)

// Create
/*
user.aadhar = '1212 2334 6754'
console.log(user)
*/


// Update
/*
user.amount = 5000;
console.log(user)  //update
*/

// Delete
/*
delete user.emailID
console.log(user) //{ name: 'Loni', age: 23, amount: 4000 }
*/

