#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    if (typeof size !== 'number' || size <= 0 || !Number.isInteger(size)) {
      throw new Error('Invalid size. Size must be a positive integer.');
    }
    super(size, size);
  }
}

module.exports = Square;
