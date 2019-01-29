class cDijkstra{
  
  cPoint start;
  cPoint end;
  
  PImage searchMap;
  
  int [] distances;
  int [] previous;
  boolean [] visited;  
  int iDisplayFactor;  
  boolean bFinished;
  
  String mapName = "map2.bmp";
  
  //-------------------
  // Constructor
  //-------------------
  cDijkstra(cPoint _start, cPoint _end){
    println("constructor");
    
    this.start = _start;
    this.end = _end;
    
    iDisplayFactor = 10;
    
    reset();
  } 

  //-------------------
  // Reset
  //-------------------  
  void reset(){
    
    /*
    searchMap = createImage(width/iDisplayFactor, height/iDisplayFactor, RGB);    
    searchMap.loadPixels();
    for (int i = 10; i < 30; i++) {
      for (int j = 10; j < 30; j++) {
        color c = color(255,255,255);
        searchMap.pixels[i*j] = c;
      }
    }
    searchMap.updatePixels();
    */
    
    searchMap = loadImage(mapName);    
    init();
  }  
  
  //-------------------
  // Initialize
  //-------------------  
  void init(){
    /*
     2      for each vertex v in Graph:                                // Initializations
     3          dist[v] := infinity ;                                  // Unknown distance function from 
     4                                                                 // source to v
     5          previous[v] := undefined ;                             // Previous node in optimal path
     6      end for                                                    // from source
     7      
     8      dist[source] := 0 ;                                        // Distance from source to source
     9      Q := the set of all nodes in Graph ;                       // All nodes in the graph are   
    */ 
    
    distances = new int [searchMap.pixels.length];  
    previous  = new int [searchMap.pixels.length];  
    visited   = new boolean [searchMap.pixels.length];  
    
    for (int i = 0; i < searchMap.pixels.length; i++) {
      distances[i] = 1000000;  //we mean here infinity
      previous[i] = -1;        //means undefined
    }    
   
    for (int i = 0; i < visited.length; i++){
      visited[i] = false;
    } 
        
    //Set start point distance to 0
    distances[pointToPixelArrayPosition(this.start)] = 0;    
    
    bFinished = false;
  }
  
  //-------------------
  // Convert cPoint::p into position in array
  //-------------------  
  int pointToPixelArrayPosition(cPoint p){
    int i = 0;
    i = ( (p.y) * searchMap.width ) + p.x;
    return i;
  }
    
  //-------------------
  // Convert position in array to cPoint
  //-------------------  
  cPoint pixelArrayPositionToPoint(int i){
    cPoint p = new cPoint(0,0);
    p.y = i/searchMap.width;
    p.x = i%searchMap.width; //reminder
    return p;
  }  
    
  //-------------------
  // Calculate the index of the point with the smallest distance
  //-------------------  
  int smallestDist(){
    int distance = 1000000;
    int j = -1;
    searchMap.loadPixels();
    for (int i = 0; i < searchMap.pixels.length; i++) {
      
      if (visited[i]){
        continue; //not in Q
      }
      
      if (distances[i] < distance){ 
        j = i;
        distance = distances[i];
      } 
    }  
    searchMap.updatePixels();
    return j;
  }
  
  //-------------------
  // Draw
  //-------------------  
  void draw(){
     update();
        
     //Display method with factor
     stroke(0);
     searchMap.loadPixels();
     for (int i = 0; i < searchMap.pixels.length; i++) {
       fill(searchMap.pixels[i]);
       cPoint p = pixelArrayPositionToPoint(i);
       rect(p.x*iDisplayFactor, p.y*iDisplayFactor, iDisplayFactor, iDisplayFactor);
     }
     
     //Display Start and End point
     fill(100);
     rect(start.x*iDisplayFactor, start.y*iDisplayFactor, iDisplayFactor, iDisplayFactor);
     rect(end.x*iDisplayFactor, end.y*iDisplayFactor, iDisplayFactor, iDisplayFactor);     
     
     searchMap.updatePixels();      
  }
  
  //-------------------
  // Draw obstacle
  //-------------------  
  void drawObstacleRect(int i){
    cPoint p = pixelArrayPositionToPoint(i);
    fill(0,255,0);
    rect(p.x*iDisplayFactor, p.y*iDisplayFactor, iDisplayFactor, iDisplayFactor);
  }
  
  void examine(int u, int v){
    if (checkUV(u,v) == false) return;
    
    int alt = 0;
    
    if (visited[v] == false){
      alt = distances[u] + dist_between(u, v);
      if (alt < distances[v]){
        distances[v] = alt;
        previous[v] = u;
      }
    }    
  }
  
  void update(){
    if (bFinished) return;
    
    int u = smallestDist();    
    int v;

    if (u == -1) println("Smallest distance error");
    
    if (u == pointToPixelArrayPosition(this.end)){ 
      println ("Finished");
      
      bFinished = true;
      
      println("previous[u] "+previous[u]);
      
      int path = previous[u];
      
      while (path != -1){
        searchMap.loadPixels();
        searchMap.pixels[path] = color(255, 0, 0); 
        searchMap.updatePixels();  

        path = previous[path];      
      }
      
      return;
    }
    if (distances[u] == 1000000){  
      println("all remaining vertices are inaccessible"); 
      bFinished = true;    
      return;  //all remaining vertices are inaccessible
    }
    
    //Mark that the point has been visited
    visited[u] = true;
    searchMap.loadPixels();
    searchMap.pixels[u] = color(0, 0, 255); 
    searchMap.updatePixels();    
   
    //Examine each 4 neighbor
    //Left
    v = u-1;
    examine(u, v);
    
    //Right
    v = u+1;
    examine(u, v);    
    
    //Top
    v = u-(width/iDisplayFactor);
    examine(u, v);  
    
    //Bottom
    v = u+(width/iDisplayFactor);
    examine(u, v);       
  }
  
  boolean checkUV(int u, int v){
    boolean ret = true;
    
    if (v < 0) ret = false;
    if (v >= ( (width/iDisplayFactor)*(height/iDisplayFactor) )) ret = false;
    
    //u is left most
    if ( ((u % (width/iDisplayFactor)) == 0) && (v == (u-1)) ) ret = false;
    
    //u is right most
    if ( (( (u+1) % (width/iDisplayFactor)) == 0) && (v == (u+1)) ) ret = false;
    
    return ret; 
  }
  
  int dist_between(int u, int v){

    searchMap.loadPixels();  
    color c = color(0,0,0);
    try{ 
      c = searchMap.pixels[v]; 
    }
    catch (ArrayIndexOutOfBoundsException e){
      println("ArrayIndexOutOfBoundsException u = " + u + " v = " + v);
    }       
    int ret = 0;    
    
    ret = 766 - ((int)red(c) + (int)green(c) + (int)blue(c));
   
    searchMap.updatePixels();
    return ret;
  }
}
