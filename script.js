



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

function notirit() {
  const canvas = document.getElementById("zimejums");
  const ctx = canvas.getContext("2d");
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}
