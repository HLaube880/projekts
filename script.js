//Vienkārš kalkulators

// Funkcija, kas veic aprēķinus atkarībā no izvēlētās darbības (+, -, *, /)
function calculate(operator) {
  const vards = document.getElementById("vards").value; // Iegūst vārdu
  const num1 = Number(document.getElementById("num1").value); // Iegūst pirmo skaitli
  const num2 = Number(document.getElementById("num2").value); // Iegūst otro skaitli

  // Pārbaudām, vai lietotājs ir ievadījis vārdu
  if (!vards) {
    alert("Lūdzu, ievadiet savu vārdu!");
    return; // Ja nav ievadīts vārds, pārtraucam funkciju un neturpina aprēķinus
  }

  // Pārbaude, vai vārds sākas ar lielo burtu un vai tas nesatur ciparus vai simbolus
  const vardsRegex = /^[A-ZĀČĒĢĪĶĻŃŠŪŽ][a-zāčēģīķļņšūž]*$/; // Lielais burts sākumā, tikai mazie burti pārējā vārdā
  if (!vardsRegex.test(vards)) {
    alert("Vārds ir jābūt ar lielo burtu un tam nedrīkst būt cipari vai simboli.");
    return; // Ja vārds neatbilst kritērijiem, pārtraucam funkciju
  }

  let rezultats;

  // Aprēķinu veikšana atkarībā no darbības
  switch (operator) {
    case '+':
      rezultats = num1 + num2;
      break;
    case '-':
      rezultats = num1 - num2;
      break;
    case '*':
      rezultats = num1 * num2;
      break;
    case '/':
      // Pārbaudām dalījumu ar nulli
      rezultats = num2 !== 0 ? (num1 / num2) : "Dalīt ar 0 nevar!";
      break;
    default:
      rezultats = "Nepareiza darbība";
  }

  // Rezultāta teksta sagatavošana
  const rezultataTeksts = `${vards}, tavs rezultāts ir: ${rezultats}`;

  // Rezultāts tiek parādīts ekrānā
  document.getElementById("result").innerText = rezultataTeksts;
}

// Funkcija, kas notīra visus ievades laukus un rezultātu
function notirit1() {
  document.getElementById("vards").value = ""; // Notīra vārdu
  document.getElementById("num1").value = ""; // Notīra pirmo skaitli
  document.getElementById("num2").value = ""; // Notīra otro skaitli
  document.getElementById("result").innerText = ""; // Notīra rezultātu
}

















 //function aprekinat() {
 // let x = Number(document.getElementById("x").value);
//let y = Number(document.getElementById("y").value);
  //let z = x + y;

  //console.log("Pirmā vērtība: " + x);
 // console.log("Otrā vērtība: " + y);
  //console.log("Abus saskaitot, rezultāts ir: " + z);

  // Ieliekam rezultātu ekrānā
  //document.getElementById("rezultats").innerText = "Rezultāts: " + z;

//alert("rezultāts ir " + z);
//}







//Figūru pogas

function taisnsturis(){
  const canvas = document.getElementById("zimejums");
  const ctx = canvas.getContext("2d");
  ctx.fillStyle = "blue";
  ctx.fillRect(75, 100, 150, 100);
  ctx.strokeStyle = "red";
  ctx.strokeRect(75, 100, 150, 100); 
} 

function aplis() {
  const canvas = document.getElementById("zimejums");
  const ctx = canvas.getContext("2d"); 
  ctx.beginPath();
  ctx.arc(125, 300, 50, 0, 2 * Math.PI);
  ctx.fillStyle = "green";
  ctx.fill(); 
  ctx.strokeStyle = "black"; 
  ctx.stroke();
}  

function teksts() {
  const canvas = document.getElementById("zimejums");
  const ctx = canvas.getContext("2d");
  ctx.font = "30px Arial";
  ctx.fillText("Čau pasaule", 300, 125);  
}  

function linijas() {
  const canvas = document.getElementById("zimejums");
  const ctx = canvas.getContext("2d");
  ctx.strokeStyle = "green";
  ctx.lineWidth = 5;      //līnijas platums
  ctx.beginPath();       //sākt ceļu
  ctx.moveTo(500, 400); // labais apakšējais stūris
  ctx.lineTo(300, 200); // augšup pa kreisi
  ctx.stroke();

  ctx.beginPath();
  ctx.strokeStyle = "purple";
  ctx.moveTo(250, 400); // kreisā mala šajā zonā
  ctx.lineTo(450, 200); // augšup pa labi
  ctx.stroke();
}

function notirit2() {
  const canvas = document.getElementById("zimejums");
  const ctx = canvas.getContext("2d");
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}
