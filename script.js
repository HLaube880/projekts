



//Figūru pogas

function taisnsturis(){
  const canvas = document.getElementById("zimejums");
  const ctx = canvas.getContext("2d");
  ctx.fillStyle = "blue";
  ctx.fillRect(40, 20, 150, 100);
  ctx.strokeStyle = "red";
  ctx.strokeRect(40, 20, 150, 100); 
} 

function aplis() {
  const canvas = document.getElementById("zimejums");
  const ctx = canvas.getContext("2d"); 
  ctx.beginPath();
  ctx.arc(100, 200, 50, 0, 2 * Math.PI);
  ctx.fillStyle = "green";
  ctx.fill(); 
  ctx.strokeStyle = "black"; 
  ctx.stroke();
}  

function teksts() {
  const canvas = document.getElementById("zimejums");
  const ctx = canvas.getContext("2d");
  ctx.font = "30px Arial";
  ctx.fillText("Čau pasaule", 300, 50);  
}  

function linijas() {
  const canvas = document.getElementById("zimejums");
  const ctx = canvas.getContext("2d");
  ctx.strokeStyle = "green";
  ctx.lineWidth = 5;      //līnijas platums
  ctx.beginPath();       //sākt ceļu
  ctx.moveTo(400, 200); //atrašanās vieta
  ctx.lineTo(200, 20); //līnijas parametri
  ctx.stroke();

  ctx.beginPath();
  ctx.strokeStyle = "purple";
  ctx.moveTo(400, 200);
  ctx.lineTo(150, 150);
  ctx.stroke();
}

function notirit() {
  const canvas = document.getElementById("zimejums");
  const ctx = canvas.getContext("2d");
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}
