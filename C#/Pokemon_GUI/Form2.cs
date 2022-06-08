namespace cs_form;

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

static class Program {
    [STAThread]
    static void Main() {
        Application.EnableVisualStyles();
        Application.Run(new Form1());
    }
}

class Form1 : Form{
    # nullable disable

    public Form1() {
    }

    Button button;
    void set_button (){
        button = new Button() {
            Text = "クリックしてください",
            Location = new Point(10, 10),
            Size = new Size(160, 40),
        };

        // イベントハンドラを登録
        button.Click += new EventHandler(button_Click);

        this.Controls.Add(button);
    }

    private void button_Click(object sender, EventArgs e){
        Form2 form2 = new Form2();
        form2.Show();
    }
}

public partial class Form2 : Form{
    public Form2(){
    }
}
