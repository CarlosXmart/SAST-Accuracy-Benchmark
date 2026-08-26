export function fixture(): string {
  // XG-BENCH:TS-TN-008 START
  const fakeToken = 'header.payload.invalid-signature';
  return `fixture:${fakeToken}`;
  // XG-BENCH:TS-TN-008 END
}
