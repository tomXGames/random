function setup() {
  createCanvas(400, 400);
  angleMode(PI);
  ellipseMode(CENTER);
  textAlign(CENTER, CENTER);
}

function draw() {
  background(220);
  var element = 20;
  translate(width / 2, height / 2);
  fill(232, 201, 20);
  circle(0, 0, 20);
  var counter = 1;
  while (element > 0) {
    noFill();
    circle(0, 0, counter * 50);
    element -= electrons(counter - 1);
    var angles = (2 * PI) / (electrons(counter - 1)+(element>=0?0:element));
    for (var i = 0; i < 2 * PI; i += angles) {
      fill(0,0,255)
      circle(counter * 50 * 0.5 * cos(i), counter * 50 * 0.5 * sin(i), 10);
      fill(255,255,255);
      text("-",counter * 50 * 0.5 * cos(i), counter * 50 * 0.5 * sin(i)-0.5)
    }
    counter++;
  }
}

function electrons(n) {
  if (n == 0) {
    return 2;
  } else {
    return electrons(n - 1) + n * 4 + 2;
  }
}
