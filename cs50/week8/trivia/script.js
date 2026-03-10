document.getElementById('right').addEventListener('click', function() {
    document.getElementById('para_1').innerHTML = 'Correct';
    this.style.backgroundColor = 'Green';

    //Reset color of the other buttons
    document.querySelectorAll('.wrong').style.backgroundColor = '#aab0b6';
})

document.querySelectorAll('.wrong').forEach(function(element) {
    element.addEventListener('click', function(){
        document.getElementById('para_1').innerHTML = 'Incorrect';
        element.style.backgroundColor = 'Red';

        //Reset color of the other buttons
        document.querySelectorAll('.wrong').forEach(function(otherElement) {
            if (otherElement !== element) {
                otherElement.style.backgroundColor = '#aab0b6';
                document.getElementById('right').style.backgroundColor = '#aab0b6';
            }
        })
    })
})

document.getElementById('myForm').addEventListener('submit', function(event){
    let namelist = ['ben', 'ben geller'];
    if (namelist.includes(document.getElementById('name').value.toLowerCase())) {
        document.getElementById('para_2').innerHTML = 'Correct';
        document.getElementById('name').style.backgroundColor = 'Green';
        document.getElementById('name').style.color = 'White';
    }
    else {
        document.getElementById('para_2').innerHTML = 'Incorrect';
        document.getElementById('name').style.backgroundColor = 'Red';
    }
    event.preventDefault();
})
