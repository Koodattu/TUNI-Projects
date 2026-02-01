import isArrayLike from '../src/isArrayLike';

describe('isArrayLike', () => {
  test('should return true for arrays', () => {
    expect(isArrayLike([1, 2, 3])).toBe(true);
  });

  test('should return true for strings', () => {
    expect(isArrayLike('abc')).toBe(true);
  });

  test('should return false for functions', () => {
    expect(isArrayLike(function() {})).toBe(false);
  });

  test('should return false for null or undefined', () => {
    expect(isArrayLike(null)).toBe(false);
    expect(isArrayLike(undefined)).toBe(false);
  });

  test('should return false for non-array-like objects', () => {
    expect(isArrayLike({})).toBe(false);
  });
});
