// This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

object Operation {

  def multiply(n: Int): Int = {
    if (n % 2 == 0) {
      n * 8
    } else {
      n * 9
    }
  }
}
