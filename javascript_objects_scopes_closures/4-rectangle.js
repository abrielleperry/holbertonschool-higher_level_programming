#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      Object.assign(this, {});
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  rotate() {
    let rotate = this.width;
    this.width = this.height;
    this.height = rotate;
      }
  }
  double() {
    this.width = 
    this.height = 
}
module.exports = Rectangle;
