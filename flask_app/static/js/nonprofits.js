

var orgForm = document.querySelector("#orgForm")

orgForm.addEventListener("submit", function(event){
    event.preventDefault()
    let value = orgForm.children[0].value
    fetch(`https://projects.propublica.org/nonprofits/api/v2`)
    .then(resp => resp.json())
    .then(data => {
        console.log(data);
        // let image = data.sprites.front_default
        // let imgDiv = document.querySelector('.img-div')
        // imgDiv.innerHTML = `<img src="${image}" alt="pokemon image">`
        // pokeForm.reset()
    })
    .catch(err => console.log(err))
})