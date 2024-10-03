using System;
using System.Collections.Generic; 

class Translator
{
  // Braille to English
  static Dictionary<string, string> brailleToEnglish = new Dictionary<string, string>
  {
    {"O.....", "a"}, {"O.O...", "b"}, {"OO....", "c"}, {"OO.O..", "d"}, {"O..O..", "e"},
    {"OOO...", "f"}, {"OOOO..", "g"}, {"O.OO..", "h"}, {".OO...", "i"}, {".OOO..", "j"},
    {"O...O.", "k"}, {"O.O.O.", "l"}, {"OO..O.", "m"}, {"OO.OO.", "n"}, {"O..OO.", "o"},
    {"OOO.O.", "p"}, {"OOOOO.", "q"}, {"O.OOO.", "r"}, {".OO.O.", "s"}, {".OOOO.", "t"},
    {"O...OO", "u"}, {"O.O.OO", "v"}, {".OOO.O", "w"}, {"OO..OO", "x"}, {"OO.OOO", "y"}, 
    {"O..OOO", "z"}, {".....O", "capital"}, {".OOO..", "number"}, {"......", " "}
    };

    // English to Braille
    static Dictionary<string, string> englishToBraille = new Dictionary<string, string>
    {
      {"a", "O....."}, {"b", "O.O..."}, {"c", "OO...."}, {"d", "OO.O.."}, {"e", "O..O.."},
      {"f", "OOO..."}, {"g", "OOOO.."}, {"h", "O.OO.."}, {"i", ".OO..."}, {"j", ".OOO.."},
      {"k", "O...O."}, {"l", "O.O.O."}, {"m", "OO..O."}, {"n", "OO.OO."}, {"o", "O..OO."},
      {"p", "OOO.O."}, {"q", "OOOOO."}, {"r", "O.OOO."}, {"s", ".OO.O."}, {"t", ".OOOO."},
      {"u", "O...OO"}, {"v", "O.O.OO"}, {"w", ".OOO.O"}, {"x", "OO..OO"}, {"y", "OO.OOO"}, 
      {"z", "O..OOO"}, {" ", "......"}
    };

    static Dictionary<string, string> numbersToBraile = new Dictionary<string, string>
    {
      {"0", ".OOO.."}, {"1", "O....."}, {"2", "O.O..."}, {"3", "OO...."}, {"4", "OO.O.."}, 
      {"5", "O..O.."}, {"6", "OOO..."}, {"7", "OOOO.."}, {"8", "O.OO.."}, {"9", ".OO..."} 
    };



  
}
