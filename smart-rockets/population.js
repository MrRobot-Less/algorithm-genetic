class Population{
    constructor(){
        this.population_size = 200
        this.rockets = []
        for (let index = 0; index < this.population_size; index++) {
            this.rockets.push(new Rocket())
            
        }
    }

    run(){
        let rockets = []
        for(let rocket of this.rockets){
            if(rocket.dead()){
                rockets.push(rocket)
                
                continue
            }
            
            if(rocket.run){
                
                
                rocket.completed()
                rocket.boundaries()
                rocket.checkcollision(obstacles)
                rocket.update();
                  
            }else if(rocket.run == false){
                
                rocket.heath += 200
            }else{
                rocket.heath += 1
            }
            rocket.display();

        }
        if(this.rockets.length == rockets.length){
            console.log("teste")
            this.evolution()
            
        }

    }

    selection(){
        let record = Infinity
        let dad = null;
        let mom = null;
        for(let rocket of this.rockets){
            let d = p5.Vector.dist(rocket.position, target)
            if(d < record){
                mom = dad
                dad = rocket
                record = d

            }
        }
        if(mom == null){
            mom = dad
        }
        return [dad, mom]
        

    }

    reproduction(daddy){
        this.population_size = this.rockets.length
        this.rockets = []
        for (let index = 0; index < this.population_size; index++) {
            let genes = []
            
            
            for (let index = 0; index < lifespan; index++) {
                let i = random(lifespan)

                let dad = random(daddy)
                let mom = random(daddy)    
                if(index > lifespan/2){
                    genes.push(dad.genes[index])
                }else{
                    genes.push(mom.genes[index])
                }

                
            }        
            let gene = this.mutation(genes)
            this.rockets.push(new Rocket(gene))
                
        }
        
    }

    mutation(gene){
        for (let index = 0; index < gene.length; index++) {
            
            if(random(1) < 0.02){
                
                gene[index] = p5.Vector.random2D()
            }
        }
        return gene
    }

    evolution(){
        let obj = this.selection()
        this.reproduction(obj)
        
    }
}