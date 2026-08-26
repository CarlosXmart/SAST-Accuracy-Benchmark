interface Redirector { void sendRedirect(String v); }
class JavaTp008 {
  static void redirect(Redirector r, String next) {
    // XG-BENCH:JAVA-TP-008 START
    r.sendRedirect(next);
    // XG-BENCH:JAVA-TP-008 END
  }
}
