using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IndianOstrich
{
    class BasePlayer
    {
        private int x, y;
        private int xVel, yVel;

        public BasePlayer(bool isPlayerOne)
        {
            if(isPlayerOne)
            {
                x = 0;
                y = 0;
            }
            else
            {
                x = 50;
                y = 50;
            }

            xVel = 0;
            yVel = 0;

        }

        public void Move(bool isLeft)
        {
            if(isLeft)
            {
                xVel -= 1;
            }
            else
            {
                xVel += 1;
            }
        }

        public void Kick()
        {

        }

        public void Punch()
        {

        }

        public void Jump()
        {
            yVel -= 1;
        }

    }
}
