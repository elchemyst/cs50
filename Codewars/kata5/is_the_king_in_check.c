#include <stdbool.h>



bool king_is_in_check (const char chessboard[8][8])
{
    for (int i = 0; i < 8; i++)
    {
      for (int j = 0; j < 8; j++)
      {
        //check for threats from pawns
        if (chessboard[i][j] == 80)
        {
          if (chessboard[i + 1][j - 1] == 75 ||
          chessboard[i + 1][j + 1])
          {
            return true;
          }
        }

        //check for threats from queen
        if (chessboard[i][j] == 81)
        {
          int r = 0;
        }
      }
    }
    return false;  // good luck :)
}
