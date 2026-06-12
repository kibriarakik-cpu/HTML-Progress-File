//json-js obj notation
let object={
    name:"Messi",
    age:39,
    city:"Buenos Aires",
    country:"Argentina",    
    GoalScored:940,
    GOAT:true
};
let parsed=JSON.stringify(object);
console.log(parsed);
let string =JSON.stringify(object);
console.log(string);    
setTimeout(()=>{
    console.log("Messi's first goal in WC26");
},20000);
let Time=setInterval(()=>{
    console.log("Messi's first goal in WC26");
},20000);
setTimeout(()=>{
    clearInterval(Time);
},1000);