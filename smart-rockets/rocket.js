class Rocket{
    constructor(dna){
        if(dna == undefined){
            this.genes = []
            
            for (let index = 0; index < lifespan; index++) {
                this.genes.push(p5.Vector.random2D())
                
            }
        }else{
            this.genes = dna
        }
        this.position = createVector(10, height/2)
        this.velocity = createVector()
        this.acc = createVector()
        this.r = 2
        this.maxspeed = 6
        this.maxforce = 1
        this.heath = 0
        this.run = true

    }

    applyForce(force){
        force.limit(this.maxforce)
        this.acc.add(force)
        
    }

    completed(){
        let d = p5.Vector.dist(this.position, target)
        if(d < 10){
            this.run = undefined
        }
    }

    update(){
        if(this.run){
            this.applyForce(this.genes[this.heath])
            this.velocity.add(this.acc)
            this.velocity.limit(this.maxspeed)
            this.position.add(this.velocity)
            this.acc.mult(0)
            this.heath += 1
        }
    }

    checkcollision(objs){
        for(let obj of objs){
            this.collision(obj)
        }

    }

    collision(obj){
        let dx = this.position.x-obj.position.x
        let dy = this.position.y- obj.position.y
        
        //console.log(dx,dy)
        if(dx > this.r && dx < obj.size.x){
            if(dy > this.r && dy < obj.size.y){
                this.run = false
            }
        }
        

    }

    dead(){
        return this.heath >= lifespan 
    }

    display(){
    
        this.theta = this.velocity.heading() + PI/2;
        let rd = color(0,255,0)
        let gr = color(255,0,0)
        let cor = lerpColor(rd, gr, this.heath/400)
        fill(cor);
        noStroke();
        push();
        translate(this.position.x, this.position.y);
        rotate(this.theta);
        beginShape();
        vertex(0, -this.r*2);
        vertex(-this.r, this.r*2);
        vertex(this.r, this.r*2); 
        endShape(CLOSE);
        pop();
    
    }

    boundaries(){
        let d = 1
        if ((this.position.x < d) || (this.position.x > width - d) || (this.position.y < d) || (this.position.y > height - d)){
            this.run = false
        }
            
    }
}