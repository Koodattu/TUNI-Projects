import endsWith from "../src/endsWith";

describe("endsWith", () => {
  test("should return true if string ends with target", () => {
    expect(endsWith("abc", "c")).toBe(true);
  });

  test("should return false if string does not end with target", () => {
    expect(endsWith("abc", "b")).toBe(false);
  });

  test("should respect the position argument", () => {
    expect(endsWith("abc", "b", 2)).toBe(true);
  });

  test("should return false for negative position", () => {
    expect(endsWith("abc", "a", -1)).toBe(false);
  });

  test("should return false when target is longer than string", () => {
    expect(endsWith("abc", "abcd")).toBe(false);
  });

  test("should return true if target is an empty string", () => {
    expect(endsWith("abc", "")).toBe(true);
  });

  test("should return true if string is empty and target is also empty", () => {
    expect(endsWith("", "")).toBe(true);
  });

  test("should return false if string is empty and target is not empty", () => {
    expect(endsWith("", "a")).toBe(false);
  });

  test("should return true if position is greater than string length", () => {
    expect(endsWith("abc", "b", 10)).toBe(true);
  });

  test("should handle NaN for position argument gracefully", () => {
    expect(endsWith("abc", "b", NaN)).toBe(false);
  });
});
