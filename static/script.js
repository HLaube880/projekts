
window.onload = function(){
  var navLinks = document.querySelectorAll('.topnav a');
  console.log(navLinks);

  navLinks.forEach(function(link){
    link.addEventListener('click', function(event){
      // Noņem 'active' klasi no visiem linkiem
      navLinks.forEach(function(l){
        l.classList.remove('active');
      });

      // Pievieno 'active' klikšķētajam linkam
      this.classList.add('active');
    });
  });
}





// Atjauno saturu iframe elementā
function atjaunotIetvaru(which) {
document.getElementById('lapas_saturs').innerHTML = '<'+'object id="lapas" name="lapas" type="text/html" data=" '+which.href+'"><\/object>';
}


// Kalkulators
function calculate(operator) {
  const vards = document.getElementById("vards").value;
  const num1 = Number(document.getElementById("num1").value);
  const num2 = Number(document.getElementById("num2").value);

  if (!vards) {
    alert("Lūdzu, ievadiet savu vārdu!");
    return;
  }

  const vardsRegex = /^[A-ZĀČĒĢĪĶĻŅŠŪŽ][a-zāčēģīķļņšūž]*$/; //JS REGexp
  if (!vardsRegex.test(vards)) {
    alert("Vārdam jāsākas ar lielo burtu un nedrīkst saturēt ciparus vai simbolus.");
    return;
  }

  let rezultats;
  switch (operator) {
    case "+": rezultats = num1 + num2; break;
    case "-": rezultats = num1 - num2; break;
    case "*": rezultats = num1 * num2; break;
    case "/": rezultats = num2 !== 0 ? num1 / num2 : "Dalīt ar 0 nevar!"; break;
    default: rezultats = "Nepareiza darbība";
  }

  document.getElementById("result").innerText = `${vards}, tavs rezultāts ir: ${rezultats}`;
}

// Notīra kalkulatoru
function notirit1() {
  document.getElementById("vards").value = "";
  document.getElementById("num1").value = "";
  document.getElementById("num2").value = "";
  document.getElementById("result").innerText = "";
}

// Zīmēšana kanvā
function taisnsturis() {
  const ctx = document.getElementById("zimejums").getContext("2d");
  ctx.fillStyle = "blue";
  ctx.fillRect(75, 100, 150, 100);
  ctx.strokeStyle = "red";
  ctx.strokeRect(75, 100, 150, 100);
}

function aplis() {
  const ctx = document.getElementById("zimejums").getContext("2d");
  ctx.beginPath();
  ctx.arc(125, 300, 50, 0, 2 * Math.PI);
  ctx.fillStyle = "green";
  ctx.fill();
  ctx.strokeStyle = "black";
  ctx.stroke();
}

function teksts() {
  const ctx = document.getElementById("zimejums").getContext("2d");
  ctx.font = "30px Arial";
  ctx.fillText("Čau pasaule", 300, 125);
}

function linijas() {
  const ctx = document.getElementById("zimejums").getContext("2d");
  ctx.strokeStyle = "green";
  ctx.lineWidth = 5;
  ctx.beginPath();
  ctx.moveTo(500, 400);
  ctx.lineTo(300, 200);
  ctx.stroke();

  ctx.beginPath();
  ctx.strokeStyle = "purple";
  ctx.moveTo(250, 400);
  ctx.lineTo(450, 200);
  ctx.stroke();
}

function notirit2() {
  const ctx = document.getElementById("zimejums").getContext("2d");
  ctx.clearRect(0, 0, 500, 400);
}
