// Usually when you buy something, you're asked whether your credit card number, phone number or
// answer to your most secret question is still correct. However, since someone could look over your shoulder,
// you don't want that shown on your screen. Instead, we mask it.
//
// Your task is to write a function maskify, which changes all but the last four characters into '#'.
//
// Examples
// maskify("4556364607935616") == "############5616"
// maskify(     "64607935616") ==      "#######5616"
// maskify(               "1") ==                "1"
// maskify(                "") ==                 ""
//
//  // "What was the name of your first pet?"
//  maskify("Skippy")                                   == "##ippy"
//  maskify("Nananananananananananananananana Batman!") == "####################################man!"

def maskify(cc: String): String = {

    val str_len = cc.length()
    var new_str = ""
    if (str_len > 4) {
      for (i <-0 until str_len - 4){
        new_str += "#"
      }
      new_str += cc.substring(str_len - 4, str_len)
    } else {
      new_str = cc
    }
    new_str
}
