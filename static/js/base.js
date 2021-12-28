const year = document.querySelector('.year')
const nav = document.querySelector('nav')
const testBtn = document.querySelector('.test_btn')
const searchForm = document.querySelector('.search-form')
const searchInput = document.querySelector('#search-input')
const searchSuggestion = document.querySelector('#search-suggestion')

// const output = document.querySelector('#output')


year.textContent = new Date().getFullYear()



window.addEventListener('scroll', e => {
    if(scrollY > 5){

        nav.classList.add('border-bottom')
    }else{
        nav.classList.remove('border-bottom')
    }
})

const feeds = []

fetch('http://localhost:8000/api/feeds/')
.then(res => res.json())
.then(data => {
    for(let d of data){
        
        feeds.push(d.content)
    }
})

console.log(feeds)
let output = ''
searchInput.addEventListener('change', e =>{
    output = e.target.value
    e.preventDefault()
       setTimeout(() => {
        output = ''
        output = e.target.value
        console.log(output)
       }, 500);
})