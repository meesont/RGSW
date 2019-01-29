cDijkstra solver;

PFont myFont;

void setup() {
  size(400, 400);
  background(255);
  //frameRate(10);
  stroke(255);
  fill(102);
  
  solver = new cDijkstra(new cPoint(0,0), new cPoint(39,33));
  
  //Texts
  // Uncomment the following two lines to see the available fonts 
  //String[] fontList = PFont.list();
  //println(fontList);
  myFont = createFont("Georgia", 32);
  textFont(myFont);
  textAlign(CENTER, CENTER);  
}


void draw() {
  background(100); 
  solver.draw(); 
  
  fill(200,100,100);
  rect(300,350,100,50);
  fill(255);
  text("Reset", 350, 375);  
  
  if (mousePressed) {
    if (mouseX > 300 && mouseY > 350){
      solver.reset();
    } 
  }
}


