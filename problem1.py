let arr = [1, 2, 3, 4];
function doubleNum(n){
    return n*2;
}
let doubledArr = arr.map(doubleNum);
let mulBy4=arr.map((n)=>n*4);
console.log(mulBy4);
console.log(doubledArr);

// array objects
let obj=[
    {name:"Mouse",price:500},  //can create multiple array
    {name:"keyboard",price:2000},
    {name:"Monitor",price:5000}, 
]  
console.log(obj.name);   //return undefined
console.log(obj[0].name);   //return Mouse
console.log(obj[1].price);  //return 2000
console.log(obj[2].name);   //return Monitor

// use map:
let productname=obj.map((n)=>n.name);   //return ["Mouse","keyboard","Monitor"]
let productprice=obj.map((n)=>n.price);    //return [500,2000,5000]
console.log(productname);
console.log(productprice);
let highvalue=obj.filter((n)=>n.price>1000);
console.log(highvalue);

// use filter:

let arr1=[1,2,3,4,5,6,7,8,9,10];
let even=arr1.filter((n)=>n%2==0);  //return [2,4,6,8,10]
let odd=arr1.filter((n)=>n%2!=0);   //return [1,3,5,7,9]
console.log(even);
console.log(odd);
//filter using function:
function iseven(n){
    return n%2==0;;
}
function isodd(n){
    return n%2!=0;;
}
let evennum=arr1.filter(iseven);
let oddnum=arr1.filter(isodd);
console.log(evennum);
console.log(oddnum);

//reduce:
let sumArr=arr1.reduce((total,curr)=>total+curr,0);
console.log(sumArr);
//reduce using function:
function sum(total,curr){
    return total+curr;
}
let sumArr1=arr1.reduce(sum,0);
console.log(sumArr1);
//spread and rest:
let arr3=[...arr,...arr1];
console.log(...arr1);
console.log(...arr3);

const merge=(one,...numbers)=>
    {
        console.log(one);
        console.log(numbers);
    }
merge(1,2,3,4,5);

//DESTRUCTURING:
let [num1,num2,...num3]=arr1;
console.log(num1,num2,num3);       //[1,2,[3,4,5,6,7,8,9,10]]
let [a,b]=[10,20];
console.log(a,b);                  //10,20
let student={name:"John",mark:78,age:20};        
let {name,mark,age}=student;
console.log(name,mark,age);     // John,78,20
