import eq from '../src/eq';

describe('eq', () => {
  test('should return true for identical primitives', () => {
    expect(eq('a', 'a')).toBe(true);
    expect(eq(1, 1)).toBe(true);
  });

  test('should return false for different primitives', () => {
    expect(eq('a', 'b')).toBe(false);
    expect(eq(1, 2)).toBe(false);
  });

  test('should return true for NaN comparisons', () => {
    expect(eq(NaN, NaN)).toBe(true);
  });

  test('should return true for identical objects', () => {
    const obj = { a: 1 };
    expect(eq(obj, obj)).toBe(true);
  });

  test('should return false for different objects with same properties', () => {
    expect(eq({ a: 1 }, { a: 1 })).toBe(false);
  });
});
