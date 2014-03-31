using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;
using System.Drawing.Imaging;


namespace IndianOstrich
{
    class BasePlayer
    {
        //An image placeholder
        private Image img;

        //x and y coordinates
        private int x, y;

        //x and y velocities
        private int xVel, yVel;

        //Constructor
        public BasePlayer(Point spawnPoint)
        {
            x = spawnPoint.X;
            y = spawnPoint.Y;

            xVel = 0;
            yVel = 0;

            img = Image.FromFile("PlayerPlaceholder.png");
        }

        //X movement
        //TODO speeds may need tweaking
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

        //Generic kick
        //TODO need collision manager to finish
        public void Kick()
        {
            
        }

        //Generic punch
        //TODO need collision manager to finish
        public void Punch()
        {
            
        }

        //Y movement
        //TODO needs gravity and
        //speeds may need tweaking
        public void Jump()
        {
            yVel -= 1;   
        }
    }
}
