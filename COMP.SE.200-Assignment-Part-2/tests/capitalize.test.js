import capitalize from '../src/capitalize';

describe('capitalize', () => {
  test('should capitalize the first character and lowercase the rest', () => {
    expect(capitalize('FRED')).toBe('Fred');
  });

  test('should handle empty strings', () => {
    expect(capitalize('')).toBe('');
  });

  test('should handle strings with special characters', () => {
    expect(capitalize('école')).toBe('École');
  });

  test('should handle non-string inputs', () => {
    expect(capitalize(null)).toBe('Null');
    expect(capitalize(undefined)).toBe('Undefined');
  });
});
