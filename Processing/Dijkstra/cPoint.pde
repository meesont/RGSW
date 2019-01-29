class cPoint{
  int x;
  int y;
  
  cPoint(){
    this.x = 0;
    this.y = 0;
  } 
  
  cPoint(int _x, int _y){
    this.x = _x;
    this.y = _y; 
  }
  
  String toString(){
    return this.x + ":" + this.y; 
  }
}
