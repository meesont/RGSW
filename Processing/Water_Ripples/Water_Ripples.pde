int cols, rows;
float[] [] current;
float[] [] previous;

float dampening = 0.99;

void setup() {
  size(600, 400);
  cols = width;
  rows = height;
  current = new float[cols] [rows];
  previous = new float[cols] [rows];
}
