// Write a function that takes a string of parentheses, and determines if the order of
// the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

// Examples
// "()"              =>  true
// ")(()))"          =>  false
// "("               =>  false
// "(())((()())())"  =>  true
// Constraints
// 0 <= length of input <= 100

// All inputs will be strings, consisting only of characters ( and ).
// Empty strings are considered balanced (and therefore valid), and will be tested.
// For languages with mutable strings, the inputs should not be mutated.

public class Kata {

  public static boolean validParentheses(String parenStr) {
    if (parenStr.length() == 0){
            return true;
        } else {
            int rez = parenStr.length()/2;
            for (int i = 0; i < rez; i++) {
                parenStr = parenStr.replace("()", "");
            }
            if (parenStr.length() == 0){
                return true;
            } else {
                return false;
            }
        }
  }
}