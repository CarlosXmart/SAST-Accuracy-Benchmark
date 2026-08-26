import javax.xml.parsers.*; import java.io.*;
class JavaTp005 {
  static Object parse(InputStream in) throws Exception {
    // XG-BENCH:JAVA-TP-005 START
    DocumentBuilderFactory f = DocumentBuilderFactory.newInstance();
    return f.newDocumentBuilder().parse(in);
    // XG-BENCH:JAVA-TP-005 END
  }
}
