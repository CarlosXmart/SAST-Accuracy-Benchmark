import javax.xml.parsers.*; import java.io.*;
class JavaTn005 {
  static Object parse(InputStream in) throws Exception {
    // XG-BENCH:JAVA-TN-005 START
    DocumentBuilderFactory f = DocumentBuilderFactory.newInstance();
    f.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
    f.setFeature("http://xml.org/sax/features/external-general-entities", false);
    f.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
    f.setXIncludeAware(false);
    f.setExpandEntityReferences(false);
    return f.newDocumentBuilder().parse(in);
    // XG-BENCH:JAVA-TN-005 END
  }
}
