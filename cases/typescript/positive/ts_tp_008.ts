interface Jwt { verify(token: string, key: string, options: { algorithms: string[] }): unknown }
export function verify(jwt: Jwt, token: string, key: string): unknown {
  // XG-BENCH:TS-TP-008 START
  return jwt.verify(token, key, { algorithms: ['none'] });
  // XG-BENCH:TS-TP-008 END
}
