class Obstacle{
    constructor(x,y,w,h){
        this.position = createVector(x, y)
        this.size = createVector(w, h)
    }

    display(){
        fill(255)
        rect(this.position.x, this.position.y, this.size.x, this.size.y)
    }
}