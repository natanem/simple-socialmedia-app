const year = document.querySelector('.year')
const nav = document.querySelector('nav')
const testBtn = document.querySelector('.test_btn')

year.textContent = new Date().getFullYear()



window.addEventListener('scroll', e => {
    if(scrollY > 5){

        nav.classList.add('border-bottom')
    }else{
        nav.classList.remove('border-bottom')
    }
})

testBtn.addEventListener('click', e =>{
    e.preventDefault()
    console.log('test button clicked')
    fetch(`api/${3}/likes/add`)
    .then(response => {
        console.log(response)
    })
})

