
// Pegando a interface inícial
var home = document.getElementById('home')

// Pegando a interface do input
var view = document.getElementById('view')


function btn_adcionaTasks() {

    home.style.display = 'none' // Some a interface de início

    view.style.display = 'flex' // Aparece a interface do input

}

function btn_deleteTasks() {
    btn_adcionaTasks() // Chama a função do btn_adcionaTasks
}

function btn_renomeiaTasks() {
    btn_adcionaTasks() // Chama a função do btn_adcionaTasks
}

function btn_voltar() {

    view.style.display = 'none' // Some a interface do input

    home.style.display = 'flex' // Aparece a interface de início

}