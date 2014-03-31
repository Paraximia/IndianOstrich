using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;
using System.Globalization;
using System.Drawing;
using SdlDotNet.Core;
using SdlDotNet.Input;

namespace IndianOstrich
{
    class Gamestate
    {
        Hashtable state;
        Screens[] screens;
        BasePlayer player1;
        BasePlayer player2;

        //character strings are which character each player chose
        public Gamestate(string character1, string character2)
        {
            player1 = new BasePlayer(new Point(1,2));
            player2 = new BasePlayer(new Point(1, 2));
        }

        public void End()
        {
        }

        public void Update(KeyboardEventArgs e)
        {
        }

        //overload update for mouseargs
        public void Update(MouseButtonEventArgs e)
        {
        }
    }
}
