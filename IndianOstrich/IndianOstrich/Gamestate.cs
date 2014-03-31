using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;
using System.Globalization;
using SdlDotNet.Core;
using SdlDotNet.Input;

namespace IndianOstrich
{
    class Gamestate
    {
        Hashtable state;
        Screens[] screens;
        BasePlayer player1();
        BasePlayer player2();

        public void Start()
        {
        }

        public void End()
        {
        }

        public void Update(KeyboardEventArgs e)
        {
        }

        //overload update for mouseargs
        public void Update(KeyboardEventArgs e)
        {
        }
    }
}
