#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends class Rectangle{
  constructor (size){
    super(size, size);
  }
}
module.exports = Square;
