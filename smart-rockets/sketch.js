let lifespan = 300;

let target;
let obstacles = []
let population;
pressed = false
let x,y,x1,y1
function setup() {
  createCanvas(800, 400);
  target = createVector(width, height/2)
  obstacles.push(new Obstacle(100, 200, 10,100))
  population = new Population()

}

function draw() {
  background(0);
  fill(255)
  circle(target.x, target.y, 20)
  for(let obstacle of obstacles){
    obstacle.display()
  }

  population.run()
  if(mouseIsPressed){
    x1 = mouseX
    y1 = mouseY

    width_obj = abs(x - x1)
    height_obj = abs(y - y1)
    fill(255)
    rect(x, y, width_obj, height_obj)
  }
  
}

function mousePressed(){
  
  x = mouseX
  y = mouseY
  
}

function mouseReleased(){
  
  width_obj = abs(x - x1)
  height_obj = abs(y - y1)
  obstacles.push(new Obstacle(x, y, width_obj,height_obj))
}
