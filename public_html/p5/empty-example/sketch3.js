
function setup() {
  // put setup code here
  createCanvas(600, 600);
  background(200);
}

function draw() {
  noFill();
  noStroke();
  if (mouseIsPressed) { // naciśnięto klawisz myszki
    if (mouseButton === LEFT) {
      fill('red');
        strokeWeight(10);
          stroke('yellow');
    }
    if (mouseButton === CENTER) {
      strokeWeight(3);
      fill(200);
      stroke(100);
      rect(mouseX-10, mouseY-10,20, 20);
    }
  }
  point(mouseX, mouseY);
  // put drawing code here
  //r = random(255);
  //g = random(255);
  // b = random(255);




}
