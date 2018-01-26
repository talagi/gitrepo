function setup() {
  // put setup code here
  createCanvas(700, 600);
}

function draw() {
  // put drawing code here
  fill('#279112');
    strokeWeight(10);
      stroke('blue');
        ellipse(100, 200, 30, 80);
strokeWeight(20);
  stroke('pink');
    fill('#f205ff');
      ellipse(40, 100, 80, 30);
strokeWeight(5);
  stroke('black');
    fill('black');
      line(10, 10, 60, 60);
      line(60, 10, 10, 60);

stroke('green');
  fill('green');
    point(100, 100);

rect(200, 200, 300, 100, 10);
}
