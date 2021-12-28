const data = {
    compilerOptions.delimiters: ["[[", "]]"],
    compilerOptions: {
        delimiters: ["[[", "]]"],
    }
    data() {
        return {
            firstName : 'Johon'
        }
    }
}

Vue.createApp(data).mount('#app')

