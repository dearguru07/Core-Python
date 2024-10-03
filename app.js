// function Genarate(){
//     let otp=''
//     otp=Math.floor(Math.random()*1000)+1000
//     return otp
// }
// console.log(Genarate())


// function GenarateOTP(){
//     let OTP=''
//     OTP=Math.floor(Math.random()*9000)
//     return OTP
// }
// console.log(GenarateOTP())


// let number=3
// let result=number==1?"telugu":number==2?"hindi":number==3?"tamil":number==4?"english":"marati"
// console.log(result)

// if(number==0){
//     console.log("no ")
// }


// let arry=[10,20,5,8,5,88,58]
// let res=arry.reduce(cur,max){
//     return 
// }


// function GenarateOTP(){
//     let OTP=''
//     OTP=Math.floor(Math.random()*9000)
//     return OTP
// }
// console.log(GenarateOTP())


// var Hello=()=>{
//     console.log("say hwloop")
// }
// Hello();


// name()
// var name =()=>{
//     console.log("hello")
// }

// function OTP(){
//     let otp=Math.floor(Math.random()*9999)
//     console.log(otp)
// }
// OTP()

// async function download(){
//     let data=await fetch("https://type.fit/api/quotes")
//     let originalData=await data.json()
//     console.log(originalData)
// }



console.log('One...')
console.log('Two...')

let myPromise=new Promise((resolve,reject)=>{
resolve()
console.log('Threee')
console.log('Four..')
})
myPromise.then(()=>{
    console.log('Five..')
    console('Six...')
}).catch(()=>{
    console.log('error code it is.......')
})