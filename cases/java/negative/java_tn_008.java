interface SafeRedirector { void sendRedirect(String v); }
class JavaTn008 {
  static void redirect(SafeRedirector r, String next) {
    // XG-BENCH:JAVA-TN-008 START
    String target = (next != null && next.startsWith("/app/")) ? next : "/app/home";
    r.sendRedirect(target);
    // XG-BENCH:JAVA-TN-008 END
  }
}
