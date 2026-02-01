import reduce from '../src/reduce';

describe('reduce', () => {
  test('should reduce an array to a single value', () => {
    const sum = reduce([1, 2, 3], (acc, val) => acc + val, 0);
    expect(sum).toBe(6);
  });

  test('should handle strings', () => {
    const concatenated = reduce(['a', 'b', 'c'], (acc, val) => acc + val, '');
    expect(concatenated).toBe('abc');
  });

  test('should reduce an object', () => {
    const obj = { a: 1, b: 2, c: 3 };
    const sum = reduce(obj, (acc, val) => acc + val, 0);
    expect(sum).toBe(6);
  });

  test('should use first element as accumulator if not provided', () => {
    const sum = reduce([1, 2, 3], (acc, val) => acc + val);
    expect(sum).toBe(6);
  });
});
