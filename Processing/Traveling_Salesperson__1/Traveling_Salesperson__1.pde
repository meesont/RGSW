PVector[] cities;
int totalCities = 4;

float recordDistance;
PVector[] bestEver;

void setup() {
  size(400, 300);
  cities = new PVector[totalCities];
  bestEver = new PVector[totalCities];
  for(int i = 0; i<totalCities;i++){ 
    PVector v = new PVector(random(width), random(height));
    cities[i] = v;
  }
  
  float d = calcDistance(cities);
  recordDistance = d;
  arrayCopy(cities, bestEver);
}

void draw() {
  background(0);
  fill(255);
  for(int i=0;i<cities.length;i++){
    ellipse(cities[i].x, cities[i].y, 8, 8);
  }
  
  stroke(255);
  strokeWeight(1);
  noFill();
  beginShape();
  for(int i=0;i<cities.length;i++){
    vertex(cities[i].x, cities[i].y);
  }
  endShape();
  
  int i = floor(random(cities.length));
  int j = floor(random(cities.length));
  swap(cities, i, j);
  
  float d = calcDistance(cities);
  if (d < recordDistance) {
    recordDistance = d;
    arrayCopy(cities, bestEver);
  }
}

void swap(PVector[] a, int i, int j){
  PVector temp = a[i];
  a[i] = a[j];
  a[j] = temp;
}

float calcDistance(PVector[] points){
  float sum = 0;
  for(int i=0;i<points.length - 1; i++){
    float d = dist(points[i].x, points[i].y, points[i + 1].x, points[i + 1].y);
    sum += d;
  }
  
  return sum;
}
