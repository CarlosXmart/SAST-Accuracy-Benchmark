class JavaTn009 {
  static String documentationFixture() {
    // XG-BENCH:JAVA-TN-009 START
    String fakeJwtFixture = "header.payload.invalid-signature";
    return "fixture:" + fakeJwtFixture;
    // XG-BENCH:JAVA-TN-009 END
  }
}
