namespace cs_gui;
using System;
using System.Drawing;
using System.Windows.Forms;

public partial class pk_frame : Form {
    public pk_frame() {
        this.Text = "ポケモン図鑑";
        this.BackColor = SystemColors.Window;
        this.ClientSize = new Size(1000, 725);
        this.StartPosition = FormStartPosition.CenterScreen;
        set_frame();
        set_menu();
    }

    TabControl tab = new TabControl();
    Data_Panel pk_data_panel = new Data_Panel();
    Pic_Panel pk_pic_panel = new Pic_Panel();
    Calc_Panel pk_calc_panel = new Calc_Panel();
    Move_Panel pk_move_panel = new Move_Panel();
    Party_Panel pk_party_panel = new Party_Panel();
    Setting_Panel pk_setting_panel = new Setting_Panel();

    TabPage pk_search = new TabPage() {
        Name = "ポケモン検索",
        Text = "ポケモン検索"
    };
    TabPage pk_data = new TabPage() {
        Name = "ポケモン図鑑",
        Text = "ポケモン図鑑"
    };
    TabPage pk_move = new TabPage() {
        Name = "技一覧",
        Text = "技一覧"
    };
    TabPage pk_calc_damage = new TabPage() {
        Name = "ダメージ計算",
        Text = "ダメージ計算"
    };
    TabPage pk_party = new TabPage() {
        Name = "パーティ編成",
        Text = "パーティ編成"
    };
    TabPage pk_setting = new TabPage() {
        Name = "設定",
        Text = "設定"
    };

    private void set_frame() {
        tab.ClientSize = new Size(1000, 700);
        tab.Location = new Point(0, 25);
        pk_search.Controls.Add(pk_pic_panel);
        tab.TabPages.Add(pk_search);
        
        pk_data.Controls.Add(pk_data_panel);
        tab.TabPages.Add(pk_data);

        pk_move.Controls.Add(pk_move_panel);
        tab.TabPages.Add(pk_move);

        pk_calc_damage.Controls.Add(pk_calc_panel);
        tab.TabPages.Add(pk_calc_damage);

        pk_party.Controls.Add(pk_party_panel);
        tab.TabPages.Add(pk_party);

        pk_setting.Controls.Add(pk_setting_panel);        
        tab.TabPages.Add(pk_setting);

        this.Controls.Add(tab);   
    }

    MenuStrip menu = new MenuStrip();
    private void set_menu() {
        ToolStripMenuItem menu1 = new ToolStripMenuItem("新規");
        ToolStripMenuItem menu_exit = new ToolStripMenuItem("終了");
        # nullable disable
        menu_exit.Click += new EventHandler(form_close);

        ToolStripMenuItem menu_file = new ToolStripMenuItem("File");
        menu_file.DropDownItems.AddRange(new ToolStripItem[] {menu1, menu_exit});

        menu.Items.AddRange(new ToolStripItem[] {menu_file});

        this.Controls.Add(menu);
        this.MainMenuStrip = menu;
    }

    public void form_close (object sender, EventArgs e) {
        this.Close();
    }
}
