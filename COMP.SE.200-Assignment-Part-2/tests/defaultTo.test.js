import defaultTo from '../src/defaultTo';

describe('defaultTo', () => {
  test('should return the value if it is not null or undefined', () => {
    expect(defaultTo(1, 10)).toBe(1);
  });

  test('should return defaultValue if value is null', () => {
    expect(defaultTo(null, 10)).toBe(10);
  });

  test('should return defaultValue if value is undefined', () => {
    expect(defaultTo(undefined, 10)).toBe(10);
  });

  test('should return defaultValue if value is NaN', () => {
    expect(defaultTo(NaN, 10)).toBe(10);
  });
});
