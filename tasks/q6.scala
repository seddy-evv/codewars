// The main idea is to count all the occurring characters in a string. If you have a string like aba,
// then the result should be {'a': 2, 'b': 1}.

// What if the string is empty? Then the result should be empty object literal, {}.

import scala.collection.mutable.Map

object Kata {
  def count(string: String): Map[Char,Int] = {

    var map = Map.empty[Char,Int]
    for (c <- string)  {
      map.update(c, map.getOrElse(c, 0) + 1)
    }
    map
  }
}