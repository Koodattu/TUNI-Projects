import add from '../src/add';

describe('add', () => {
  test('should add two positive numbers', () => {
    expect(add(6, 4)).toBe(10);
  });

  test('should add negative numbers', () => {
    expect(add(-6, -4)).toBe(-10);
  });

  test('should handle adding zero', () => {
    expect(add(6, 0)).toBe(6);
  });

  test('should handle adding floating-point numbers', () => {
    expect(add(1.5, 2.5)).toBe(4);
  });
});
