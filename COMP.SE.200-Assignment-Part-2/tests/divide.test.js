import divide from '../src/divide';

describe('divide', () => {
  test('should divide two positive numbers', () => {
    expect(divide(6, 3)).toBe(2);
  });

  test('should divide a negative and a positive number', () => {
    expect(divide(-6, 3)).toBe(-2);
  });

  test('should divide two negative numbers', () => {
    expect(divide(-6, -3)).toBe(2);
  });

  test('should handle division by zero', () => {
    expect(divide(6, 0)).toBe(Infinity);
  });

  test('should handle zero divided by a number', () => {
    expect(divide(0, 6)).toBe(0);
  });
});
