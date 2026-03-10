//DISCLAIMER: 90% OF THIS IS WRITTEN WITH THE HELP OF DUCK DEBUGGER & THE IDEA IS TO BUILD UP NEW VOCABULARY WHILE DOING SO

var now = new Date();
var hour = now.getHours();
const morn_greetings = ['Good Morning', 'Guten Morgen', 'Bonjour', 'おはよう', 'Buen Día', 'Buongiorno'];
const noon_greetings = ['Good Afternoon', 'Guten Tag', 'Bon Après-Midi', 'こんにちは', 'Buenas Tardes', 'Buon pomeriggio'];
const even_greetings = ['Good Evening', 'Guten Abend', 'Bonne Soirée', 'こんばんは', 'Buenas Noches', 'Buonasera'];
var vary = 0;

// Update the greeting every 5 seconds
function time_sensitive_greeting() {
    var greetingElement = document.getElementById('time-sensitive-greeting');
    if (hour < 12) {
        greetingElement.style.opacity = 0;
        setTimeout(function() {
            greetingElement.innerHTML = morn_greetings[vary];
            greetingElement.style.opacity = 1;
            vary = (vary + 1) % morn_greetings.length;
        }, 500);
    } else if (hour < 18) {
        greetingElement.style.opacity = 0;
        setTimeout(function() {
            greetingElement.innerHTML = noon_greetings[vary];
            greetingElement.style.opacity = 1;
            vary = (vary + 1) % noon_greetings.length;
        }, 500);
    } else {
        greetingElement.style.opacity = 0;
        setTimeout(function() {
            greetingElement.innerHTML = even_greetings[vary];
            greetingElement.style.opacity = 1;
            vary = (vary + 1) % even_greetings.length;
        }, 500, );
    }
}

time_sensitive_greeting();
setInterval(time_sensitive_greeting, 3000);
