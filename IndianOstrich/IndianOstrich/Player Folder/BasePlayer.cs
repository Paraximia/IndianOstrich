using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;

namespace IndianOstrich
{
    class BasePlayer
    {
        private Image img;
        private int x, y;
        private int xVel, yVel;

        public BasePlayer(Point spawnPoint)
        {
            x = spawnPoint.X;
            y = spawnPoint.Y;

            xVel = 0;
            yVel = 0;

            img = new Image.FromFile("PlayerPlaceholder.png");
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
