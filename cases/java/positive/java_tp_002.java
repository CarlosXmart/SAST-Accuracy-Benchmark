class JavaTp002 {
  static Process run(String user) throws Exception {
    // XG-BENCH:JAVA-TP-002 START
    return Runtime.getRuntime().exec("sh -c echo " + user);
    // XG-BENCH:JAVA-TP-002 END
  }
}
