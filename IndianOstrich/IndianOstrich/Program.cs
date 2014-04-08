using System;
using System.Collections.Generic;
using System.Linq;
<<<<<<< HEAD
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing;
using SdlDotNet.Graphics;
using SdlDotNet.Core;
using SdlDotNet.Graphics.Primitives;


namespace IndianOstrich
{
    public class IndianOstrich
    {
        private const int swidth = 1280;
        private const int sheight = 800;
        private static Surface screen;
        private static Random r = new Random();
        public static void Main(string[] args)
        {
            screen = Video.SetVideoMode(swidth, sheight, 32, false, false, false, true);
            Events.TargetFps = 50;
            Events.Quit += (QuitEventHandler);
            Events.Tick += (TickEventHandler);
            Events.Run();
            Events.Run();
        }

        private static void QuitEventHandler(object sender, QuitEventArgs args)
        {
            Events.QuitApplication();
        }

        private static void TickEventHandler(object sender, TickEventArgs args)
        {
            var color = Color.FromArgb(r.Next(255), r.Next(255), r.Next(255));
            for (var i = 0; i < 17; i++)
            {
                screen.Fill(color);
                screen.Update();
                Video.WindowCaption = Events.Fps.ToString();
            }
=======
using System.Text;
using System.Threading.Tasks;

namespace IndianOstrich
{
    class Program
    {
        static void Main(string[] args)
        {
>>>>>>> 96287cb7e003558b9dded597a78cdfc54844c565
        }
    }
}
