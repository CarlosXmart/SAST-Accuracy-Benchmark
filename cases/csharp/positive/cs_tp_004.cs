using System.IO; using System.Runtime.Serialization.Formatters.Binary;
class CsTp004 {
  public static object Load(Stream input) {
    // XG-BENCH:CS-TP-004 START
#pragma warning disable SYSLIB0011
    return new BinaryFormatter().Deserialize(input);
#pragma warning restore SYSLIB0011
    // XG-BENCH:CS-TP-004 END
  }
}
