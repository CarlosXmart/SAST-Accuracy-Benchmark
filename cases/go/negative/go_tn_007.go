package cases
import "html/template"
func GoTn007(input string) interface{} {
    // XG-BENCH:GO-TN-007 START
    return struct{Value string}{Value: input}
    // XG-BENCH:GO-TN-007 END
}
var _ = template.HTMLEscapeString
